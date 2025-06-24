# Late Show API

A Flask REST API for managing a Late Night Show system. Built with PostgreSQL, Flask-JWT for authentication, and MVC architecture.

## 📦 Tech Stack

- Python + Flask
- Flask-SQLAlchemy
- PostgreSQL
- Flask-Migrate
- Flask-JWT-Extended
- Postman (for API testing)

---

## 🔧 Setup Instructions


## 1. Clone the repo
``` console
https://github.com/Kabogo-Maverick/late_show.git
```

### 2. Install dependencies

```bash
pipenv install
pipenv shell
```

### 3. View the database
open psql and run;

```console
psql -U postgres -d show_db -h localhost
```

```console
pharaoh as the db pass
```


### 4. Run migrations and seed

```console
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python -m server.seed
```

### BELOW IS THE AUTHENTICATION FLOW

## Register :

```console
POST /register
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}
```

## Login :

```console
POST /login
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}
```

## NB: 🔐 You’ll receive a token like:
```console
{ "access_token": "..." }
```

## 🔬 Postman Testing
```console
Open Postman → Import

Choose challenge-4-lateshow.postman_collection.json

Go to Environments → Create one named LateShowEnv

Add variable:

token = (Paste your login token here)

Select LateShowEnv in the top-right dropdown

Click Send on protected routes → they’ll work with the token!
```

Thank you and enjoy the experience!
