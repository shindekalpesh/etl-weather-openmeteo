import requests

latitude = "19.076090"
longitude = "72.877426"

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&&current_weather=true"
print(url)

response = requests.get(url)
print("response", type(response), response)

if response.status_code == 200:
    data = response.json()
    print("data", type(data), data)
else:
    print("Error occured!")

