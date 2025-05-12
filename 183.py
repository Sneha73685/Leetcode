import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customer_list = orders["customerId"].unique().tolist()
    customers = customers[~customers["id"].isin(customer_list)]
    customers = customers.rename(columns={"name": "Customers"})
    return customers[["Customers"]]