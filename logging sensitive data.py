#Example 11: logging sensitive data
import logging

logging.basicConfig(level=logging.INFO)

def log_user_info(user_id, user_email, password):
    logging.info(f"User ID: {user_id}, Email: {user_email}, Password: {password}") #Vulnerable line.

log_user_info(123, "test@example.com", "anotherterriblepassword")