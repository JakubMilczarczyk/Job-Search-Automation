import requests
from urllib.parse import urlparse


def check_common_apis_endpoints(url) -> bool:
    parsed_url = urlparse(url)
    base_url = f'{parsed_url.scheme}://{parsed_url.netloc}'
    path = parsed_url.path
    
    common_endpoints = ['/api', '/api/v1', '/api/v2', '/api/v3', '/api/v4']
    for endpoint in common_endpoints:
        try:
            response = requests.get(base_url + endpoint)
            if response.status_code == 200:
                print(f'Found URL: {base_url + endpoint}')
                print('Response:')
                print(response.json())
                return True
        except Exception as e:
            print(f'Error while checking endpoint {base_url + endpoint}: {e}')
    return False


def check_scraping_rules(url) -> bool:
    parsed_url = urlparse(url)
    base_url = f'{parsed_url.scheme}://{parsed_url.netloc}'
    path = parsed_url.path
    
    try:
        response = requests.get(base_url + '/robots.txt')
        if response.status_code == 200:
            print('Found robots.txt rules.')
            robots_txt = response.text
            disallowed_paths = []
            for line in robots_txt.splitlines():
                if line.startswith('Disallow:'):
                    disallowed_path = line.split(': ')[1]
                    disallowed_paths.append(disallowed_path)
            
            for disallowed_path in disallowed_paths:
                if path.startswith(disallowed_path):
                    return False
            return True
        else:
            print('The robots.txt file is missing or cannot be downloaded.')
            return True
    
    except Exception as e:
        print(f'Error downoading robots.txt: {e}')
        return False


if __name__ == '__main__':
    url = input('URL to check: ')
    if check_common_apis_endpoints(url):
        print('Found API\n')
    else:
        print('API not found\n')

    if check_scraping_rules(url):
        print('Scraping allowed.\n')
    else:
        print('Scraping prohibited!\n')
