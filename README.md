
# Todo App API

This is a RESTful API for a Todo application built using Django and Django Rest Framework. The API allows users to create, read, update, and delete (CRUD) todo items.

## Features

- User authentication using JWT
- CRUD operations for todos
- API documentation using Swagger OpenAPI

## Technologies Used

- **Django**: Backend framework
- **Django Rest Framework**: For building the API
- **JWT Authentication**: For securing the API
- **PostgreSQL**: Database
- **Docker**: Containerization (optional)
  
## API Endpoints

| Method | Endpoint                  | Description                        | Auth Required |
|--------|---------------------------|------------------------------------|---------------|
| POST   | `/api/auth/login/`         | Log in and get a JWT token         | No           |
| GET    | `/api/todos/`              | Retrieve a list of todos           | Yes          |
| POST   | `/api/todos/`              | Create a new todo                  | Yes          |
| GET    | `/api/todos/{id}/`         | Retrieve details of a specific todo| Yes          |
| PUT    | `/api/todos/{id}/`         | Update a todo entirely             | Yes          |
| PATCH  | `/api/todos/{id}/`         | Update a todo                      | Yes          |
| DELETE | `/api/todos/{id}/`         | Delete a todo                      | Yes          |

## Installation

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Mohammadreza-Alizadeh/Todo-App.git
   cd TODO-App/
   ```
2. Copy `.env.example` to `.env`  
    ```bash
    cp .env.example .env
    ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. You can now access the API at `http://127.0.0.1:8000/`.

### Docker Setup (Optional)

If you prefer to use Docker, follow these steps:

1. Copy `.env.example` to `.env`  
    ```bash
    cp .env.example .env
    ```

2. Build the Docker image:
   ```bash
   docker compose build
   ```

3. Run the containers:
   ```bash
   docker compose up
   ```

The API will be available at `http://localhost:8000/`.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://github.com/jazzband/djangorestframework-simplejwt)