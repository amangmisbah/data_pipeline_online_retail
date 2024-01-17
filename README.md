# Data Pipeline Online Retail
# Dataset
  you can get dataset here https://www.kaggle.com/datasets/tunguz/online-retail

# Column Description
| Column      | Description                                       | Type     |
|-------------|---------------------------------------------------|----------|
| InvoiceNo   | Invoice number. A 6-digit integral number uniquely assigned to each transaction. If starts with 'c', indicates cancellation. | STRING   |
| StockCode   | Product (item) code. A 5-digit integral number uniquely assigned to each distinct product. | STRING   |
| Description | Product (item) name.                              | STRING   |
| Quantity    | Quantities of each product (item) per transaction. | INTEGER  |
| InvoiceDate | Invoice Date and time. Day and time when each transaction was generated. | TIMESTAMP|
| UnitPrice   | Unit price. Product price per unit in sterling.   | FLOAT    |
| CustomerID  | Customer number. A 5-digit integral number uniquely assigned to each customer. | INTEGER  |
| Country     | Country name. The name of the country where each customer resides. | STRING   |

# ARCHITECTURE
![ARCHITECTURE_DATA (1)](https://github.com/amangmisbah/data_pipeline_online_retail/assets/72803669/9f866211-5ad2-46d2-ac3b-2f58047a73d8)

# TOOLS
  1. Docker
  2. Airflow for orchrestation
  3. DBT (Data Build Tools) for Transformation
  4. Google Coud Storage for Data Lake
  5. Google Bigquery for Data Wrehouse

# GOALS PROJECT
  1. report_customer_invoices.sql:
  Objective: Generate a report showing the total number of invoices, total revenue, and country-related information with ISO codes for customers.
  Steps: Joining the fact table (fct_invoices) with the customer dimension table (dim_customer) based on the customer_id. Then, grouping the results by          country and ISO code of the customer and ordering them by total revenue in descending order.
  
  2. report_product_invoices.sql:
  Objective: Generate a report showing the total quantity sold for specific products.
  Steps: Joining the fact table (fct_invoices) with the product dimension table (dim_product) based on the product_id. Grouping the results by product_id,       stock_code, and description, and ordering them by the total quantity sold in descending order.
  
  3. report_year_invoices.sql:
  Objective: Generate a report showing the total number of invoices, total revenue, and time-related information for each year and month.
  Steps: Joining the fact table (fct_invoices) with the date and time dimension table (dim_datetime) based on datetime_id. Grouping the results by year and      month and ordering them by year and month.

# DATA WAREHOUSE
![Screenshot from 2024-01-18 00-26-38](https://github.com/amangmisbah/data_pipeline_online_retail/assets/72803669/09d074c6-7254-4f2a-ac39-11a774239086)
1. Staging area is raw data
2. Warehouse is Tansformation
3. Mart is table to achieve business goals

# ORCHESTRATION AND SCHEDULING WITH AIRFLOW
![Screenshot from 2024-01-18 00-44-37](https://github.com/amangmisbah/data_pipeline_online_retail/assets/72803669/dfe64bc9-8f79-4765-8c67-10e140f73945)



