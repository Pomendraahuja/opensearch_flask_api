from opensearch_client import get_opensearch_client

sample_students = [
    {"student_id": "S101", "name": "Amit Sharma", "age": 21, "course": "B.Tech", "scores": 85},
    {"student_id": "S102", "name": "Priya Verma", "age": 22, "course": "MBA", "scores": 90},
    {"student_id": "S103", "name": "Rohit Gupta", "age": 20, "course": "B.Sc", "scores": 78}
]

if __name__ == "__main__":
    client = get_opensearch_client()
    INDEX_NAME = "student_records" 

    for student in sample_students:
        client.index(index=INDEX_NAME, id=student["student_id"], body=student)
    print("Sample students inserted successfully.")