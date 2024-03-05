#!/usr/bin/python3
'''queries and returns corresponding result from the Reddit API'''
import requests
import time

def number_of_subscribers(subreddit):
    '''
    Description:
    - Queries and returns the number of subscribers
      (not active users, total subscribers) for a given subreddit.
    - Returns 0 if an invalid subreddit is given or if an error occurs.
    '''
    endpoint = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Your Unique User Agent 1.0'}
    
    try:
        # Introduce a delay to avoid hitting rate limits
        time.sleep(1)  # Sleep for 1 second between requests
        
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

if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name: ")
    subscribers = number_of_subscribers(subreddit_name)
    print(f"The number of subscribers in r/{subreddit_name} is: {subscribers}")

