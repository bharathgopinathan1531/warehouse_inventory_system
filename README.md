:::writing{variant="document" id="84571"}
Warehouse Inventory Management System
A FastAPI-based backend application for managing warehouse inventory, products, suppliers, and stock movements with JWT Authentication, Role-Based Access Control, Pagination, Category Filtering, Docker Support, and Pytest Testing.
🚀 Tech Stack
Python 3.9+
FastAPI
SQLAlchemy
Pydantic
SQLite
JWT Authentication
Uvicorn
Docker
Pytest
✨ Features
Authentication
User Registration (POST /auth/register)
User Login (POST /auth/login)
JWT Token Authentication
Password Hashing
Protected Routes
Role-Based Access (Admin, Staff)
Product Management
Create Product
View All Products
View Product by ID
Update Product
Delete Product
Product Fields:
product_name
sku (unique)
category
price
stock_quantity
Supplier Management
Create Supplier
View Suppliers
Update Supplier
Delete Supplier
Supplier Fields:
supplier_name
email
phone
Stock Management
Add Stock (POST /stock/inward)
Remove Stock (POST /stock/outward)
View Stock History (GET /stock/history)
View Current Stock (GET /stock)
Low Stock Alert (GET /stock/low)
✅ Business Rules
SKU must be unique
Product must exist before stock update
Stock cannot become negative
Every stock movement is tracked
Protected APIs require authentication
✅ Validations
Valid email validation
Positive price validation
Positive quantity validation
Duplicate username validation
Duplicate email validation
Duplicate SKU validation
Proper HTTPException handling
⭐ Bonus Features
Low Stock Alerts
Returns products with low inventory levels.
Endpoint:
Http
GET /stock/low
Pagination
Supports paginated product listing.
Example:
Http
GET /products?skip=0&limit=10
Category Filtering
Filter products by category.
Example:
Http
GET /products/category/Electronics
Docker Support
Containerized deployment using Docker.
Build Image:
Bash
docker build -t warehouse-api .
Run Container:
Bash
docker run -p 8000:8000 warehouse-api
Pytest Testing
Run tests using:
Bash
pytest
Result:
Plain text
1 passed
Swagger Enhancements
Custom API Title
API Description
API Version
Organized Tags
Interactive Documentation
Swagger UI:
Plain text
http://127.0.0.1:8000/docs
📂 Project Structure
Plain text
warehouse_inventory_system/
│
├── app/
│   ├── routers/
│   │   ├── auth.py
│   │   ├── products.py
│   │   ├── suppliers.py
│   │   └── stock.py
│   │
│   ├── database.py
│   ├── dependencies.py
│   ├── models.py
│   ├── schemas.py
│   ├── security.py
│   └── main.py
│
├── tests/
│   └── test_main.py
│
├── screenshots/
│
├── sql/
│   └── schema.sql
│
├── Dockerfile
├── requirements.txt
├── README.md
└── warehouse.db
▶️ Installation & Setup
Create Virtual Environment
Bash
python -m venv venv
Activate Virtual Environment
Windows:
Bash
venv\Scripts\activate
Install Dependencies
Bash
pip install -r requirements.txt
Run Application
Bash
uvicorn app.main:app --reload
📖 API Documentation
Swagger UI:
Plain text
http://127.0.0.1:8000/docs
ReDoc:
Plain text
http://127.0.0.1:8000/redoc
📸 Screenshots Included
JWT Authentication API
Product APIs
Supplier APIs
Stock APIs
Swagger Documentation
Complete API List
Pytest Result
👨‍💻 Author
Bharath G
Warehouse Inventory Management System developed using FastAPI, SQLAlchemy, JWT Authentication, Docker, and Pytest. :::
Copy this entire content into your README.md file and commit it to GitHub. This is professional and covers all mandatory and bonus requirements. 🚀