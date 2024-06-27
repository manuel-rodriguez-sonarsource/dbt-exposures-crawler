import requests


class DbtRest:
    def __init__(self, account_id, token):
        self.base_url = f"https://emea.dbt.com/api/v2/accounts/{account_id}"
        self.headers = {'Accept': 'text/html', 'Authorization': f'Bearer {token}'}

    def fetch_manifest(self, job_id):
        url = f"{self.base_url}/jobs/{job_id}/artifacts/manifest.json"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()  # Raises a HTTPError if the response status is 4xx, 5xx
        return response.json()
