import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create Sample Healthcare Dataset
# Data includes Age, Glucose Level, and Blood Pressure for 100 patients
data = {
    'Patient_ID': range(1, 101),
    'Age': np.random.randint(20, 80, 100),
    'Glucose_Level': np.random.randint(70, 200, 100),
    'Blood_Pressure': np.random.randint(60, 120, 100),
    'Diabetes_Risk': np.random.choice([0, 1], 100, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# 2. Data Cleaning and Initial Statistics
print("--- Dataset Overview ---")
print(df.head())
print("\n--- Basic Statistics ---")
print(df.describe())

# 3. Data Analysis (Correlation between Age and Glucose)
correlation = df['Age'].corr(df['Glucose_Level'])
print(f"\nCorrelation between Age and Glucose Level: {correlation:.2f}")

# 4. Data Visualization using Seaborn
plt.figure(figsize=(10, 6))

# Scatter Plot to show relationship between Age and Glucose Level
sns.scatterplot(data=df, x='Age', y='Glucose_Level', hue='Diabetes_Risk', palette='viridis')
plt.title('Patient Age vs Glucose Level (Risk Analysis)')
plt.xlabel('Age')
plt.ylabel('Glucose Level (mg/dL)')
plt.legend(title='Diabetes Risk (1=High, 0=Low)')

# Save the plot as an image (Useful for GitHub portfolio)
plt.savefig('healthcare_analysis_plot.png')
print("\nPlot saved as 'healthcare_analysis_plot.png'")

# 5. Data Summary using Groupby
risk_summary = df.groupby('Diabetes_Risk')[['Glucose_Level', 'Blood_Pressure']].mean()
print("\n--- Average Levels by Risk Group ---")
print(risk_summary)
