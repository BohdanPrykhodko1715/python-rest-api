def create_user_schema():
    return {
        "id": None,
        "name": ""
    }

def create_category_schema():
    return {
        "id": None,  # unique identifier for the category
        "name": ""  # name of the category
    }

def create_record_schema():
    return {
        "id": None,  # unique identifier for the record
        "user_id": None,  # ID of the associated user
        "category_id": None,  # ID of the associated category
        "date": "",  # date of the record
        "amount": 0.0  # amount spent
    }

users = []
categories = []
records = []