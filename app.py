import json
from flask import Flask, request, jsonify
from opensearchpy import OpenSearch
from opensearch_client import get_opensearch_client
import uuid

app = Flask(__name__)

# Initialize OpenSearch client
client = get_opensearch_client()

# Load index mapping and settings from JSON file
with open("student_index_mapping.json") as f:
    mapping_data = json.load(f)

INDEX_NAME = mapping_data["index_name"]

# Check if index exists; create if missing (no sample data here)
if not client.indices.exists(index=INDEX_NAME):
    client.indices.create(index=INDEX_NAME, body={
        "settings": mapping_data.get("settings", {}),
        "mappings": mapping_data.get("mappings", {})
    })
    print(f"Index '{INDEX_NAME}' created automatically by app.py")

# Simplifying  API routes
@app.route("/students", methods=["POST"])
def add_student():
    """
    Add a student record to the OpenSearch index.
    Generates a UUID if student_id is not provided.
    """
    data = request.get_json()
    student_id = data.get("student_id", str(uuid.uuid4()))
    data["student_id"] = student_id

    response = client.index(index=INDEX_NAME, id=student_id, body=data)
    return jsonify({"result": response["result"], "id": response["_id"]}), 201

@app.route("/students/<student_id>", methods=["GET"])
def get_student(student_id):
    """
    Retrieve a student record by student_id.
    """
    try:
        response = client.get(index=INDEX_NAME, id=student_id)
        return jsonify(response["_source"]), 200
    except Exception:
        return jsonify({"error": "Student not found"}), 404

@app.route("/students/<student_id>", methods=["DELETE"])
def delete_student(student_id):
    """
    Delete a student record by student_id.
    """
    try:
        response = client.delete(index=INDEX_NAME, id=student_id)
        return jsonify({"result": response["result"]}), 200
    except Exception:
        return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)