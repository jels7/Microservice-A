import requests

BASE_URL = "http://127.0.0.1:5000/api/resource"

def test_get_resource():
    response = requests.get(BASE_URL)
    print(f"GET /api/resource: {response.status_code} - {response.text}")

def test_create_resource():
    data = {"key": "value"}
    response = requests.post(BASE_URL, json=data)
    print(f"POST /api/resource: {response.status_code} - {response.json()}")

def test_update_resource(resource_id):
    data = {"key": "new_value"}
    response = requests.put(f"{BASE_URL}/{resource_id}", json=data)
    print(f"PUT /api/resource/{resource_id}: {response.status_code} - {response.json()}")

def test_delete_resource(resource_id):
    response = requests.delete(f"{BASE_URL}/{resource_id}")
    print(f"DELETE /api/resource/{resource_id}: {response.status_code}")

if __name__ == "__main__":
    test_get_resource()
    test_create_resource()
    test_update_resource(1)  # Replace with a valid resource ID
    test_delete_resource(1)  # Replace with a valid resource ID