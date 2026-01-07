# Healthcare-Data-Analysis
Python-based tool for analyzing healthcare data to identify disease risk factors.Python-based tool for analyzing healthcare data to identify disease risk factors.
Description
This project utilizes an automated Python script to analyze a synthetic healthcare record dataset. The primary objective is to identify the statistical correlation between a patient's Age and Glucose Level, providing insights into diabetes risk factors.
Technologies & Libraries Used
Python
Pandas (pd): Used for data structure creation and manipulation.
NumPy (np): Used for generating synthetic data (randint, choice) and mathematical operations.
Seaborn (sns) & Matplotlib (plt): Used for data visualization (e.g., scatter plots) and correlation matrix generation.
Jupyter Notebook: The entire analysis was conducted in an interactive notebook environment.
Project Code
The complete analysis methodology is showcased in the code block below:
python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Generation
# Creates a synthetic dataset for 100 patients with Age, Glucose Level, Blood Pressure, and Diabetes Risk (0=Low, 1=High)
data = {
    'Age': np.random.randint(20, 70, 100),
    'Glucose_Level': np.random.randint(70, 200, 100),
    'Blood_Pressure': np.random.randint(80, 130, 100),
    'Diabetes_Risk': np.random.choice(, 100, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# 2. Data Cleaning and Initial Statistics
print("--- Dataset Overview ---")
print(df.head())
print("\n--- Basic Statistics ---")
print(df.describe())

# 3. Data Analysis (Correlation between Age and Glucose Level)
correlation = df['Age'].corr(df['Glucose_Level'])
print(f"\nCorrelation between Age and Glucose Level: {correlation:.2f}")

# 4. Data Visualization using Seaborn
plt.figure(figsize=(10, 6))
# Scatter Plot to show relationship, using a colorblind-friendly 'viridis' palette
sns.scatterplot(data=df, x='Age', y='Glucose_Level', hue='Diabetes_Risk', palette='viridis')
plt.title('Patient Age vs Glucose Level with Diabetes Risk')
plt.xlabel('Age')
plt.ylabel('Glucose Level (mg/dL)')
plt.legend(title='Diabetes Risk')

# Save the plot as an image file (e.g., in PNG format)
plt.savefig('healthcare_analysis_plot.png')
print("\nPlot saved as 'healthcare_analysis_plot.png'")

# 5. Data Summary using Groupby
risk_summary = df.groupby('Diabetes_Risk')[['Age', 'Glucose_Level', 'Blood_Pressure']].mean()
print("\n--- Average Levels by Risk Group ---")
print(risk_summary)
Use code with caution.

Getting Started
To run this project locally, use the following commands to install the necessary libraries:
bash
pip install pandas numpy seaborn matplotlib
Use code with caution.

Then, simply run your Jupyter Notebook or Python file.
