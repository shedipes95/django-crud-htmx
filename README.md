# Django CRUD + HTMX (ERP-style demo)

Minimal server-rendered app using **Django**, **Bootstrap**, and **HTMX**.  
It showcases a classic back-office flow: **Products** CRUD, a quick **Order** form that decrements stock, and **live search** by name/SKU.

## Why this demo (fit for Herbst)
I like pragmatic, ERP-style internal tools: simple server-rendered forms, clear validations, and only as much interactivity as needed. **HTMX** adds small, targeted updates (like live search) without SPA complexity. This aligns with modules around stock, sales, purchasing, and reporting. I’m keen to deepen my **SQL/ORM** skills while building clean CRUD flows that save users time.

## Tech stack
- Django 4.x (server-rendered)
- Bootstrap 5 (UI)
- HTMX 1.9 (partial page updates)
- SQLite (dev)

## Features
- Product CRUD (name, SKU, price, stock)
- Order creation (updates product stock)
- **Live search** (HTMX) in the product list
- Admin site for quick inspection

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
# (optional) create an admin user
python manage.py createsuperuser

python manage.py runserver

<video src="demo.mp4" controls width="720"></video>
