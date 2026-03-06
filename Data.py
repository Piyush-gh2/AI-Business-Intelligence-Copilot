import pandas as pd

def load_data(file):
    data = pd.read_csv(file)
    return data

def analyze_sales(data):
    total_revenue = data["Revenue"].sum()
    best_region = data.groupby("Region")["Revenue"].sum().idxmax()
    best_product = data.groupby("Product")["Revenue"].sum().idxmax()

    return {
        "Total Revenue": total_revenue,
        "Best Region": best_region,
        "Best Product": best_product
    }