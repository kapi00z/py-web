from flask import Flask, redirect, url_for, request, jsonify
import dbs

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/db/<name>", methods = ['POST', 'GET'])
def people(name):
    if request.method == "POST":
        db = dbs.select(name)
        args = request.get_json(force=True)
        add = dbs.person()
        found = False
        for p in db:
            if p['name'] == args['name']:
                for key in args.keys():
                    add[key] = args[key]
                p = add
                found = True
                break
        if found is False:
            db.append(add)
        dbs.save(name, db)
        return db
    else:
        db = dbs.select(name)
        args = request.get_json(force=True)
        if 'name' in args.keys():
            for p in db:
                if p['name'] == args['name']:
                    return p
        elif 'uuid' in args.keys():
            for p in db:
                if p['uuid'] == args['uuid']:
                    return p
        else:
            return db
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)