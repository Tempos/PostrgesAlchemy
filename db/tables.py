from sqlalchemy import Column, ForeignKey, MetaData, CHAR, DATE, SMALLINT, INT, REAL, LargeBinary, VARCHAR, TEXT
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()
# metadata = MetaData()


class Categories(base):
    __tablename__ = 'categories'

    category_id = Column(SMALLINT, primary_key=True, unique=True)
    category_name = Column(VARCHAR(15))
    description = Column(TEXT)
    picture = Column(LargeBinary)


class CustomerCustomerDemo(base):
    __tablename__ = 'customer_customer_demo'

    customer_id = Column(CHAR, ForeignKey('customers.customer_id'), primary_key=True)
    customer_type_id = Column(CHAR, ForeignKey('customer_demographics.customer_type_id'), primary_key=True, unique=True)


class CustomerDemographics(base):
    __tablename__ = 'customer_demographics'

    customer_type_id = Column(CHAR, primary_key=True)
    customer_desc = Column(TEXT, unique=True)


class Customers(base):
    __tablename__ = 'customers'

    customer_id = Column(CHAR, primary_key=True, unique=True)
    company_name = Column(VARCHAR(40))
    contact_name = Column(VARCHAR(30))
    contact_title = Column(VARCHAR(30))
    address = Column(VARCHAR(60))
    city = Column(VARCHAR(15))
    region = Column(VARCHAR(15))
    postal_code = Column(VARCHAR(10))
    country = Column(VARCHAR(15))
    phone = Column(VARCHAR(24))
    fax = Column(VARCHAR(24))


class EmployeeTerritories(base):
    __tablename__ = 'employee_territories'

    employee_id = Column(SMALLINT, ForeignKey('employees.employee_id'), primary_key=True, unique=True)
    territory_id = Column(VARCHAR(20), ForeignKey('territories.territory_id'))


class Employees(base):
    __tablename__ = 'employees'

    employee_id = Column(SMALLINT, primary_key=True, unique=True)
    last_name = Column(VARCHAR(20))
    first_name = Column(VARCHAR(10))
    title = Column(VARCHAR(30))
    title_of_courtesy = Column(VARCHAR(25))
    birth_date = Column(DATE)
    hire_date = Column(DATE)
    address = Column(VARCHAR(60))
    city = Column(VARCHAR(15))
    region = Column(VARCHAR(15))
    postal_code = Column(VARCHAR(10))
    country = Column(VARCHAR(15))
    home_phone = Column(VARCHAR(24))
    extension = Column(VARCHAR(4))
    photo = Column(LargeBinary)
    notes = Column(TEXT)
    reports_to = Column(SMALLINT, ForeignKey('employees.employee_id'))
    photo_path = Column(VARCHAR(255))


class OrderDetails(base):
    __tablename__ = 'order_details'

    order_id = Column(SMALLINT, ForeignKey('orders.order_id'), primary_key=True, unique=True)
    product_id = Column(SMALLINT, ForeignKey('products.product_id'), primary_key=True, unique=True)
    unit_price = Column(REAL)
    quantity = Column(SMALLINT)
    discount = Column(REAL)


class Orders(base):
    __tablename__ = 'orders'

    order_id = Column(SMALLINT, primary_key=True, unique=True)
    customer_id = Column(CHAR, ForeignKey('customers.customer_id'))
    employee_id = Column(SMALLINT, ForeignKey('employees.employee_id'))
    order_date = Column(DATE)
    required_date = Column(DATE)
    shipped_date = Column(DATE)
    ship_via = Column(SMALLINT, ForeignKey('shippers.shipper_id'))
    freight = Column(REAL)
    ship_name = Column(VARCHAR(40))
    ship_address = Column(VARCHAR(60))
    ship_city = Column(VARCHAR(15))
    ship_region = Column(VARCHAR(15))
    ship_postal_code = Column(VARCHAR(10))
    ship_country = Column(VARCHAR(15))


class Products(base):
    __tablename__ = 'products'

    product_id = Column(SMALLINT, nullable=False, primary_key=True)
    product_name = Column(VARCHAR(40))
    supplier_id = Column(SMALLINT, ForeignKey('products.supplier_id'))
    category_id = Column(SMALLINT, ForeignKey('products.category_id'))
    quantity_per_unit = Column(VARCHAR(20))
    unit_price = Column(REAL)
    units_in_stock = Column(SMALLINT)
    units_on_order = Column(SMALLINT)
    reorder_level = Column(SMALLINT)
    discontinued = Column(INT, nullable=False)


class Region(base):
    __tablename__ = 'region'

    region_id = Column(SMALLINT, primary_key=True, unique=True)
    region_description = Column(CHAR)


class Shippers(base):
    __tablename__ = 'shippers'

    shipper_id = Column(SMALLINT, primary_key=True, unique=True)
    company_name = Column(VARCHAR(40))
    phone = Column(VARCHAR(24))


class Suppliers(base):
    __tablename__ = 'suppliers'

    supplier_id = Column(SMALLINT, primary_key=True, unique=True)
    company_name = Column(VARCHAR(40))
    contact_name = Column(VARCHAR(30))
    contact_title = Column(VARCHAR(30))
    address = Column(VARCHAR(60))
    city = Column(VARCHAR(15))
    region = Column(VARCHAR(15))
    postal_code = Column(VARCHAR(10))
    country = Column(VARCHAR(15))
    phone = Column(VARCHAR(24))
    fax = Column(VARCHAR(24))
    homepage = Column(TEXT)


class Territories(base):
    __tablename__ = 'territories'

    territory_id = Column(VARCHAR(20), primary_key=True, unique=True)
    territory_description = Column(CHAR)
    region_id = Column(SMALLINT, ForeignKey('region.region_id'))


class USStates(base):
    __tablename__ = 'us_states'

    state_id = Column(SMALLINT, primary_key=True, unique=True)
    state_name = Column(VARCHAR(100))
    state_abbr = Column(VARCHAR(2))
    state_region = Column(VARCHAR(50))
