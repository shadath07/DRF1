import requests

URL = "http://127.0.0.1:8000/student_details/2"
  
r = requests.get(url = URL)

# extracting
data = r.json()
print(data)

# try:
#     r = requests.get(url=URL)
#     r.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)

#     if r.text:  # Check if response content is not empty
#         data = r.json()  # Attempt to parse JSON
#         print(data)
#     else:
#         print("Response is empty.")
# except requests.exceptions.HTTPError as http_err:
#     print(f"HTTP error occurred: {http_err}")
# except requests.exceptions.RequestException as req_err:
#     print(f"Request error occurred: {req_err}")
# except ValueError as json_err:
#     print(f"JSON decoding error occurred: {json_err}")