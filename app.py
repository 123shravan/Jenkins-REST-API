
from flask import Flask, jsonify, request

app = Flask(__name__)

# Student data
students = [
    {"id": 1, "name": "Rahul", "course": "CSE"},
    {"id": 2, "name": "Priya", "course": "IT"}
]

# Home API
@app.route("/")
def home():
    return jsonify({
        "message": "Student REST API is running",
        "status": "Success"
    })

# Get all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students), 200

# Add new student
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("course"):
        return jsonify({"error": "Name and course required"}), 400

    new_student = {
        "id": max([s["id"] for s in students], default=0) + 1,
        "name": data["name"],
        "course": data["course"]
    }

    students.append(new_student)

    return jsonify(new_student), 201

# Get student by ID
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student), 200

    return jsonify({"error": "Student not found"}), 404

# Run application
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
