CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(100) UNIQUE,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    product_name VARCHAR(100),
    sku VARCHAR(100) UNIQUE,
    category VARCHAR(100),
    price INTEGER,
    stock_quantity INTEGER
);

CREATE TABLE suppliers (
    id INTEGER PRIMARY KEY,
    supplier_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(50)
);