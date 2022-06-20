# install requests and jsonpath
# cmd: pip install requests,pip install -u jsonpath : -u will update or reinstall the latest package
import json
import jsonpath
import requests

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(response.headers)
print(response)
print(response.content)

# parse response into json format
json_response = json.loads(response.text)
print(json_response)

# Fetch value using json path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print("==========")
print(pages[0])
