import requests
import re
import json


def get_response_user(your_username, my_token):
    """
    Wrapper around the function `requests.get()`.
    If my_token is supplied by me (i.e. it's not an empty string), then use authentication.
    Otherwise, go ahead without authentication.
    
    Args:
        your_username: the GitHub username of the user whose commits you want to count and sort by repository.
        my_token: your own GitHub personal access token for authentication. Authenticated requests get a higher hourly API rate limit.
    
    Returns:
        Response object for the GitHub user on the API.
    """
    if my_token:
        response_user = requests.get('https://api.github.com/users/%s' % your_username, headers={'Authorization': 'token %s' % my_token})
    else:
        response_user = requests.get('https://api.github.com/users/%s' % your_username)
    return response_user


def get_response_commits(commits_url, my_token):
    """
    Wrapper around the function `requests.get()`.
    If my_token is supplied by me (i.e. it's not an empty string), then use authentication.
    Otherwise, go ahead without authentication.
    
    Args:
        commits_url: URL with JSON metadata for commits.
        my_token: your own GitHub personal access token for authentication. Authenticated requests get a higher hourly API rate limit.
    
    Returns:
        Response object for no. of commits by the GitHub user on the API.
    """
    if my_token:
        response_commits = requests.get(commits_url, headers={'Authorization': 'token %s' % my_token})
    else:
        response_commits = requests.get(commits_url)
    return response_commits


def get_repo_commits(commits_url, your_username, my_token):
    """
    Gets no. of commits made by your_username to the respective default branch of a specific GitHub repository under commits_url.
    The necessary data is scraped from the GitHub API.
    
    Args:
        commits_url: URL with JSON metadata for commits.
        your_username: the GitHub username of the user whose commits you want to count and sort by repository.
        my_token: your own GitHub personal access token for authentication. Authenticated requests get a higher hourly API rate limit.
    
    Returns:
        Total no. of commits made by your_username to this GitHub repository.
    
    Throws:
        TypeError: Exception if GitHub repository is empty (i.e. no commits).
    """
    response_user = get_response_user(your_username, my_token)
    your_name = response_user.json()['name']
    
    page_idx = 1
    response_commits = get_response_commits(commits_url, my_token)
    commits = json.loads(response_commits.content)
    n_commits = 0
    try:
        while (len(commits) != 0):
            for commit in commits:
                author = commit['commit']['author']['name']
                if author == your_username or author == your_name or (commit['author'] is not None and commit['author']['login'] == your_username):
                    n_commits += 1
            commits_url = re.sub('\?page=%d' % page_idx, '?page=%d' % (page_idx+1), commits_url)
            page_idx += 1
            response_commits = get_response_commits(commits_url, my_token)
            commits = json.loads(response_commits.content)
    except TypeError:  # empty GitHub repo
        pass
    return n_commits
