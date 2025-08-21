# 📌 Smart Inventory & Order Management System

A **Python-based** application to help small businesses **track inventory**, **manage customer orders**, and **generate reports**.

<p align="left">
  <a href="https://www.python.org/downloads/"><img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue.svg"></a>
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green.svg">
  <img alt="Status" src="https://img.shields.io/badge/Status-Active-success">
</p>

---

## ✨ Features

### 🛒 Product Management
- Add / update / delete products  
- Track stock levels, categories, and prices

### 👥 Customer Management
- Store customer details (name, contact, order history)
- Support different customer types (**Retail**, **Wholesale**) via **inheritance**

### 📦 Order Processing
- Create orders and automatically reduce stock
- Apply discounts by customer type

### 📊 Reporting
- Low-stock alerts
- Monthly sales summaries
- Best-selling products

### 💾 Data Storage
- Persist data to **CSV** (ready to upgrade to **SQLite**)

---

## 🧱 OOP Design (Core Classes)

- `Product` — SKU, name, category, price, stock
- `Inventory` — manages products, stock operations, low-stock detection
- `Customer` (base), `RetailCustomer`, `WholesaleCustomer`
- `Order` & `OrderItem` — pricing, totals, discounts
- `ReportGenerator` — sales, top products, low-stock
- `BalanceSheet` — optional: record revenue/COGS summaries

---


