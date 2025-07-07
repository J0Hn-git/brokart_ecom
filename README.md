🛍️ Brokart – E-Commerce Web App

Brokart is a modern, feature-rich eCommerce application built with Django (and optionally React/HTML for frontend).
It allows customers to browse products, manage their cart, place secure orders, and much more. It's perfect for showcasing online store capabilities with a customizable admin panel.

🚀 Features

- 🛒 Product catalog with images, categories & details
- 👥 User registration, login, and profile management
- 🧺 Add to cart and quantity management
- 💳 Checkout and order placement
- 📦 Order history & tracking
- 🧑‍💼 Admin panel for managing users, products, and orders
- 🔐 Secure authentication and authorization

- 🧱 Tech Stack

| Layer        | Technology                  |
|--------------|-----------------------------|
| Frontend     | HTML, CSS, Bootstrap / React (optional) |
| Backend      | Django (Python)             |
| Database     | PostgreSQL / SQLite         |
| Deployment   | GitHub, Render / Heroku / Vercel |
| Others       | Django Admin, Django REST Framework (optional)

Setup Database & Run Server
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
