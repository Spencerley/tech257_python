import requests

# Helpful for making http requests - protocol used to serve up webpages on the internet
# Can get information from the internet using this

request_bbc = requests.get("https://www.bbc.co.uk/")
print(request_bbc.status_code)
print(request_bbc.content)
