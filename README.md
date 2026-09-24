# Supermarket Sales Analysis

AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026

## Project Overview
This project analyzes supermarket sales transactions to identify useful business insights about products, branches, categories, customers, payment methods, and ratings.

## Dataset
- Records: 500
- Columns: 13
- Source file supplied for the internship project: SUPER MARKET DATA (1).pdf
- Converted CSV: `supermarket_sales.csv`

## Technologies
- Python
- Pandas
- Matplotlib

## How to Run

1. Install Python 3.9+.
2. Open a terminal in this project folder.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run:

```bash
python supermarket_sales_analysis.py
```

The script creates an `analysis_output` folder containing charts and an analysis summary.

## Main Analysis
The script:
- checks missing values
- converts numeric/date fields
- calculates `Quantity × Unit Price` as a validation field
- analyzes sales by product, branch and category
- analyzes payment-method usage
- compares average transaction value by customer type
- calculates average customer rating
- generates charts

## Key Results from the supplied dataset
- Total sales: ₹244,411.08
- Average transaction: ₹488.82
- Highest-sales product: Cheese — ₹27,906.30
- Highest-sales branch: Branch C (Mumbai) — ₹72,469.45
- Highest-sales category: Beverages — ₹56,108.24
- Most-used payment method: UPI — 127 transactions
- Average customer rating: 3.99/5

## Files
- `supermarket_sales_analysis.py` — analysis code
- `supermarket_sales.csv` — cleaned CSV dataset
- `requirements.txt` — Python dependencies
- `README.md` — project instructions
- `Project_Report.pdf` — project report

## Disclaimer
The analysis is based on the dataset supplied for the internship project. Business recommendations are derived from the observed transaction patterns.
