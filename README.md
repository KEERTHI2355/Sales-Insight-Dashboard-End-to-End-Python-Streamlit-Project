📊 Sales Insight Dashboard — End-to-End Python & Streamlit Project

This project delivers a complete Sales Insights Dashboard using Python, Pandas, Matplotlib/Seaborn, and Streamlit.
It demonstrates practical skills in:
-> Data Cleaning
-> Feature Engineering
-> Exploratory Data Analysis (EDA)
-> KPI Computation
-> Data Visualization
-> Building an Interactive Dashboard
-> Export-to-Excel Reporting
This is a job-ready project suitable for Data Analyst, BI Analyst, and Data Science portfolios.


🚀 Project Overview
The goal of this project is to analyze a synthetic retail sales dataset and build:
✔ A clean, well-structured dataset
✔ EDA with charts and aggregated insights
✔ KPI calculations (Revenue, AOV, Top Product, Top Region, etc.)
✔ A fully interactive Streamlit Dashboard
✔ Excel Report export functionality


📁 Project Structure
sales-insight-dashboard/
│
├── data/
│   ├── Generate_Sales_Dataset.py
│   ├── sales_cleaned.csv
│   └── sales_dataset.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_eda.ipynb
│   └── 03_eda(plots).ipynb
│
├── charts/
│   ├── product_sales.png
│   ├── category_sales.png
|   ├── region_sales.png
│   └── other charts
│
├── app/
│   └── app.py
│
├── src/
│   └── KPI.py
│
└── README.md


🧰 Technologies Used
-> Python
-> Pandas, NumPy
-> Matplotlib, Seaborn
-> Streamlit
-> xlsxwriter (for Excel export)
-> VS Code (editor)


📥 Step 1 — Install Python & VS Code
-> Install Python (3.10+ recommended)
-> Install VS Code + Python Extension


📦 Step 2 — Create Virtual Environment & Install Dependencies
Activate:
-> python -m venv venv

Windows
-> venv\Scripts\activate

Install packages:
-> pip install pandas numpy matplotlib seaborn streamlit xlsxwriter


📄 Step 3 — Add the Dataset
Place the sales_dataset.csv inside the data/ folder.

Dataset Columns:
-> Order ID
-> Order Date
-> Product
-> Category
-> Region
-> Quantity
-> Price
-> Sales(Price*Quantity)


📘 Step 4 — Exploratory Data Analysis (EDA)
Performed inside Jupyter Notebooks:

✔ Key Steps:
-> Load dataset
-> Check shape, dtypes, missing values
-> Add computed field:
    df['order_month'] = df['Order Date'].dt.to_period('M').astype(str)
-> Groupwise aggregations:
    - Product-wise Sales
    - Category-wise Sales
    - Region-wise Sales

-> Generate visualizations:
    - Top Products (Bar)
    - Category Share (Pie)
    - Regional Sales (Bar)
All charts stored in /charts.


📌 Step 5 — KPI Calculations
Using Pandas groupby:

-> KPIs include:
    - Total Revenue
    - Total Orders
    - Average Order Value (AOV)
    - Top-Selling Product
    - Top Revenue Region
Stored for dashboard display.


🖥 Step 6 — Build Streamlit Dashboard
app/app.py contains:

✔ Sidebar Filters
    - Month
    - Region
    - Category

✔ KPI Cards
    - Displayed using styled HTML blocks.

✔ Visual Insights Section
    - Using Matplotlib/Seaborn inside Streamlit.

✔ Export-to-Excel Button
  -> Uses:
      - import xlsxwriter
      - import io

✔ Exports:
-> KPI summary
-> Aggregation tables
-> Raw data sample


▶ Step 7 — Run the Streamlit App
-> Run from repository root:
    streamlit run app/app.py
The dashboard opens in your browser.


📤 Step 8 — Generate Excel Report
Inside the dashboard:
➡️ Click Download Excel Report

Includes:
-> KPI sheet
-> Category summary
-> Top Products
-> Region summary
-> Sample raw data


📝 Step 9 — Final Deliverables
✔ Cleaned & Engineered Dataset
✔ EDA Notebooks
✔ Visualization Charts
✔ KPI Calculations
✔ Interactive Streamlit Dashboard
✔ Excel Reports
✔ Portfolio-Ready GitHub Repository
