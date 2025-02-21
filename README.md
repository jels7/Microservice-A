### Requesting Data

To request data from Microservice-A, you need to send an HTTP GET request to the following endpoint:

```
GET http://your-microservice-url/api/data
```

#### Example Request

```bash
curl -X GET http://your-microservice-url/api/data
```

### Receiving Data

The response from Microservice-A will be in JSON format. Here is an example of how to receive and handle the data programmatically using Python:

#### Example Response Handling

```python
import requests

response = requests.get('http://your-microservice-url/api/data')
data = response.json()

print(data)
```

Make sure to replace `http://your-microservice-url` with the actual URL of your microservice.

### Running the Microservice

Ensure you have all the dependencies installed. You can install them using requirements.txt fileL

         pip install -r requirements.txt

Start the Flask application:

         python run.py

In a separate terminal, run the test script to interact with those microservices:

        python test_api.py

### Notes

- Ensure your requests include any necessary headers or authentication tokens as required by your microservice.
- Handle any potential errors or exceptions that may occur during the request.
