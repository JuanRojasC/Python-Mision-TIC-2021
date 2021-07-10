# VARIABLES
storeInventory = [{"code": 1, "name": "Manzanas", "price": 8000.0, "stock": 550},
                  {"code": 2, "name": "Limones", "price": 2300.0, "stock": 15},
                  {"code": 3, "name": "Peras", "price": 2500.0, "stock": 38},
                  {"code": 4, "name": "Arandanos", "price": 9300.0, "stock": 55},
                  {"code": 5, "name": "Tomates", "price": 2100.0, "stock": 42},
                  {"code": 6, "name": "Fresas", "price": 4100.0, "stock": 33},
                  {"code": 7, "name": "Helado", "price": 4500.0, "stock": 41},
                  {"code": 8, "name": "Galletas", "price": 500.0, "stock": 833},
                  {"code": 9, "name": "Chocolates", "price": 3500.0, "stock": 806},
                  {"code": 10, "name": "Jamon", "price": 17000.0, "stock": 10}]
function = input()
code, name, price, stock = input().split(" ")


# FUNCTIONS
# VERIFY THE INDEX OF THE ELEMENT NONE IF DOESN'T EXIST
def existProduct(nameProduct):
    global storeInventory
    if type(nameProduct) == str:
        return next((index for (index, d) in enumerate(storeInventory) if d["name"] == nameProduct), False)
    return next((index for (index, d) in enumerate(storeInventory) if d["price"] == nameProduct), False)

# MODIFY THE DATA OF A PRODUCT
def modifyProduct(function,code, name, price, stock):
    global storeInventory
    if not existProduct(name) and function == "AGREGAR":
        storeInventory.append({"code": int(code), "name": name, "price": float(price), "stock": int(stock)})
        return True
    if existProduct(name) and function == "ACTUALIZAR":
        storeInventory[existProduct(name)]={"code": int(code), "name": name, "price": int(price), "stock": int(stock)}
        return True
    elif existProduct(name) and function == "BORRAR":
        storeInventory.pop(existProduct(name))
        return True
    return False

# PRINT INFORMATION
def printOutput(function,code,name,price,stock):
    global storeInventory
    if not modifyProduct(function,code,name,price,stock):
        return "ERROR"
    cheapProductName = storeInventory[existProduct(min(product["price"] for product in storeInventory))]["name"]
    expensiveProductName = storeInventory[existProduct(max(product["price"] for product in storeInventory))]["name"]
    priceAverage = round(sum(product["price"] for product in storeInventory) / len(storeInventory),1)
    inventoryValue = round(sum(product["price"]*product["stock"] for product in storeInventory),1)
    return f"{expensiveProductName} {cheapProductName} {priceAverage} {inventoryValue}"
    
    
# EXECUTION
print(printOutput(function,code,name,price,stock))