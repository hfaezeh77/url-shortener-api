# URL Shortener API

A REST API built with Django REST Framework and MongoDB that converts long URLs into short links and redirects users to their original destinations.

## Features

- Create short URLs through a REST API.
- Generate six-character alphanumeric short codes.
- Redirect short links to their original URLs.
- Store URL records persistently in MongoDB.
- Validate URL input and return appropriate error responses.

## Tech Stack

- Python
- Django
- Django REST Framework
- MongoDB
- PyMongo
- Docker

## Project Structure

```text
url-shortener/
├── config/
│   ├── settings.py
│   └── urls.py
├── shortener/
│   ├── db.py
│   ├── urls.py
│   └── views.py
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository URL.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd url-shortener
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you have not created `requirements.txt`, you can install the main dependencies manually:

```bash
pip install django djangorestframework pymongo python-dotenv
```

### 4. Configure environment variables

Create a `.env` file in the project root, next to `manage.py`:

```env
MONGODB_URI=mongodb://admin:YOUR_PASSWORD@localhost:27017/?authSource=admin
```

Replace `YOUR_PASSWORD` with the password configured for your local MongoDB container. Do not commit `.env` or real credentials to GitHub.

### 5. Start MongoDB with Docker

For a new local development container:

```bash
docker run -d \
  --name url-shortener-mongodb \
  -p 27017:27017 \
  -v mongodb_url_data:/data/db \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=YOUR_PASSWORD \
  mongo:7
```

Use the same password in `MONGODB_URI` and `MONGO_INITDB_ROOT_PASSWORD`.

If the container already exists but is stopped, start it with:

```bash
docker start url-shortener-mongodb
```

### 6. Run Django

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/hello/` | Check that the API is working |
| POST | `/api/shorten/` | Create a short URL |
| GET | `/<short_code>/` | Redirect to the original URL |

### Create a Short URL

**Request**

`POST /api/shorten/`

```json
{
  "url": "https://www.djangoproject.com/"
}
```

**Example response**

```json
{
  "original_url": "https://www.djangoproject.com/",
  "short_code": "aB12xY",
  "short_url": "http://127.0.0.1:8000/aB12xY/"
}
```

The generated short code will vary.

## Error Handling

The API is intended to return `400 Bad Request` when the URL is missing or invalid, and `404 Not Found` when a short code does not exist.

## Future Improvements

- Add collision-safe code generation and a unique database index.
- Add automated API tests.
- Add URL listing and deletion endpoints.
- Improve production configuration and deployment.
- Add rate limiting and stronger input validation.

## Learning Goals

This project demonstrates REST API development, HTTP methods and status codes, MongoDB integration using PyMongo, Docker-based database setup, and environment-based configuration.
