# Adronall E-commerce

Adronall is a fully designed and developed e-commerce platform that provides a seamless experience for users and sellers. The project encompasses features such as user and seller logins, an admin dashboard, product management, cart APIs, and order functionality.

## Features

- **User and Seller Login**: Secure authentication using JWT.
- **Admin Dashboard**: Comprehensive management of products, users, and orders.
- **Product Management**: Create, update, and delete products.
- **Shopping Cart**: Add and remove items from the cart.
- **Order Functionality**: Process and manage user orders.
- **User and Seller Information**: Manage profiles and account details.

## Technologies Used

- **Backend**: Django REST Framework
- **Celery**: For asynchronous task management
- **Database**: PostgreSQL
- **Caching**: Redis
- **Authentication**: JWT (JSON Web Token)
- **Frontend**: Flutter

## Getting Started

### Prerequisites

- Python 3.x
- Django
- PostgreSQL
- Redis
- Flutter

### Installation (Backend)

1. Clone the repository:
   ```bash
   git clone https://github.com/Sanket-Ugale/adronall.git

   # For backend
   cd adronall/Backend

   # For app
   cd adronall/AdronAll-App

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
4. Set up the PostgreSQL database:
5. Create a database in PostgreSQL.
6. Update your database settings in settings.py.
7. Run migrations:
    ```bash
    python manage.py migrate
8. Start the Django development server:
    ```bash
    python manage.py runserver

### Installation (App)

1. Clone the repository:
   ```bash
   git clone https://github.com/Sanket-Ugale/adronall.git

   cd adronall/AdronAll-App

2. Install dependencies
    ```bash
    flutter pub get
3. Run Flutter App
    ```bash
    flutter run