import requests
idno = input("Enter IDNO : ")
result = requests.get("http://127.0.0.1:8000/one/"+idno)
print(result.status_code)
print(result.json())