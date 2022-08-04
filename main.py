import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""
GRAPH_ID = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response)

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Coding Graph",
    "unit" : "hours",
    "type" : "float",
    "color" : "shibafu"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

today = datetime.now().strftime(r"%Y%m%d")

graph1_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
graph1_parameters = {
    "date" : today,
    "quantity" : input("How many hours did you code today? "),

}
response = requests.post(url=graph1_endpoint,json=graph1_parameters, headers=headers)
print(response.text)
