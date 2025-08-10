This project demonstrates a simple REST API built with Flask that interacts with OpenSearch to perform basic CRUD operations on a `student_records` index.  
The API supports:

- **POST /student** — Add a new student record  
- **GET /student/<student_id>** — Retrieve a student record by ID  
- **DELETE /student/<student_id>** — Delete a student record by ID

---

## Setup Instructions

### 1. Install and Run OpenSearch (via Docker)

- Make sure you have Docker installed.
- Run the OpenSearch container:

- ```docker-compose up -d```


- Verify OpenSearch is running by visiting: http://localhost:9200
- You should see JSON output with cluster info.

### 2. Create Virtual Environment and Install Dependencies

- ```python -m venv .venv```
- ```source .venv/bin/activate```  
# On Windows: ```.venv\Scripts\activate```
- ```pip install -r requirements.txt```

### 3. Create Index and Insert Sample Data (Optional)

Run the index setup script to create the student_records index and add 3 sample students:

- ```python sample_index.py```

### 4. Run the Flask API

- python app.py
The API will start on http://127.0.0.1:5000

## API Endpoints:

### 1. Add a New Student

```curl -X POST http://127.0.0.1:5000/student \```
```-H "Content-Type: application/json" \```
```-d '{"student_id":"S105", "name":"Rahul Mehta", "age":22, "course":"Flask", "score":91.2}'```

### 2. Get Student by ID

```curl -X GET http://127.0.0.1:5000/student/S101```

### 3. Delete Student by ID

```curl -X DELETE http://127.0.0.1:5000/student/S105```


## Git Branch Structure

- `feature/opensearch`
Contains OpenSearch setup, index mapping, and sample data insertion.

- `feature/flask_api`
Contains Flask API implementation.

- `main (or master)`
Stable branch, integrates tested features from other branches.



### Notes

# The student_index_mapping.json file holds the index mappings.

# The .gitignore file excludes environment files and caches.

# If you don't want sample data inserted at start, just skip running sample_index.py.

