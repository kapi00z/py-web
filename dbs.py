import json, os
from faker import Faker

fake = Faker()

def person():
    p = {"name": fake.name(), "email": fake.email(), "phone": fake.phone_number(), "uuid": fake.uuid4()}
    return p

def path(name):
    return f"databases/{name}.db"

def create(name):
    with open(path(name), 'w') as file:
        file.write(json.dumps([person() for i in range(5000)]))

def load(name):
    with open(path(name), 'r') as file:
        return json.loads(file.read())
    
def select(name):
    if(not os.path.isfile(path(name))):
        create(name)
    return load(name)
    
def save(name, data):
    with open(path(name), 'w') as file:
        file.write(json.dumps(data))