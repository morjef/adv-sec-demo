# Example 8: Environment variable misuse (simulated, real env vars are better)
import os

os.environ['DB_PASSWORD'] = 'anotherbadpassword' #Simulating env var usage. Never hardcode in real code.

def connect_to_db():
  password = os.environ.get('DB_PASSWORD')
  if password == 'anotherbadpassword':
    print('Connecting to db')
  else:
    print('Incorrect password')
