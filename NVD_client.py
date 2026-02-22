import os
import requests

NVD_API_KEY = os.getenv("NVD_API_KEY")

# 2. Configure headers specifically for NVD v2.0
HEADERS = {
    "apiKey": NVD_API_KEY
}

# Example Usage: Fetching a specific CVE
def get_cve_data(cve_id):
    base_url = f"https://services.nvd.nist.gov{cve_id}"
    
    response = requests.get(base_url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"

# Test with a known CVE
if __name__ == "__main__":
    print(get_cve_data("CVE-2023-1234"))
