# 🇵🇰 BazaarPK — Full-Stack E-Commerce Store

> A modern, Pakistan-focused full-stack e-commerce platform built with Django, Python, HTML, CSS, and JavaScript.

BazaarPK is a complete e-commerce web application designed around the shopping experience of customers in Pakistan.

The project includes product browsing, search and filtering, shopping cart functionality, checkout, user authentication, order management, PKR pricing, Cash on Delivery, and a Django admin dashboard.

---

## 🚀 Project Overview

BazaarPK was developed as a full-stack e-commerce project to demonstrate how a real-world online store can be designed and developed from frontend to backend.

The application combines:

- 🎨 Modern responsive frontend
- ⚙️ Django backend
- 🗄️ Database-driven products and orders
- 🛒 Shopping cart
- 👤 User authentication
- 📦 Order processing
- 💳 Pakistan-focused payment method selection
- 🛠️ Django administration
- 📱 Mobile-friendly interface

The goal was not just to create a visual storefront, but to build a functional foundation for a real e-commerce platform.

---

# ✨ Features

## 🛍️ Product Catalog

- Product listing
- Product categories
- Product detail pages
- Product pricing in PKR
- Stock availability
- Product search
- Filtering
- Sorting
- Product descriptions

## 🛒 Shopping Cart

Customers can:

- Add products to cart
- Increase/decrease quantity
- Remove products
- View subtotal
- View total quantity
- Continue shopping
- Proceed to checkout

## 👤 Authentication

Includes:

- User registration
- User login
- User logout
- Customer account
- Order history

## 📦 Checkout & Orders

Customers can provide:

- Full name
- Phone number
- Email
- Address
- City
- Postal code
- Payment method

Supported payment method selections include:

- 💵 Cash on Delivery
- 📱 Easypaisa
- 📱 JazzCash

> Note: Easypaisa and JazzCash are currently payment-method placeholders. A real production payment gateway/API must be integrated before accepting online payments.

## 🏙️ Pakistan-Focused Experience

The application is designed specifically with Pakistani e-commerce requirements in mind.

Examples include:

- 🇵🇰 PKR currency
- Pakistani cities and addresses
- Cash on Delivery
- Easypaisa
- JazzCash
- Pakistani-style contact information
- Localized checkout experience

## 🛠️ Admin Dashboard

Django Admin can be used to manage:

- Products
- Categories
- Customers
- Orders
- Stock
- Order status

---

# 🧑‍💻 Tech Stack

### Frontend

- HTML5
- CSS3
- Vanilla JavaScript
- Responsive Web Design

### Backend

- Python
- Django

### Database

- SQLite for local development
- PostgreSQL recommended for production

### Development Tools

- Git
- GitHub
- Django Admin
- Python Virtual Environment

---

# 🏗️ Project Architecture

```text
BazaarPK
│
├── manage.py
│
├── pakistanshop/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── shop/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   ├── urls.py
│   │
│   ├── migrations/
│   │
│   ├── management/
│   │   └── commands/
│   │       └── seed_store.py
│   │
│   ├── templates/
│   │   └── shop/
│   │
│   └── static/
│       └── shop/
│           ├── css/
│           └── js/
│
├── templates/
│   └── registration/
│
├── requirements.txt
└── README.md
