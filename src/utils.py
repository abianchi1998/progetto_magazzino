#serve a contenere tutte quelle funzioni di servizio che fanno un lavoro generico e ripetitivo
# e che possono essere riutilizzate in più parti del progetto.

import csv

CSV_FILE = "data/products.csv"

def read_csv_products():
    products = [] #creiamo una lista, come se fosse il contenitore dei giochi 
    try: #serve per non mandare in crash il server 
        with open(CSV_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file) #trasforma la lista in un dizionario 
            for row in reader:
                row["id"] = int(row["id"])
                row["quantity"] = int(row["quantity"])
                products.append(row)
    except FileNotFoundError:
        return [] #se c'è qualche errore, restituisce la lista vuota 
    return products