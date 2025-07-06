
CREATE TABLE Employee (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    role VARCHAR(50),
    hire_date DATE,
    salary DECIMAL(10, 2),
    is_active BOOLEAN DEFAULT TRUE
);


CREATE TABLE Customer (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    registered_on DATE DEFAULT CURRENT_DATE,
    total_visits INT DEFAULT 0,
    total_spent DECIMAL(10, 2) DEFAULT 0.0
);


CREATE TABLE Category (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE,
    aisle_number INT,
    description TEXT
);


CREATE TABLE Supplier (
    supplier_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    email VARCHAR(100),
    address TEXT,
    gst_number VARCHAR(20),
    active BOOLEAN DEFAULT TRUE,
    created_on DATE DEFAULT CURRENT_DATE
);


CREATE TABLE Coupon (
    code VARCHAR(20) PRIMARY KEY,
    discount_percent INT,
    valid_from DATE,
    valid_until DATE,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE Items (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    category_id INT REFERENCES Category(category_id),
    supplier_id INT REFERENCES Supplier(supplier_id),
    price DECIMAL(10, 2),
    stock INT,
    is_returnable BOOLEAN DEFAULT FALSE,
    is_available BOOLEAN DEFAULT TRUE
);


CREATE TABLE Supplier_Billing (
    supply_id SERIAL PRIMARY KEY,
    supplier_id INT REFERENCES Supplier(supplier_id),
    item_id INT REFERENCES Items(item_id),
    quantity_supplied INT,
    supply_price DECIMAL(10, 2),
    supply_date DATE DEFAULT CURRENT_DATE
);


CREATE TABLE Billing (
    bill_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES Customer(customer_id),
    employee_id INT REFERENCES Employee(employee_id),
    bill_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2),
    discount_amount DECIMAL(10, 2) DEFAULT 0.0,
    coupon_code VARCHAR(20),
    FOREIGN KEY (coupon_code) REFERENCES Coupon(code)
);


CREATE TABLE Bill_Item (
    bill_item_id SERIAL PRIMARY KEY,
    bill_id INT REFERENCES Billing(bill_id) ON DELETE CASCADE,
    item_id INT REFERENCES Items(item_id),
    quantity INT,
    unit_price DECIMAL(10, 2),
    total_price DECIMAL(10, 2)
);


CREATE TABLE Return_Items (
    return_id SERIAL PRIMARY KEY,
    bill_item_id INT REFERENCES Bill_Item(bill_item_id),
    return_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    reason TEXT,
    quantity INT,
    refund_amount DECIMAL(10, 2),
    approved_by INT REFERENCES Employee(employee_id)
);
