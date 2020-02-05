import sys
import requests
from static_variables import *


def get_data_collection_from_github_api(url):
    data = []
    while 1:
        response = get_response_from_github_api(url)
        json_response = response.json()
        data += json_response
        if LINK in response.headers:
            url = get_next_page_url(response.headers[LINK])
        else:
            url = None

        if url is None:
            break

    return data


def get_next_page_url(links):
    links = links.split(", ")
    for link in links:
        ind = link.find('next')
        if ind != -1:
            return link[1:ind - 8]

    return None


def get_single_data_from_github_api(url):
    response = get_response_from_github_api(url)
    json_response = response.json()
    return json_response


def get_response_from_github_api(url):
    token = '5f682f5cc3dd7069ae351a52ddc7297e8858e02a'
    headers = {'Authorization': 'token ' + token}

    response = requests.get(url, headers=headers)
    check_for_unexpected_response(response, url)

    return response


def check_for_unexpected_response(response, url):
    json_response = response.json()
    if MESSAGE in json_response:
        message = json_response[MESSAGE]
        if message.find(BAD_CREDENTIALS_MESSAGE) != -1:
            sys.exit(BAD_CREDENTIALS_MESSAGE)
        elif message.find(RATE_LIMIT_EXCEEDED_MESSAGE) != -1:
            sys.exit(RATE_LIMIT_EXCEEDED_MESSAGE)
        elif message.find(NOT_FOUND_MESSAGE) != -1:
            sys.exit(url + " is " + NOT_FOUND_MESSAGE)
        elif message.find(ADMIN_RIGHTS_MESSAGE) != -1:
            sys.exit(ADMIN_RIGHTS_MESSAGE)
