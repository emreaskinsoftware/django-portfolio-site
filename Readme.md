# 🚀 Full-Stack Django Portfolio Website

This project is a **professional full-stack portfolio website** built using Django, applying **senior-level software architecture principles** such as SRP (Single Responsibility), DRY (Don’t Repeat Yourself), and MVT (Model-View-Template).

> 🔗 **Live Demo:** *Not deployed yet — coming soon*

---

## ✨ Key Features & Architecture

### 🧱 1. Modular & Maintainable Architecture

Designed as a *scalable, secure, and production-ready* system:

* **SRP (Single Responsibility):** The project is divided into 5 independent Django apps — `pages`, `projects`, `blog`, `contact`, and `ratelimit`.
* **DRY (Don’t Repeat Yourself):** Shared UI elements (Navbar, Footer, etc.) are managed via `_base.html` and extended by all templates.

### ⚙️ 2. Backend (Django MVT + Forms)

* **Relational Models:** Uses proper one-to-many relations (e.g., `ProjectGalleryImage` with `ForeignKey`).
* **Rich Text Editing:** Integrated **CKEditor** for professional blog content management (images, code snippets, formatted text).
* **Inline Admin:** Admin panel supports inline gallery image management for each project.
* **Secure Forms:** Contact form is CSRF-protected and server-side validated using Django’s `forms.py`.

### 🔒 3. Security & Environment Management

* **Environment Variables:** Sensitive keys (e.g. `SECRET_KEY`, `EMAIL_HOST_PASSWORD`) stored in `.env` using `django-environ`.
* **Git Ignore Rules:** `.env`, `venv`, and database files are excluded from Git to prevent leaks.
* **Spam Protection:** Integrated `django-ratelimit` to prevent brute-force/spam attacks (e.g., max 5 requests/minute per IP).

### 🎨 4. Frontend (Bootstrap 5 + Custom Styling)

* **Responsive Design:** Built with Bootstrap’s grid and utility system.
* **Custom Theme:** Uses `main.css` with CSS Variables (`:root`) for branded light-mode color palette.
* **Smooth Animations:** Enhanced with AOS (Animate on Scroll) and CSS transitions for a polished user experience.

---

## 🧠 Tech Stack

| Layer       | Technology                                 |
| ----------- | ------------------------------------------ |
| Backend     | Django (Python)                            |
| Frontend    | HTML5, CSS3, Bootstrap 5, AOS.js           |
| Database    | SQLite (Development)                       |
| CMS / Admin | django-ckeditor, Pillow                    |
| Security    | django-ratelimit, django-environ           |
| Deployment  | Docker, Gunicorn, Nginx (Production Ready) |

---

## ⚡ Local Setup (Development)

```bash
# 1️⃣ Clone the repository
git clone https://github.com/emreaskinsoftware/django-portfolio.git
cd django-portfolio

# 2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate      # macOS/Linux
.\venv\Scripts\activate       # Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Apply migrations
python manage.py migrate

# 5️⃣ Create a superuser
python manage.py createsuperuser

# 6️⃣ Run the development server
python manage.py runserver
```

Visit:
🌐 [http://127.0.0.1:8000/](http://127.0.0.1:8000/) → Portfolio site
🔑 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) → Admin panel

---

## 🐳 Docker Setup (Production Ready)

To build and run the app with Docker (Gunicorn + Nginx stack):

```bash
docker compose -f docker-compose.prod.yml up --build
```

Access it via:
🔘 [http://localhost](http://localhost)

---

## 🧰 Project Highlights

* ✅ Modular, extensible Django architecture
* ✅ Secure `.env`-based configuration
* ✅ Ready for Gunicorn + Nginx deployment
* ✅ Rate-limited contact form (anti-spam)
* ✅ Responsive & animated frontend

---

## 👤 Author

**👨‍💻 EMRE AŞKIN**

* 🔗 [GitHub Profile](https://github.com/emreaskinsoftware)
* 💼 [LinkedIn](https://www.linkedin.com/in/emre-askin)

---

> *“Professional code is not just about making it work — it’s about making it last.”*
