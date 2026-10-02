# ☕ Café Django — Full-Stack Café Website

A modern, responsive café website built with **Django** and designed with a premium, warm editorial-style café aesthetic.

The project includes menu browsing, cart/order functionality, user authentication, contact and about pages, Django Admin, responsive layouts, static assets, and production deployment support.

## 🌐 Live Demo

🚀 **Live Website:** https://cafe-django-ixvb.onrender.com/

## ✨ Features

### 👤 User Authentication
- User registration
- User login/logout
- Protected user functionality
- Authentication-ready order workflow

### 🍽️ Menu
- Browse café menu items
- Item details
- Category-based organization
- Add items to cart
- Responsive menu interface

### 🛒 Cart & Orders
- Add items to cart
- Manage cart items
- Order workflow
- Backend-supported order handling
- Authentication protection for user-specific actions

### 📩 Contact
- Contact page
- Contact form
- Location/map section
- Café contact information

### 📖 About
- Café story/about section
- Premium editorial-style layout
- Call-to-action sections

### 🛠️ Django Admin
- Manage users
- Manage menu data
- Manage orders
- Manage project content through Django Admin

### 🎨 UI / Design
- Premium café-inspired visual design
- Warm coffee/brown color palette
- Responsive layout
- Mobile-friendly interface
- Custom CSS styling
- Responsive buttons and components
- Floating WhatsApp contact button
- Newsletter/footer section

### 🚀 Deployment
- Production-ready Django configuration
- Gunicorn support
- WhiteNoise support for static files
- Environment variable configuration
- Render deployment support
- Static file collection with `collectstatic`

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Backend programming |
| **Django 5.2** | Web framework |
| **SQLite** | Database |
| **HTML5** | Page structure |
| **CSS3** | Styling & responsive design |
| **JavaScript** | Frontend interactions |
| **Gunicorn** | Production WSGI server |
| **WhiteNoise** | Static file serving |
| **Render** | Deployment |

---

## 📁 Project Structure

```text
Cafe-Django/
│
├── Cafe_Project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
├── core/
├── menu/
├── orders/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/
├── templates/
│
├── manage.py
├── db.sqlite3
├── requirement.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirement.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=
```

> Never commit your real `SECRET_KEY` or other sensitive credentials to GitHub.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an admin user

```bash
python manage.py createsuperuser
```

### 7. Collect static files

```bash
python manage.py collectstatic --noinput
```

### 8. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

---

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Enables/disables Django debug mode |
| `ALLOWED_HOSTS` | Hosts allowed to serve the application |
| `CSRF_TRUSTED_ORIGINS` | Trusted origins for CSRF protection |

Example:

```env
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
CSRF_TRUSTED_ORIGINS=https://your-domain.com
```

---

## 🚀 Deployment on Render

This project can be deployed as a **Render Web Service**.

### Build Command

```bash
pip install -r requirement.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

### Start Command

```bash
gunicorn Cafe_Project.wsgi:application
```

### Production Environment Variables

```env
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=your-render-domain.onrender.com
CSRF_TRUSTED_ORIGINS=https://your-render-domain.onrender.com
```

---

## 🗄️ Database

The project currently uses **SQLite**:

```text
db.sqlite3
```

SQLite is convenient for local development and small/demo projects.

For a larger production application, a persistent production database such as PostgreSQL can be considered.

---

## 🔒 Security Notes

Before deploying:

- Keep `DEBUG=False` in production.
- Store secrets in environment variables.
- Do not commit `.env`.
- Do not expose private credentials.
- Configure `ALLOWED_HOSTS` correctly.
- Configure `CSRF_TRUSTED_ORIGINS` correctly.
- Use HTTPS in production.
- Protect authenticated actions on the backend, not only through frontend UI.

---

## 🖥️ Development Notes

For local development:

```bash
python manage.py runserver
```

For production on a Linux-based deployment environment:

```bash
gunicorn Cafe_Project.wsgi:application
```

Gunicorn is intended for Unix/Linux production environments and is not normally used directly on Windows.

---

## 🧪 Useful Django Commands

```bash
# Start development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Open Django shell
python manage.py shell
```

---

## 🎯 Project Goals

This project demonstrates a complete Django-based café website combining:

- Clean backend architecture
- Django authentication
- Menu management
- Cart/order functionality
- Responsive frontend design
- Admin management
- Static/media handling
- Environment-based configuration
- Production deployment

The goal is to provide a polished café website that feels closer to a real-world hospitality product rather than a basic Django demo.

---

## 📱 Responsive Design

The interface is designed for:

- 💻 Desktop
- 💻 Laptop
- 📱 Mobile
- 📟 Tablet

Responsive styling is applied across navigation, menu cards, forms, buttons, footer content, and other components.

---

## 📝 Future Improvements

Possible future improvements include:

- Online payment integration
- Order status tracking
- Email notifications
- Customer order history
- Advanced menu filtering
- Product reviews and ratings
- Reservation/booking system
- PostgreSQL production database
- Cloud media storage
- Automated testing
- CI/CD pipeline
- Improved analytics dashboard

---

## 👨‍💻 Author

**Your Name**

Built with ❤️ using **Django, Python, HTML, CSS & JavaScript**.

---

## 📄 License

This project is currently intended as a personal/portfolio project.

If you plan to distribute or reuse it publicly, add an appropriate open-source license such as MIT and update this section accordingly.

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.
