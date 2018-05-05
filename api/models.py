# Import Section
import hashlib

# API Model Class
class clsMiro(object):

    '''
    # Function Name: generate_miro_subject_id
    # Input: argStudyID -> str, argSubID -> str
    # Output: UniqueID which will be the same across calls
    '''
    def generate_miro_subject_id(self, argStudyID, argSubID):
        # Generate Miro ID based on the StudyID and SubID
        strID = str(argStudyID) + str(argSubID)
        
        # Use Hash to generate a unqiue ID
        
        # encode() converts string into seq of bytes as hash function requires bytes
        # hexdigest() returns Hex string representing the hash
        strMiroID = hashlib.sha256(str(strID).encode('utf-8')).hexdigest()
        
        # Newly created ID
        return strMiroID