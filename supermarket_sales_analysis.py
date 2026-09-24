"""
Supermarket Sales Analysis
AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026

Dataset columns:
Invoice ID, Date, Branch, City, Customer Type, Gender, Product,
Category, Quantity, Unit Price, Payment, Rating, Sales

How to use:
1. Keep the dataset file in the same folder as this Python file.
2. If your dataset is CSV, name it: supermarket_sales.csv
3. Run: python supermarket_sales_analysis.py

If the provided dataset is PDF, first convert/copy it to CSV.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


DATA_FILE = Path("supermarket_sales.csv")
OUTPUT_DIR = Path("analysis_output")
OUTPUT_DIR.mkdir(exist_ok=True)


def load_data():
    """Load the supermarket dataset."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}\n"
            "Put supermarket_sales.csv in the same folder as this script."
        )

    df = pd.read_csv(DATA_FILE)
    return df


def clean_data(df):
    """Basic data cleaning and preparation."""
    df = df.copy()

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Convert numeric columns to numbers
    numeric_cols = ["Quantity", "Unit Price", "Rating", "Sales"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Convert date
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Calculate Sales from Quantity × Unit Price
    if {"Quantity", "Unit Price"}.issubset(df.columns):
        df["Calculated Sales"] = (
            df["Quantity"] * df["Unit Price"]
        ).round(2)

    # Remove completely empty rows
    df = df.dropna(how="all")

    return df


def print_basic_information(df):
    print("\n" + "=" * 60)
    print("SUPERMARKET SALES ANALYSIS")
    print("=" * 60)

    print(f"\nTotal transactions: {len(df)}")

    print("\nMissing values:")
    print(df.isnull().sum())

    if "Sales" in df.columns:
        print(f"\nTotal Sales: ₹{df['Sales'].sum():,.2f}")
        print(f"Average Transaction: ₹{df['Sales'].mean():,.2f}")

    if "Rating" in df.columns:
        print(f"Average Rating: {df['Rating'].mean():.2f}/5")


def analyze_products(df):
    if "Product" not in df.columns or "Sales" not in df.columns:
        return None

    result = (
        df.groupby("Product")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n--- Sales by Product ---")
    print(result)

    print(f"\nHighest-sales product: {result.idxmax()}")
    print(f"Sales: ₹{result.max():,.2f}")

    return result


def analyze_branches(df):
    if "Branch" not in df.columns or "Sales" not in df.columns:
        return None

    result = (
        df.groupby(["Branch", "City"])["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n--- Sales by Branch ---")
    print(result)

    best = result.index[0]
    print(f"\nHighest-sales branch: Branch {best[0]} ({best[1]})")
    print(f"Sales: ₹{result.iloc[0]:,.2f}")

    return result


def analyze_categories(df):
    if "Category" not in df.columns or "Sales" not in df.columns:
        return None

    result = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n--- Sales by Category ---")
    print(result)

    print(f"\nHighest-sales category: {result.idxmax()}")
    print(f"Sales: ₹{result.max():,.2f}")

    return result


def analyze_payments(df):
    if "Payment" not in df.columns:
        return None

    result = df["Payment"].value_counts()

    print("\n--- Payment Methods ---")
    print(result)

    print(f"\nMost used payment method: {result.idxmax()}")
    print(f"Transactions: {result.max()}")

    return result


def analyze_customer_type(df):
    if "Customer Type" not in df.columns or "Sales" not in df.columns:
        return None

    result = df.groupby("Customer Type")["Sales"].mean()

    print("\n--- Average Transaction by Customer Type ---")
    print(result)

    return result


def create_charts(df, products, branches, categories, payments):
    """Create charts for the project report/presentation."""

    # Product sales
    if products is not None:
        plt.figure(figsize=(10, 6))
        products.plot(kind="bar")
        plt.title("Sales by Product")
        plt.xlabel("Product")
        plt.ylabel("Sales (₹)")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "sales_by_product.png", dpi=300)
        plt.close()

    # Branch sales
    if branches is not None:
        branch_labels = [
            f"{branch} ({city})"
            for branch, city in branches.index
        ]

        plt.figure(figsize=(8, 5))
        plt.bar(branch_labels, branches.values)
        plt.title("Sales by Branch")
        plt.xlabel("Branch")
        plt.ylabel("Sales (₹)")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "sales_by_branch.png", dpi=300)
        plt.close()

    # Category sales
    if categories is not None:
        plt.figure(figsize=(9, 5))
        categories.plot(kind="bar")
        plt.title("Sales by Category")
        plt.xlabel("Category")
        plt.ylabel("Sales (₹)")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "sales_by_category.png", dpi=300)
        plt.close()

    # Payment method
    if payments is not None:
        plt.figure(figsize=(8, 5))
        payments.plot(kind="bar")
        plt.title("Payment Method Usage")
        plt.xlabel("Payment Method")
        plt.ylabel("Number of Transactions")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "payment_methods.png", dpi=300)
        plt.close()

    print(f"\nCharts saved in: {OUTPUT_DIR.resolve()}")


def save_summary(df, products, branches, categories, payments):
    """Save important analysis results into a text file."""
    with open(OUTPUT_DIR / "analysis_summary.txt", "w", encoding="utf-8") as file:
        file.write("SUPERMARKET SALES ANALYSIS\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Total Transactions: {len(df)}\n")

        if "Sales" in df.columns:
            file.write(f"Total Sales: ₹{df['Sales'].sum():,.2f}\n")
            file.write(
                f"Average Transaction: ₹{df['Sales'].mean():,.2f}\n"
            )

        if "Rating" in df.columns:
            file.write(
                f"Average Rating: {df['Rating'].mean():.2f}/5\n"
            )

        if products is not None:
            file.write(
                f"\nHighest Sales Product: {products.idxmax()}"
                f" - ₹{products.max():,.2f}\n"
            )

        if branches is not None:
            branch, city = branches.index[0]
            file.write(
                f"Best Branch: {branch} ({city})"
                f" - ₹{branches.iloc[0]:,.2f}\n"
            )

        if categories is not None:
            file.write(
                f"Highest Sales Category: {categories.idxmax()}"
                f" - ₹{categories.max():,.2f}\n"
            )

        if payments is not None:
            file.write(
                f"Most Used Payment: {payments.idxmax()}"
                f" - {payments.max()} transactions\n"
            )


def main():
    df = load_data()
    df = clean_data(df)

    print_basic_information(df)

    products = analyze_products(df)
    branches = analyze_branches(df)
    categories = analyze_categories(df)
    payments = analyze_payments(df)
    analyze_customer_type(df)

    create_charts(df, products, branches, categories, payments)
    save_summary(df, products, branches, categories, payments)

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
