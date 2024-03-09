from faker import Faker
import json, os

fake = Faker()

dbPath = os.path.join(os.path.dirname(__file__), 'database')
if not os.path.isdir(dbPath):
    os.mkdir(dbPath)

def reset(dbFile):
    data = []
    for i in range(5000):
        data.append({"name": fake.name(), "email": fake.email(), "phone": fake.phone_number(), "uuid": fake.uuid4()})
    with open(dbFile, 'w') as file:
        file.write(json.dumps(data))

def load(dbName):
    dbFile = os.path.join(dbPath, f"{dbName}.db")
    if not os.path.isfile(dbFile):
        reset(dbFile)
    with open(dbFile, 'r') as file:
        data = json.loads(file.read())
    return data, dbFile

def printDB(dbName):
    db, dbFile = load(dbName)
    print(db)

def save(data, dbFile):
    with open(dbFile, 'w') as file:
        file.write(json.dumps(data))
    return True

def update(dbName, data):
    dbFile = os.path.join(dbPath, f"{dbName}.db")
    if type(data) is not dict:
        try:
            jsondata = json.loads(data)
        except ValueError:
            return "Data is not JSON"
    else:
        jsondata = data
    
    db, dbFile = load(dbName)
    db.append(jsondata)
    save(db, dbFile)