import streamlit as st
import pandas as pd
import numpy as np
import io

# ---------- CONFIG ----------
# Use whichever path you have the CSV at. Example local path you shared:
DATA_PATH = r"data\sales_dataset.csv"
# If you keep dataset in repo/data/ then use: DATA_PATH = "data/sales_dataset.csv"

# ---------- LOAD ----------
@st.cache_data
def load_data(path):
    df = pd.read_csv(path, parse_dates=["Order Date"], low_memory=False)
    # ensure order_month column exists (string)
    if "order_month" not in df.columns:
        df["order_month"] = df["Order Date"].dt.to_period("M").astype(str)
    return df

df = load_data(DATA_PATH)

# Function to export to EXCEL
def to_excel_bytes(df: pd.DataFrame) -> bytes:
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="raw_data", index=False)
        # example summaries:
        df.groupby("Product")["Sales"].sum().reset_index().to_excel(writer, sheet_name="top_products", index=False)
        df.groupby("Category")["Sales"].sum().reset_index().to_excel(writer, sheet_name="category_summary", index=False)
        df.groupby("Region")["Sales"].sum().reset_index().to_excel(writer, sheet_name="region_summary", index=False)
    return buffer.getvalue()

# ---------- FILTERS ----------
st.sidebar.header("Filters")
min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()
date_range = st.sidebar.date_input("Order date range", [min_date, max_date], min_value=min_date, max_value=max_date)

selected_regions = st.sidebar.multiselect("Region", options=df["Region"].unique(), default=list(df["Region"].unique()))
selected_cats = st.sidebar.multiselect("Category", options=df["Category"].unique(), default=list(df["Category"].unique()))


# UI - should be placed where the export button is needed
st.sidebar.markdown("### Export")
excel_bytes = to_excel_bytes(df)
st.sidebar.download_button(
    label="Download Excel report",
    data=excel_bytes,
    file_name="sales_report.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# ---------- APPLY FILTERS ----------
start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
mask = (df["Order Date"] >= start) & (df["Order Date"] <= end) & df["Region"].isin(selected_regions) & df["Category"].isin(selected_cats)
df_f = df.loc[mask].copy()

# ---------- KPIs ----------
st.title("Sales Insights — KPI Overview")

# KPI calculations
total_revenue = df_f["Sales"].sum()
total_orders = df_f.shape[0]
avg_order_value = total_revenue / total_orders if total_orders > 0 else 0

# monthly revenue for growth calculation
monthly = df_f.groupby("order_month")["Sales"].sum().sort_index()
monthly_last = monthly.iloc[-1] if len(monthly) >= 1 else np.nan
monthly_prev = monthly.iloc[-2] if len(monthly) >= 2 else np.nan
monthly_growth = ((monthly_last - monthly_prev) / monthly_prev * 100) if pd.notna(monthly_prev) and monthly_prev != 0 else np.nan

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Avg Order Value", f"₹{avg_order_value:,.0f}")
# show monthly growth with sign
if pd.notna(monthly_growth):
    col4.metric("MoM Revenue Growth", f"{monthly_growth:.2f}%", delta=f"{monthly_last:,.0f}")
else:
    col4.metric("MoM Revenue Growth", "N/A")

st.markdown("---")

# show top product
top_product = df_f.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(1)
if not top_product.empty:
    p_name = top_product.index[0]
    p_sales = top_product.values[0]
    st.subheader("Top Product (by Sales)")
    st.write(f"**{p_name}** — ₹{p_sales:,.0f}")

# add a small table of top 5 products
top5 = df_f.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5).reset_index()
st.table(top5.assign(Sales=top5["Sales"].apply(lambda x: f"₹{x:,.0f}")))

# ---------- Basic charts below ----------
st.markdown("### Monthly Revenue Trend")
st.line_chart(monthly)

st.markdown("### Sales by Region")
region_sales = df_f.groupby("Region")["Sales"].sum().reindex(df_f["Region"].unique())
st.bar_chart(region_sales)

