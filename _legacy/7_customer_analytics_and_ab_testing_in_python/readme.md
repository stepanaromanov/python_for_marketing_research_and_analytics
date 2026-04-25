# Description 

I commenced the course with a concise introduction to the upcoming content, setting the stage for a comprehensive exploration. The focus then shifted to Key Performance Indicators (KPIs), where I developed the ability to identify and define meaningful KPIs through a blend of critical thinking and Python tools. This practical and widely applicable approach laid the groundwork for the subsequent discussion on A/B testing.

Building on this foundation, I delved into the dynamic realm of visualizing, manipulating, and exploring KPIs as they evolve over time. Examples were utilized to demonstrate how to work with datetime objects, enabling the calculation of metrics per unit time. Techniques for graphing different data segments and applying smoothing functions were explored to uncover hidden trends. The chapter culminated in a comprehensive walkthrough, demonstrating how exploratory data analysis of customer data can pinpoint issues, introducing various functions in a highly generalizable manner.

Transitioning seamlessly into A/B testing, I acquired the mathematical knowledge and skills necessary for designing and successfully planning such tests. This involved determining experimental units, calculating sample sizes, and an introduction to the functions and code essential for statistical testing. Post A/B test execution, I mastered the art of data analysis and effective communication of results.

To enrich the understanding of statistical significance and confidence intervals, I interwove theoretical concepts with practical tools, demonstrating how to calculate them directly from the data. The chapter concluded with insights into visually and effectively communicating these results.

This holistic approach not only equips me with a strong theoretical foundation but also demonstrates my ability to apply these concepts practically using Python tools, ensuring a well-rounded skill set in data analysis and experimental design.


# About Dataset

https://www.kaggle.com/datasets/rishikumarrajvansh/marketing-insights-for-e-commerce-company/data

## Marketing Insights for E-Commerce Company

Transaction data has been provided for the period of 1st Jan 2019 to 31st Dec 2019. 


The below data sets have been provided:

Online_Sales.csv: This file contains actual orders data (point of Sales data) at transaction level with below variables.
CustomerID: Customer unique ID
Transaction_ID: Transaction Unique ID
Transaction_Date: Date of Transaction
Product_SKU: SKU ID – Unique Id for product
Product_Description: Product Description
Product_Cateogry: Product Category
Quantity: Number of items ordered
Avg_Price: Price per one quantity
Delivery_Charges: Charges for delivery
Coupon_Status: Any discount coupon applied

Customers_Data.csv: This file contains customer’s demographics.
CustomerID: Customer Unique ID
Gender: Gender of customer
Location: Location of Customer
Tenure_Months: Tenure in Months

Discount_Coupon.csv: Discount coupons have been given for different categories in different months
Month: Discount coupon applied in that month
Product_Category: Product category
Coupon_Code: Coupon Code for given Category and given month
Discount_pct: Discount Percentage for given coupon

Marketing_Spend.csv: Marketing spend on both offline & online channels on day wise.
Date: Date
Offline_Spend: Marketing spend on offline channels like TV, Radio, NewsPapers, Hordings etc…
Online_Spend: Marketing spend on online channels like Google keywords, facebook etc..

Tax_Amount.csv: GST Details for given category
Product_Category: Product Category
GST: Percentage of GST