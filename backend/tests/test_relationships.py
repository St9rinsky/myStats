
import pandas as pd

from app.services.relations import discover_relations


customers = pd.DataFrame({
    "customerID": ["1", "2", "3"],
    "Name": ["Sello", "Letswalo", "Starinsky"]
})

orders = pd.DataFrame({
    "orderID": ["1", "2", "3", "4"],
    "customerID": ["1", "1", "2", "3"],
    "Amount": [500, 250, 300, 700]
})


relationships = discover_relations(customers,orders,"Customers","Orders")
print(relationships)
