import requests

apiUrl = 'http://mailtosonalid.pythonanywhere.com/api/?studyid=json&subjectID=a'
apiUName = 'apiuser'
apiPwd = 'mirouser'

print("-------------------------")
print("---- Valid Request  -----")
print("-------------------------")
resp = requests.get(apiUrl, auth=(apiUName, apiPwd))
print("Status Code: " + str(resp.status_code) +"\n")
print("API Returned Value ")
print(resp.text)

print("------------------------------------------------------------")
print("---- Invalid Request: User Authorization not provided  -----")
print("------------------------------------------------------------")
resp = requests.get(apiUrl)
print("Status Code: " + str(resp.status_code) +"\n")
print("API Returned Value ")
print(resp.text)

print("------------------------------------------------------------")
print("---- Invalid Request: studyid not provided  ----------------")
print("------------------------------------------------------------")
apiUrl = 'http://mailtosonalid.pythonanywhere.com/api/?subjectID=a'
resp = requests.get(apiUrl, auth=(apiUName, apiPwd))
print("Status Code: " + str(resp.status_code) +"\n")
print("API Returned Value ")
print(resp.text)

print("------------------------------------------------------------")
print("---- Invalid Request: subjectID not provided  ----------------")
print("------------------------------------------------------------")
apiUrl = 'http://mailtosonalid.pythonanywhere.com/api/?studyid=a'
resp = requests.get(apiUrl, auth=(apiUName, apiPwd))
print("Status Code: " + str(resp.status_code) +"\n")
print("API Returned Value ")
print(resp.text)
