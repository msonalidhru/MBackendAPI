# Backend API
API created using Python and Django Rest Framework. This API contains a function which accepts two input parameters and generates a unique ID.

URL: ServerName/Api/?Studyid=value&subjectID=value"
Auth Header: UserName and Password

Python Client API to consume this service:
------------------------------------------------
import requests

apiUrl = "<http://URL>"

apiUName = "username"

apiPwd = "pwd"

resp = requests.get(apiUrl, auth=(apiUName, apiPwd))
print("---- API Status Code: -----" + str(resp.status_code) +"\n")
print("---- API Returned Value -----")
print(resp.text)
