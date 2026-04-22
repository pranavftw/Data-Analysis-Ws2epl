# 💧 Water Quality Analysis & Monitoring System

## 📌 Overview

This project focuses on analyzing water treatment plant data using key parameters such as **TDS (Total Dissolved Solids)** and **Turbidity**.
The goal is to evaluate system performance, detect anomalies, and generate actionable insights using data analytics and machine learning.

---

## 🎯 Objectives

* Monitor water quality trends over time
* Evaluate treatment efficiency
* Detect anomalies in system performance
* Generate automated insights and reports
* Predict future system behavior

---

## 🛠️ Technologies Used

* Python
* Pandas (Data Processing)
* NumPy
* Matplotlib (Visualization)
* Scikit-learn (Machine Learning)
* Excel (Reporting)

---

## 📂 Dataset Description

* Time Period: July 2025 – December 2025
* Total Records: 67
* Parameters:

  * Raw TDS
  * Treated TDS
  * Raw Turbidity
  * Treated Turbidity

---

## ⚙️ Workflow / Pipeline

### 1️⃣ Data Loading & Preprocessing

* Loaded dataset using Pandas
* Converted Date column to datetime format
* Sorted data for time-series analysis

👉 Purpose: Ensures accurate chronological analysis

---

### 2️⃣ Efficiency Calculation

* TDS Efficiency
* Turbidity Efficiency

👉 Helps evaluate how effectively the treatment system removes contaminants

---

### 3️⃣ Rolling Average Analysis

* Applied 5-day rolling average

👉 Purpose:

* Smooths fluctuations
* Reveals true trend

---

### 4️⃣ Performance Score (KPI)

* Combined efficiency metrics into a single score

👉 Purpose:

* Provides overall system performance indicator
* Simplifies monitoring

---

### 5️⃣ Health Status Classification

* Classified system into:

  * Good
  * Warning
  * Critical

👉 Purpose:

* Mimics real-world monitoring systems

---

### 6️⃣ Anomaly Detection

#### 🔹 Threshold-Based:

* Turbidity > 8
* TDS > 350

#### 🔹 Machine Learning:

* Isolation Forest

👉 Purpose:

* Detect unusual system behavior
* Enable proactive maintenance

---

### 7️⃣ Correlation Analysis

* Measured relationship between raw TDS and turbidity

👉 Insight:

* Strong correlation indicates common contamination sources

---

### 8️⃣ Predictive Modeling

* Used Linear Regression to forecast future TDS

👉 Purpose:

* Anticipate system performance
* Support decision-making

---

### 9️⃣ Reporting & Export

* Generated:

  * Excel file
  * CSV file
  * Console summary

👉 Purpose:

* Deliver insights in usable formats

---

## 📊 Output Explanation

### 📌 Efficiency Metrics

* Average TDS Efficiency ≈ 63.9%
* Average Turbidity Efficiency ≈ 88.1%

👉 Interpretation:

* Turbidity removal is highly effective
* TDS reduction is moderate

---

### ⚠️ Alerts (Threshold-Based)

* Detected high TDS and turbidity values in early July

👉 Meaning:

* Possible filtration inefficiency
* Chemical imbalance

---

### 🤖 ML Anomalies

* Detected both:

  * High spikes
  * Unusually low values

👉 Meaning:

* ML captures deeper patterns beyond thresholds

---

### 📉 Efficiency Drops

* Observed on specific days

👉 Possible Causes:

* Filter clogging
* Operational instability

---

### 🔗 Correlation (0.97)

* Strong positive relationship

👉 Insight:

* Same contamination source affecting both parameters

---

### 📈 Prediction

* Future TDS ≈ 239

👉 Meaning:

* System performance improving over time

---

## 📊 Graph Explanations

### 📉 TDS Trend Graph

* Shows raw vs treated TDS over time

👉 Insight:

* Clear reduction after treatment
* System effectiveness visible

---

### 🌫️ Turbidity Trend Graph

* Raw vs treated turbidity

👉 Insight:

* Significant drop → efficient filtration

---

### 📊 Efficiency Trend Graph

* TDS & Turbidity efficiency over time

👉 Insight:

* Stability and consistency of system

---

### 📈 Rolling Average Graph

* Smooth trend of treated TDS

👉 Insight:

* Removes noise
* Shows actual performance trend

---

### 📉 Distribution Plot

* Frequency of treated TDS values

👉 Insight:

* Identifies spread and outliers
* Evaluates consistency

---

## 🧠 Key Insights

* System performs consistently well for turbidity removal
* Moderate efficiency in TDS reduction
* Early-stage anomalies indicate operational issues
* Strong correlation suggests shared contamination source
* Predictive model indicates improving system trend

---

## 🚀 Future Improvements

* Real-time monitoring dashboard (Streamlit)
* Advanced ML models for prediction
* Integration with IoT sensors
* Automated alert system (email/SMS)

---

## 👨‍💻 Author

**Pranav More**
