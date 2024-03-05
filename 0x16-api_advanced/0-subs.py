#!/usr/bin/python3
'''queries and returns corresponding result from the Reddit API'''
import requests

def number_of_subscribers(subreddit):
    '''
    Description:
    - queries and returns the number of subscribers
      (not active users, total subscribers) for a given subreddit.
    - returns 0 if an invalid subreddit is given
    '''
    endpoint = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    
    try:
        res = requests.get(endpoint, headers=headers)
        res.raise_for_status()  # Raise an exception for HTTP errors
        data = res.json()
        return data['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
        return 0
    except KeyError as ke:
        print("KeyError:", ke)
        return 0
    return res.json()['data']['subscribers']
