from data.secret import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.tables import (
    base,
    Categories, CustomerCustomerDemo, CustomerDemographics, Customers, EmployeeTerritories, Employees,
    OrderDetails, Orders, Products, Region, Shippers, Suppliers, Territories, USStates)

db_string = f"postgresql://{LOGIN}:{PASSWORD}@localhost:5432/northwind"
db = create_engine(db_string)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# Create
# mozzarella = Product(product_name="Mozzarella di Giovanni", quantity_per_unit='24 - 200 g pkgs.', unit_price=35.5,
#                      units_in_stock=14, discontinued=0)
# session.add(mozzarella)
# session.commit()

# Read
for product in session.query(Products):
    print(product.product_name)

# Update
# mozzarella.product_name = "Mozzarella"
# session.commit()

# Delete
# session.delete(mozzarella)
# session.commit()
