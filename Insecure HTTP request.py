# Insecure HTTP request (No SSL verification)
def fetch_data():
    url = input("Enter URL to fetch: ")  # Untrusted user input
    response = requests.get(url, verify=False)  # Missing SSL verification
    return response.text
