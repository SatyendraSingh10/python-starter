import requests
try:
    statusCode = requests.get("http://127.0.0.1:5000/slowclusters").status_code
    if not 200 <= statusCode <= 400:
        print(statusCode)

except Exception as e:
    print(e)

