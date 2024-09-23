import requests

class ApiClient:
    def __init__(self, base_url, headers=None):
        """
        Initializes the API client with a base URL and optional headers.
        :param base_url: The base URL of the API.
        :param headers: Optional headers to include in the API calls.
        """
        self.base_url = base_url
        self.headers = headers if headers is not None else {}

    def get(self, endpoint, params=None):
        """
        Sends a GET request to the specified endpoint.
        :param endpoint: API endpoint to append to the base URL.
        :param params: Query parameters to include in the request.
        :return: The response object or None if an error occurs.
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()  # Raise an error for bad status codes (4xx, 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"GET request failed: {e}")
            return None

    def post(self, endpoint, data=None, json=None):
        """
        Sends a POST request to the specified endpoint.
        :param endpoint: API endpoint to append to the base URL.
        :param data: Form data to include in the request body.
        :param json: JSON data to include in the request body.
        :return: The response object or None if an error occurs.
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.post(url, headers=self.headers, data=data, json=json)
            response.raise_for_status()  # Raise an error for bad status codes (4xx, 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"POST request failed: {e}")
            return None

    def set_headers(self, headers):
        """
        Updates or sets the headers for future requests.
        :param headers: A dictionary of headers to set.
        """
        self.headers.update(headers)
