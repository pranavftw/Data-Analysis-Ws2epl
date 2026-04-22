import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression

# =========================
# LOAD & PREPROCESS DATA
# =========================
df = pd.read_csv("water data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

# =========================
# BASIC INFO
# =========================
print("📊 Dataset Info:")
print(df.info())

print("\n📊 Summary Statistics:")
print(df.describe())

# =========================
# EFFICIENCY METRICS
# =========================
df['TDS_Efficiency'] = ((df['Raw_TDS'] - df['Treated_TDS']) / df['Raw_TDS']) * 100
df['Turbidity_Efficiency'] = ((df['Raw_Turbidity'] - df['Treated_Turbidity']) / df['Raw_Turbidity']) * 100

avg_tds_eff = df['TDS_Efficiency'].mean()
avg_turb_eff = df['Turbidity_Efficiency'].mean()

# =========================
# ROLLING AVERAGES
# =========================
df['TDS_Rolling'] = df['Treated_TDS'].rolling(window=5).mean()
df['Turbidity_Rolling'] = df['Treated_Turbidity'].rolling(window=5).mean()

# =========================
# PERFORMANCE SCORE
# =========================
df['Performance_Score'] = (
    0.6 * df['TDS_Efficiency'] +
    0.4 * df['Turbidity_Efficiency']
)

# =========================
# HEALTH STATUS
# =========================
def health_status(row):
    if row['Treated_Turbidity'] > 8 or row['Treated_TDS'] > 350:
        return "Critical"
    elif row['TDS_Efficiency'] < 60:
        return "Warning"
    else:
        return "Good"

df['Health_Status'] = df.apply(health_status, axis=1)

# =========================
# TREND PLOTS
# =========================

plt.figure()
plt.plot(df['Date'], df['Raw_TDS'], label='Raw TDS')
plt.plot(df['Date'], df['Treated_TDS'], label='Treated TDS')
plt.legend()
plt.title("TDS Trend Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(df['Date'], df['Raw_Turbidity'], label='Raw Turbidity')
plt.plot(df['Date'], df['Treated_Turbidity'], label='Treated Turbidity')
plt.legend()
plt.title("Turbidity Trend Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# ALERTS & ANOMALIES
# =========================
alerts = df[(df['Treated_Turbidity'] > 8) | (df['Treated_TDS'] > 350)]

print("\n⚠️ ALERTS (Threshold-based):")
print(alerts[['Date', 'Treated_TDS', 'Treated_Turbidity']])

# ML Anomaly Detection
features = df[['Treated_TDS', 'Treated_Turbidity']]

model = IsolationForest(contamination=0.1, random_state=42)
df['ML_Anomaly'] = model.fit_predict(features)

ml_anomalies = df[df['ML_Anomaly'] == -1]

print("\n🤖 ML Detected Anomalies:")
print(ml_anomalies[['Date', 'Treated_TDS', 'Treated_Turbidity']])

# =========================
# CORRELATION
# =========================
corr = df[['Raw_TDS', 'Raw_Turbidity']].corr()

print("\n📊 Correlation Matrix:")
print(corr)

if corr.iloc[0,1] > 0.9:
    print("\n🧠 Insight:")
    print("High correlation suggests contamination source affects both TDS and turbidity simultaneously.")

# =========================
# PREDICTION MODEL
# =========================
df['Day'] = np.arange(len(df))

lr_model = LinearRegression()
lr_model.fit(df[['Day']], df['Treated_TDS'])

future_day = pd.DataFrame({'Day': [len(df) + 5]})
prediction = lr_model.predict(future_day)

# =========================
# EXECUTIVE SUMMARY
# =========================
print("\n" + "="*50)
print("📄 EXECUTIVE SUMMARY")
print("="*50)

print(f"📅 Data Period: {df['Date'].min().date()} → {df['Date'].max().date()}")
print(f"📊 Records Analyzed: {len(df)}")

print(f"\n💧 Avg TDS Efficiency: {avg_tds_eff:.2f}%")
print(f"🌫️ Avg Turbidity Efficiency: {avg_turb_eff:.2f}%")

print(f"\n⚠️ Total Alerts: {len(alerts)}")
print(f"🤖 ML Anomalies: {len(ml_anomalies)}")

print(f"\n📈 Predicted Future TDS: {prediction[0]:.2f}")
print("="*50)

# =========================
# TOP / WORST DAYS
# =========================
worst_days = df.sort_values(by='Treated_TDS', ascending=False).head(5)

print("\n🔥 Top 5 Worst TDS Days:")
print(worst_days[['Date', 'Treated_TDS', 'TDS_Efficiency']])

best_days = df.sort_values(by='Performance_Score', ascending=False).head(5)

print("\n🏆 Top 5 Best Performance Days:")
print(best_days[['Date', 'Performance_Score']])

# =========================
# MONTHLY ANALYSIS
# =========================
df['Month'] = df['Date'].dt.to_period('M')

monthly = df.groupby('Month').mean(numeric_only=True)

print("\n📅 Monthly Average Performance:")
print(monthly[['Treated_TDS', 'Treated_Turbidity', 'Performance_Score']])

# =========================
# DISTRIBUTION PLOT
# =========================
plt.figure()
plt.hist(df['Treated_TDS'], bins=10)
plt.title("Distribution of Treated TDS")
plt.xlabel("TDS")
plt.ylabel("Frequency")
plt.show()

# =========================
# EXPORT FILES
# =========================
df.to_csv("final_analysis.csv", index=False)
df.to_excel("final_analysis.xlsx", index=False)

print("\n✅ Files exported: final_analysis.csv & final_analysis.xlsx")
