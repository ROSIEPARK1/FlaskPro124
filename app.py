from flask import Flask,jsonify,request

app = Flask(__name__)

data = [
    {
        "id":1,
        "Contact":"6579081230",
        "Name":"Jennie",
        "done":False
    },
    {
        "id":2,
        "Contact":"9876543210",
        "Name":"Rose",
        "done":False
    
    },

    {
        "id":3,
        "Contact":"9078654321",
        "Name":"Lisa",
        "done":False
    
    },
    {
        "id":2,
        "Contact":"6789054321",
        "Name":"Jisoo",
        "done":False
    
    }


]

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":data
    })
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json :
        return jsonify({
            "status":"error",
            "message":"please provide the data !"

        },400)

    contact = {
        "id":data[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get("Contact",""),
        "done":False
    }
    data.append(contact)
    return jsonify ({
        "status":"success",
        "message" : "task added successfully "  
    }),200
        


if (__name__ == "__main__"):
    app.run()

