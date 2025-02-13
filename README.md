Cryptocurrency Financial Data Analysis & Visualization Project

Overview

This project processes, analyzes, and visualizes historical cryptocurrency financial data. It demonstrates key skills in data cleaning, aggregation, and visualization using Python (Pandas, Matplotlib) and Power BI.
Project Components

  Data Processing with Python
        Data Loading: Import raw data from consolidated_coin_data.csv.
        Data Cleaning: Convert dates and numeric values (e.g., removing commas) into proper formats.
        Feature Engineering: Create new columns:
            Daily Change: The difference between Close and Open.
            Volatility: The difference between High and Low.
        Aggregation: Calculate metrics such as:
            Average closing price per cryptocurrency.
            Total trading volume per cryptocurrency.
            Identify the day with the greatest growth and the day with the highest volatility.
        Export: Save a detailed data analysis report to data_analysis.txt and export cleaned data to modified_consolidated_coin_data.csv.

  Visualization with Python
        Generate visual insights like a market capitalization trend for the top 3 cryptocurrencies.
        Plot dynamic charts for price changes, trading volumes, daily changes, and volatility.

  Visualization with Power BI
        Import modified_consolidated_coin_data.csv into Power BI.
        Build interactive dashboards featuring:
            Line Charts for price dynamics (Open vs. Close).
            Bar Charts for trading volume.
            Tables/Cards highlighting maximum daily growth and highest volatility.
            Slicers for filtering data by cryptocurrency.
        Ensure all visuals are synchronized through a slicer for a selected cryptocurrency, allowing you to view the complete history of one coin.
