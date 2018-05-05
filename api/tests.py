# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework import status
import api.config as cfg

# API Test Case
class clsMiroTest(APITestCase):
    
    def setUp(self):
        # Create a test User
        self.objUser = User.objects.create_user(username = cfg.testConfig["userName"], 
                    password = cfg.testConfig["pwd"])
        self.objClient = APIClient()
        self.objClient.force_authenticate(user=self.objUser)
        
        # Fetch the Input Param and Output Param values for testing from config file
        self.lstTestValues = cfg.testValidValues
        
    def test_valid_generate_miro_subject_id(self):
        # For every dictionary row of I/O function paramaters
        for val in self.lstTestValues:
            # Retrieve the values
            strStudyID = val["studyID"]
            strSubID = val["subjectID"] # May contain Unicode chars
            strTestResult = val["result"]
            
            # Test success for valid user and valid parameters passed
            response = self.objClient.get('/api/?studyid=' + strStudyID + '&subjectid=' + strSubID)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
            # Test MiroID is the same for every consecutive calls for a 
            # pair of Input params
            strJson = response.data
            strResult = strJson["strMiroID"]
            self.assertEqual(strResult, strTestResult)
            
            # Test if the return string is hexadecimal
            self.assertTrue(bool(int(strResult, 16)))
            
    def test_errors_generate_miro_subject_id(self):
        # Test Error when only studyid is passed
        response = self.objClient.get('/api/?studyid=1')
        self.assertEqual(response.status_code, status.HTTP_428_PRECONDITION_REQUIRED)     
        
        # Test Error when only subjectid is passed  
        response = self.objClient.get('/api/?subjectid=abc')
        self.assertEqual(response.status_code, status.HTTP_428_PRECONDITION_REQUIRED)
        
        #Test Error when no parameters are passed
        response = self.objClient.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_428_PRECONDITION_REQUIRED)
        
        #Test Unauthenticated Users
        testClient = APIClient()
        response = testClient.get('/api/?studyid=1&subjectid=abc')  
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)    

# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
#https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
#http://knowpapa.com/import/