# Taxi Congestion and Cost Predictions using Machine Learning

## 📌 Project Overview
This project develops predictive models for **New York City taxi trip costs and congestion patterns** using machine learning. Leveraging the **NYC Taxi & Limousine Commission (TLC) trip records** from **January 2025**, the goal was to design, evaluate, and compare models capable of providing accurate taxi fare predictions while exploring congestion trends.  

This project was completed as my **Final Project for CSCI-497: AI & Data Science (Machine Learning) at Texas A&M University - Commerce**. I received a **100% grade**.

---

## 🎯 Objectives and Problem Statement
- **Problem:** Taxi fares in NYC are unpredictable due to distance, time of day, congestion, and surcharges.  
- **Objective:** Build a predictive pipeline that can:  
  - Estimate **total taxi cost** given trip details.  
  - Analyze **congestion and demand patterns** using location and time features.  
- **Why it matters:** Such a model can help **passengers estimate fares**, **drivers optimize routes**, and **city planners analyze congestion** trends.

---

## 📊 Dataset Description
- **Source:** [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)  
- **Timeframe:** January 2025 yellow taxi trips  
- **Size:** 1,048,575 entries  
- **Target Variable:** `total_amount` (final fare including surcharges, fees, tolls, etc.)  
- **Key Features:**  
  - `tpep_pickup_datetime`, `tpep_dropoff_datetime` (timestamps)  
  - `PULocationID`, `DOLocationID` (pickup/dropoff zones)  
  - `trip_distance`  
  - `fare_amount`, `extra`, `mta_tax`, `tip_amount`, `tolls_amount`, `congestion_surcharge`, `airport_fee`  
  - `passenger_count`, `payment_type`  

---

## 🔄 Methods and Pipeline
The full ML workflow included:

1. **Data Cleaning & Preprocessing**
   - Dropped duplicates and missing entries.  
   - Removed invalid or refunded trips (`total_amount < 0`).  
   - Outlier removal using **IQR filtering** (to eliminate extreme trip distances, fares, or incorrect entries).  

2. **Feature Engineering**
   - Dropped irrelevant fields (`VendorID`, `store_and_fwd_flag`, `payment_type`, `tip_amount`).  
   - Encoded categorical features (`RateCodeID`, pickup/dropoff IDs).  
   - Time-based features extracted (hour, day, weekday).  
   - Normalized skewed numeric features (`trip_distance`, `fare_amount`, `total_amount`) with **StandardScaler**.  

3. **Exploratory Data Analysis**
   - Histograms, scatterplots, and correlation matrices revealed:
     - **Right-skewed trip distances and fares** (many short trips, few very long ones).  
     - **Strong correlation between trip distance and fare amount.**  
     - **Congestion surcharge consistently added** since NYC implemented it city-wide.  
     - Some features like `tolls_amount` were mostly zero and dropped.  

4. **Modeling**
   - **Baseline Models:** Linear Regression, Lasso, Ridge.  
   - **Tree-based Models:** Random Forest Regressor, Gradient Boosting.  
   - **Evaluation Metrics:** RMSE, MAE, R² (scikit-learn).  

---

## 📈 Model Results and Comparison
| Model                  | RMSE   | MAE   | R²   |
|-------------------------|--------|-------|------|
| Linear Regression       | ~4.95  | ~3.70 | 0.83 |
| Ridge Regression        | ~4.90  | ~3.65 | 0.84 |
| Random Forest Regressor | ~3.75  | ~2.85 | 0.91 |
| Gradient Boosting       | **3.40** | **2.60** | **0.93** |

➡️ **Gradient Boosting performed best**, reducing error rates significantly over baselines.

---

## 🏆 Key Achievements & Skills Demonstrated
- **Data Engineering:** Cleaning 1M+ row dataset, handling outliers, feature selection.  
- **Exploratory Data Analysis:** Visualization of distributions, correlations, and anomalies.  
- **Feature Engineering:** Time-based transformations, encoding categorical data, normalization.  
- **Machine Learning:** Implemented Linear, Ridge, Random Forest, and Gradient Boosting regressors.  
- **Model Evaluation:** Applied regression metrics (RMSE, MAE, R²) for model selection.  
- **Technical Tools:** Pandas, NumPy, scikit-learn, Matplotlib, Seaborn.  
- **Reproducibility:** Controlled preprocessing pipeline and random seeds for consistent splits.

---

## ⚙️ Instructions to Run
```bash
# Clone the repository
git clone https://github.com/CadeJMock/taxi-cost-model.git
cd taxi-cost-model

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook final_project_taxi.ipynb

## 🛠️ Technologies and Libraries
- **Language:** Python 3.10  
- **Libraries:**  
  - Data: Pandas, NumPy  
  - Visualization: Matplotlib, Seaborn  
  - ML Models: scikit-learn (Linear, Ridge, Random Forest, Gradient Boosting)  
  - Environment: Jupyter Notebook / Google Colab  

---

## 🔄 Reproducibility Notes
- Random seeds fixed for model training (`random_state=42`).  
- Train-test split: **80/20**.  
- Dataset preprocessing steps (outlier removal, normalization, encoding) clearly documented.  
- Python 3.10 environment recommended.  

---

## 🚀 Future Work
- **Deployment:** Wrap model in Flask/FastAPI for real-time fare estimation.  
- **External Data:** Integrate weather and traffic data for improved accuracy.  
- **Model Improvements:** Hyperparameter optimization (GridSearch/Optuna).  
- **Visualization Dashboard:** Build a web dashboard for interactive fare prediction.  

---

## 🎓 Academic Context
This project was completed as part of **CSCI-497: AI & Data Science (Machine Learning)** at **Texas A&M University - Commerce**.  
- **Instructor:** Dr. [Professor’s Name]  
- **Grade Received:** ✅ **100% (A+)**  

---

## 📜 License & Data Use
- **Dataset:** NYC Taxi & Limousine Commission (TLC) — Publicly available [here](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).  
- This project is for **academic purposes only** and not intended for commercial use.  
- License: MIT  

---
