import requests

def fetch_posts(url, timeout = 10):
    """ Fetch posts from the given API URL"""

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raise an error
        return response.json()
    
    except requests.exceptions.ConnectionError:
        print("Connection error while fetching posts.")
        return []

    except requests.exceptions.Timeout:
        print("Request timed out while fetching posts.")
        return []


def fetch_users(url, timeout = 10):
    """ Fetch users from the given API URL"""

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raise an error
        return response.json()
    
    except requests.exceptions.ConnectionError:
        print("Connection error while fetching users.")
        return []

    except requests.exceptions.Timeout:
        print("Request timed out while fetching users.")
        return []


