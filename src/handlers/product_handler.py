from src.utils import read_csv_products
import csv

CSV_FILE = "data/products.csv" 

# 1. GET-"Dammi le informazioni", Si usa per leggere i dati
def get_all_products_handler():
    return read_csv_products()

# 2. POST-"Crea qualcosa di nuovo". Si usa per inviare dati al server e modificare qualcosa 
def create_product_handler(data):
    for field in ["id", "name", "quantity"]:
        if field not in data:
            return {"Error": f"Parametro {field} mancante"}, 400
            
    products = read_csv_products()
    for p in products:
        if p["id"] == int(data["id"]):
            return {"Error": "Un prodotto con questo ID esiste già"}, 400
            
    nuovo_gioco = {
        "id": int(data["id"]),
        "name": data["name"],
        "quantity": int(data["quantity"])
    }
    products.append(nuovo_gioco)
    
    #sorted che si usa per ordinare in modo crescente 
    products = sorted(products, key=lambda x: int(x["id"]))
    
    with open(CSV_FILE, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "quantity"])
        writer.writeheader()
        writer.writerows(products)
    return {"Message": "Gioco aggiunto con successo!", "Product": nuovo_gioco}, 201

# 3. PUT-"Aggiorna questo dato". Si usa per modificare informazioni già esistenti
def update_product_handler(product_id, data):
    if "quantity" not in data:
        return {"Error": "Parametro quantity mancante"}, 400
        
    products = read_csv_products()
    trovato = False
    for p in products:
        if p["id"] == product_id:
            p["quantity"] = int(data["quantity"])
            trovato = True
            break
            
    if not trovato:
        return {"Error": "Gioco non trovato"}, 404
        
    #sorted per ordinare 
    products = sorted(products, key=lambda x: int(x["id"]))
        
    with open(CSV_FILE, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "quantity"])
        writer.writeheader()
        writer.writerows(products)
    return {"Message": "Quantità aggiornata con successo!"}, 200

# 4. DELETE-"Cancella questo dato". Rimuove un elemento che decidiamo dal server.
def delete_product_handler(product_id):
    products = read_csv_products()
    nuovi_prodotti = [p for p in products if p["id"] != product_id]
    
    if len(products) == len(nuovi_prodotti):
        return {"Error": "Gioco non trovato"}, 404
        
    #sorted per ordinare
    nuovi_prodotti = sorted(nuovi_prodotti, key=lambda x: int(x["id"]))
        
    with open(CSV_FILE, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "quantity"])
        writer.writeheader()
        writer.writerows(nuovi_prodotti)
    return {"Message": "Gioco eliminato!"}, 200 