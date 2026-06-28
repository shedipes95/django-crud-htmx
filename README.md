# Django CRUD + HTMX

A small, server-rendered Django app for managing products and orders. It uses Bootstrap for the UI and HTMX for live search, so the page updates without a full reload and without any front-end framework.

## What it does

- **Products** — create, edit, and delete products (name, SKU, price, stock).
- **Orders** — place a quick order against a product. The form checks there's enough stock and then decrements it on save.
- **Live search** — filter the product list by name or SKU as you type, powered by HTMX returning just the table rows.
- **Admin** — both models are registered in the Django admin for quick inspection.

## Why I built it

I wanted to practise the kind of back-office tooling a lot of internal business apps are made of: plain server-rendered forms, sensible validation, and a real database relationship (orders that draw down stock). HTMX adds the small bits of interactivity that actually help — like live search — without reaching for a single-page-app setup. It's also a clean place to keep working on my SQL and Django ORM.

## Tech stack

- **Django 4.2+** — views, forms, ORM, admin
- **Bootstrap 5.3** — UI (loaded via CDN)
- **HTMX 1.9** — partial page updates (loaded via CDN)
- **SQLite** — local development database

## Project layout

- `herbst_demo/` — project settings and URL config
- `inventory/` — the app: `models.py`, `views.py`, `forms.py`, `urls.py`, `admin.py`, and templates
- `inventory/templates/inventory/partials/` — the HTMX snippets (search rows, order confirmation)

## Run it

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser   # optional, for the admin site
python manage.py runserver
```

Then open http://127.0.0.1:8000/ for the product list, or http://127.0.0.1:8000/admin/ for the admin.

## Demo

A short screen recording is included in the repo: [`demo.mp4`](demo.mp4).
