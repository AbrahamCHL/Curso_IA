import requests as req

# Get the response from the API endpoint.
response = req.get("http://api.open-notify.org/astros.json")
data = response.json()
# 9 people are currently in space.
print(data["number"])
print(data)
