# Expense Tracking REST API

## Визначення варіанту

* Номер групи - 22 
* 22 % 3 = 1 - **Валюти**


## Setup

1. Clone the repository:
```bash
git clone https://github.com/BohdanPrykhodko1715/python-rest-api.git
```

2. Navigate to the project directory and create a virtual environment:
```bash
python3 -m venv env
source env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
flask run --host=0.0.0.0 --port=5000
```

## Docker Setup

1. Build and run the application using Docker:
```bash
docker-compose up --build
```

2. Access the API at: `http://localhost:5000`

## Endpoints

- `POST /users`: Create a user
- `GET /users`: Get all users
- `POST /categories`: Create a category
- `GET /categories`: Get all categories
- `POST /records`: Create a record
- `GET /records/user/<user_id>`: Get records for a user
- `GET /records/category/<category_id>/user/<user_id>`: Get records by category for a user

