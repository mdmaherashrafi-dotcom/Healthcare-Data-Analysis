import sqlite3
import pandas as pd
import matplotlib
# Use 'Agg' backend to ensure the script runs on servers without a display
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns
import os
import logging

# =================================================================
# PROJECT: Production-Ready Automated Business Intelligence System
# AUTHOR: MD MAHER ASHRAFI
# FEATURES: Professional Logging, Non-GUI Backend, Error Handling
# =================================================================

# Setting up professional logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("business_analysis.log"),
        logging.StreamHandler()
    ]
)

class BusinessAnalyzer:
    def __init__(self, db_name='business_intelligence.db', csv_name='sales_data.csv'):
        self.db_name = db_name
        self.csv_name = csv_name
        self.conn = None

    def create_dynamic_csv(self):
        """Simulating a dynamic data source (CSV) for the pipeline."""
        if not os.path.exists(self.csv_name):
            data = {
                'Category': ['Healthcare', 'Electronics', 'Fashion', 'Home Decor', 'Food & Bev'],
                'Revenue': [95000, 82000, 55000, 40000, 32000],
                'Cost': [42000, 58000, 35000, 18000, 14000],
                'Region': ['Dhaka', 'Chittagong', 'Sylhet', 'Dhaka', 'Rajshahi']
            }
            df = pd.DataFrame(data)
            df.to_csv(self.csv_name, index=False)
            logging.info(f"Dynamic Data Source Created: {self.csv_name}")

    def run_pipeline(self):
        try:
            logging.info("Initializing SQL Database Connection...")
            self.conn = sqlite3.connect(self.db_name)
            
            self.create_dynamic_csv()
            raw_data = pd.read_csv(self.csv_name)
            raw_data.to_sql('sales_records', self.conn, if_exists='replace', index=False)
            logging.info("Data Ingestion from CSV to SQL Table completed successfully.")

            # Advanced SQL Query
            query = """
                SELECT Category, Revenue, (Revenue - Cost) AS Net_Profit,
                ROUND(((Revenue - Cost) / Revenue * 100), 2) AS Profit_Margin
                FROM sales_records
                WHERE Profit_Margin > 15
                ORDER BY Net_Profit DESC
            """
            analysis_df = pd.read_sql_query(query, self.conn)

            logging.info("SQL Analysis Completed. Preparing Impact Report...")
            print("\n" + "="*40)
            print("       BUSINESS IMPACT REPORT       ")
            print("="*40)
            print(analysis_df)
            print("-" * 40)

            self.generate_dashboard(analysis_df)

        except sqlite3.Error as e:
            logging.error(f"SQL Database Error: {e}")
        except Exception as e:
            logging.error(f"System Error: {e}")
        finally:
            if self.conn:
                self.conn.close()
                logging.info("Database connection closed.")

    def generate_dashboard(self, df):
        """Generating professional BI visualization."""
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Category', y='Net_Profit', data=df, palette='viridis')
        
        plt.title('Business Intelligence: Net Profit Analysis', fontsize=14)
        plt.xlabel('Category')
        plt.ylabel('Net Profit ($)')
        
        output_file = 'bi_dashboard_output.png'
        plt.savefig(output_file)
        logging.info(f"Visualization saved successfully as {output_file}")

if __name__ == "__main__":
    analyzer = BusinessAnalyzer()
    analyzer.run_pipeline()
