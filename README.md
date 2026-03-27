# 🏠 NYC Airbnb Data Pipeline & Analysis

This project demonstrates an end-to-end data pipeline built using Python, SQLite, and Apache Airflow concepts. The goal is to process, transform, and analyze Airbnb listing data for insights into pricing, demand, and host activity.

---

# 📌 Project Overview

The pipeline performs the following steps:

1. Extract raw Airbnb data from CSV  
2. Validate dataset structure and quality  
3. Clean missing values and inconsistencies  
4. Generate analytical features  
5. Load processed data into SQLite database  
6. Perform SQL-based analysis  
7. Visualize insights using Python  

---

# ⚙️ Technologies Used

- Python (Pandas, NumPy)
- SQLite
- Apache Airflow (DAG design)
- Seaborn & Matplotlib
- VS Code

---

# 🏗️ Pipeline Architecture
Raw Data → Validation → Cleaning → Feature Engineering → SQLite → SQL Analysis → Visualization


---

# 📂 Project Structure

airbnb-data-pipeline/
│
├── dags/ # Airflow DAG definition
├── scripts/ # ETL scripts
├── notebooks/ # Analysis & visualization
├── sql/ # SQL queries
├── data/
│ └── processed/ # Cleaned & featured data
├── database/
│ └── nyc.db # SQLite database
├── .gitignore
├── README.md
└── requirements.txt


---

# 🔄 ETL Pipeline Steps

### 1. Data Cleaning
- Handled missing values
- Removed duplicates
- Validated numerical ranges

### 2. Feature Engineering
Created new analytical columns:
- `price_category`
- `is_active`
- `price_per_review`
- `review_activity_level`

### 3. Data Loading
- Stored processed data in SQLite (`airbnb_listings` table)

### 4. Data Quality Checks
- Ensured no invalid values (e.g. negative prices)
- Verified row counts and constraints

---

# 📊 Key Analyses

### Average Price by Neighbourhood
- Identifies most expensive areas

### Top Hosts by Listings
- Reveals commercial vs individual usage

### Price vs Popularity
- Finds best value listings

### Review Activity Analysis
- Shows active vs inactive listings

---

# 📈 Example Insights

- Manhattan has the highest average listing price  
- A small number of hosts manage a large number of listings  
- Some low-priced listings receive high engagement (high reviews)  
- Listing activity varies significantly across regions  

---

# 🚀 How to Run

1. Clone repository
2. Install dependencies
3. Run scripts:
python scripts/clean_airbnb.py
python scripts/feature_engineering.py
python scripts/load_to_sqlite.py
python scripts/data_quality_checks.py


4. Open notebook for analysis:


notebooks/airbnb_dashboard.ipynb


---

# 💡 Future Improvements

- Integrate real-time data ingestion
- Deploy Airflow for automated scheduling
- Connect to cloud database (PostgreSQL / BigQuery)
- Build dashboard with Power BI or Streamlit

---

# 👩‍💻 Author

Zeynep Ozge