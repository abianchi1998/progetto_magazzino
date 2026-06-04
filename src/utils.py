import csv

CSV_FILE = "data/products.csv"

def read_csv_products():
    products = []
    try:
        with open(CSV_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["id"] = int(row["id"])
                row["quantity"] = int(row["quantity"])
                products.append(row)
    except FileNotFoundError:
        return []
    return products