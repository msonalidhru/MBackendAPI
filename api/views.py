## Import all Packages needed from django rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

## Import the clsMiro for generating ID
from .models import clsMiro
from .serializers import miroSerializer

import logging

# Create your views here.

class miroAPI(APIView):
    """
    GET: Returns a Miro Unique ID for the StudyID and SubjectID provided for authenticated user.
         Authorization: Basic Auth, requires username and password supplied by API admin
         Input Parameters: 
                    1) studyid -> string
                    2) subjectid -> string
                    
         Output: JSON String with "strMiroID" key that contains Hexadecimal string
             { "strMiroID": "<Unique Miro ID returned>"}
         
         Sample Python client:
             
            import requests
            resp = requests.get('<ServerName>/Api/?studyid=<value>&subjectID=<value>', auth=(<UserName>, <Pwd>))
            print("API Status Code: " + str(resp.status_code))
            print("API Returned Value: "+ resp.text)    
    """
    def get(self, request):
        try:
            ## Authenticate User credentials
            if(not request.user.is_authenticated):
                result = "Please provide Username and Password"
                response = Response(result, status=status.HTTP_401_UNAUTHORIZED)
                return response
            
            ## Retrieve QryString Parameter Name should be case in-sensitive
            argStudyID = argSubID = ''
            for k, v in request.GET.dict().items():
                if(k.lower() == 'studyid'):
                    argStudyID = v
                elif(k.lower() == 'subjectid'):     
                    argSubID = v
            # If either parameter is empty then return Message to user
            if(argStudyID == '' or argSubID == ''):
                # Return empty response
                result = "Please pass Parameter studyID=" + argStudyID + \
                        ", subjectID=" + argSubID + " values and try again."
                response = Response(result, status=status.HTTP_428_PRECONDITION_REQUIRED)
                return response
            
            ## Valid User and Parameters call Model to generate MiroID    
            objMiro = clsMiro()
            strMiroID = objMiro.generate_miro_subject_id(argStudyID, argSubID)
            strResponse= {"strMiroID": strMiroID}
            result = miroSerializer(strResponse).data
            response = Response(result, status=status.HTTP_200_OK, content_type='application/json')
        except Exception as e:
            # Get logger instance (if it doesnt exist it will create one
            logger = logging.getLogger(__name__)
            # Get the exception
            strException = str(e)
            logger.error(strException)
            response = Response(strException, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            return response