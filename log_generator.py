import random
import string
import time
import logging


#Setting up logging for error handling

logging.basicConfig(filename="log_generator.log" , level= logging.ERROR)


#List the level of loggs

LOG_LEVELS = ["INFO" , "DEBUG" , "ERROR" , "WARNING"]

#List of possible actions

ACTIONS = ["Login" , "Logout" , "Data Request" , "File Upload" , "Download" , "Error"]

#Functions to generate randon strings for the logs 

def generate_random_string(length=10):
    """
    Genearte the string of the given length (default length is 10 characters)
    """
    try:
     return ''.join(random.choice(string.ascii_letters + string.digits , k=length))
    except Exception as e:
       logging.error(f"Error is generated_random_string: {e}")