# Pet Adoption Management System

A Django-based web application for managing pet adoption, pet listings, breeders, pet shops, products, orders, reviews, and breeder bookings.

## Features

- User/adopter registration and login
- Pet browsing and adoption requests
- Pet management by shops
- Breeder registration and pet management
- Breeder booking requests
- User–breeder chat
- Pet shop product management
- Shopping cart and order flow
- Product reviews
- Admin management for users, breeders, and shops
- Django media/static file support

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (development)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Images:** Pillow
- **Static libraries:** Bootstrap, Font Awesome, AOS, Swiper, GLightbox and related frontend assets

## Project Structure

```text
pet_adoption/
├── manage.py
├── pet_adoption/          # Django project configuration
├── pet_app/               # Main application
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── tests.py
├── templates/             # HTML templates
├── static/                # CSS, JavaScript and frontend assets
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd pet_adoption
```

### 2. Create a virtual environment

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and set a secure Django secret key.

```bash
cp .env.example .env
```

> The project reads the environment variables directly. If you use a local `.env` file, make sure it remains ignored by Git.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an admin account

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Important Notes

- `db.sqlite3` is intentionally not included in the GitHub-ready package. Running `python manage.py migrate` creates a fresh development database.
- Uploaded/generated runtime files should not be committed unless they are intentionally part of the project.
- For production deployment, use environment variables for secrets and configure a production database, `DEBUG=False`, allowed hosts, static files, HTTPS, and secure cookie settings.
- Review the existing application code before deploying publicly; this repository is prepared for source control, not hardened as a production deployment.

## Main Django Commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## License

Add the license you want to use before publishing the repository.
