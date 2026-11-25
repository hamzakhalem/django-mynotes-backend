# MyNotes API

The backend of a notes app: a small REST API built with Django REST Framework. A React frontend for it lives in [reactnotes](https://github.com/hamzakhalem/reactnotes).

## Features

- Create, list, read, update and delete notes
- Notes are sorted by last update
- `GET /api/` lists every route with its method and body, so the API documents itself
- CORS enabled for a separate frontend

## API

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/` | List of all routes |
| GET | `/api/notes/` | All notes |
| GET | `/api/notes/<id>` | One note |
| POST | `/api/notes/create/` | Create a note (`{"body": "..."}`) |
| PUT | `/api/notes/update/<id>` | Update a note |
| DELETE | `/api/notes/delete/<id>` | Delete a note |

## Built with

- Python 3, Django 4.1, Django REST Framework 3.14
- django-cors-headers
- SQLite

## Run it locally

```bash
git clone https://github.com/hamzakhalem/django-mynotes-backend.git
cd django-mynotes-backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
export DJANGO_SECRET_KEY="any-long-random-string"   # PowerShell: $env:DJANGO_SECRET_KEY="..."
cd mynotes
python manage.py migrate
python manage.py runserver
```

The API is then at http://127.0.0.1:8000/api/.

## Project structure

```
mynotes/
  mynotes/   Settings and root URLs
  api/       Note model, serializer and API views
```
