# Corporate Financial Performance & Cost Intelligence
## Dataset Guide

### Dataset status — read this before using it
This is a **synthetic educational dataset** created for a Data Analytics portfolio project. It uses recognizable real-world car model and manufacturer names to make the product categories easier to understand, but **none of the financial figures are actual company data**. Do not present these costs, revenues, profits, budgets, or plant allocations as reported financial results of Maruti Suzuki, Hyundai, Tata Motors, or Mahindra.

For a clear portfolio framing, describe this as a fictional financial benchmarking scenario using familiar Indian car models. Plant assignments are illustrative and are not claims about where each named model is manufactured.

### Coverage
- Period: April 2024 to March 2026
- Rows: 480 monthly plant-and-model records
- Columns: 15
- Plants: four illustrative plant labels
- Models: Maruti Suzuki Swift, Hyundai Creta, Tata Nexon, Maruti Suzuki Dzire, Mahindra Scorpio-N
- Currency: Indian Rupees (INR)

### Column dictionary
| Column | Meaning |
|---|---|
| Month | Month-start date for the record |
| Manufacturer | Brand/manufacturer name associated with the model |
| Plant | Illustrative plant label used for scenario analysis; not an actual production assignment |
| Car_Model | Recognizable car model name |
| Units_Produced | Synthetic number of cars produced in the scenario |
| Units_Sold | Synthetic number of cars sold in the scenario |
| Avg_Selling_Price_INR | Synthetic average selling price per car, INR |
| Revenue_INR | Units sold × synthetic average selling price |
| Raw_Material_Cost_INR | Synthetic raw material cost |
| Labour_Cost_INR | Synthetic labour cost |
| Manufacturing_Overhead_INR | Synthetic overhead cost |
| Total_Manufacturing_Cost_INR | Sum of raw material, labour, and overhead costs |
| Operating_Profit_INR | Revenue minus total manufacturing cost (simplified project definition) |
| Budget_Revenue_INR | Synthetic budgeted revenue benchmark |
| Budget_Cost_INR | Synthetic budgeted cost benchmark |

### Important interpretation notes
- This is not an official dataset from any automaker or government source.
- It is a simplified financial model, not audited accounting data; taxes, interest, warranty provisions, inventory accounting, and full cost allocation are not included.
- Budget values are synthetic planning benchmarks and may be higher or lower than actuals.
- Revenue variance = Revenue_INR - Budget_Revenue_INR.
- Cost variance = Total_Manufacturing_Cost_INR - Budget_Cost_INR. Positive cost variance means scenario cost is above budget.
- Profit margin (%) = Operating_Profit_INR / Revenue_INR × 100.
