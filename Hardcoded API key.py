# Example 3: Hardcoded API key
import requests
def get_data(api_key, resource):
  url = f"https://api.example.com/{resource}?key={api_key}"
  response = requests.get(url)
  return response.json()

api_key = "YOUR_SECRET_API_KEY_HERE"