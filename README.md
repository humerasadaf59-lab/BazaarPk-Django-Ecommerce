# BazaarPK — Full-Stack Pakistani E-commerce Store

A polished Django e-commerce starter built around Pakistani shopping habits: PKR pricing, Cash on Delivery, Easypaisa/JazzCash-ready payment selection, local city/address fields, account registration/login, product catalog, search/filtering, cart, checkout and order history.

## Stack
- Django + SQLite (easy local development)
- HTML5 templates
- CSS3 responsive design
- Vanilla JavaScript for cart quantity controls, mobile navigation, filters and UI polish
- Django Admin for products, categories and orders

## Run locally
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py seed_store
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.
Admin: `http://127.0.0.1:8000/admin/`

## Production checklist
1. Move `SECRET_KEY` to environment variables.
2. Set `DEBUG=False` and configure `ALLOWED_HOSTS`.
3. Use PostgreSQL for production.
4. Configure cloud media storage (S3/Cloudinary/etc.).
5. Connect a real payment provider before accepting online payments. The included Easypaisa/JazzCash options are intentionally order-method placeholders, not a live payment gateway.
6. Add email/SMS/WhatsApp order notifications.
7. Run `collectstatic` and deploy behind HTTPS.
