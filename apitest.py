import requests

url = "https://rest.method.me/api/v1/tables/Contacts/8"

payload = {}
headers = {
  'Authorization': 'APIKey NjY2YzRhNzY5OTUwZGE2OGFmY2Q1ZGNhLkZGODhDNDgxQ0U0MTQyNEFCMDhDNTQ5NkQ4RTg3ODQ4'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
