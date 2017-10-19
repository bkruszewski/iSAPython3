import requests

response = requests.get("http://trojmiasto.pl/iuhiuh")

try:
    response.raise_for_status()
except Exception as e:
    print("Wystąpił bład:", e)
finally:
    print(response.status_code)


