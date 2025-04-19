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
       return "ERROR"
       


#Function to generate the random log entry 
def generate_log():
   """
   Generate a random log entry with a timestamp , log level , action and user 
   """
   try:
    log_level = random.choice(LOG_LEVELS)
    timestamp= time.strftime("%Y-%m-%d %H-%M%S" , time.gmtime())
    action = random.choice(ACTIONS)
    user= generate_random_string(8)
    log_entry= f"{timestamp} - {log_level} - {action} - User: {user}"
    return log_entry
   except Exception as e:
     logging.error(f"Error is generated_log_entry: {e}")
     return "ERROR"

