import requests

apiUrl = 'http://127.0.0.1:8000/Api/?studyid=json&subjectID=a'
apiUName = 'apiuser'
apiPwd = 'mirouser'

resp = requests.get(apiUrl, auth=(apiUName, apiPwd))
print("---- API Status Code: -----" + str(resp.status_code) +"\n")
print("---- API Returned Value -----")
print(resp.text)