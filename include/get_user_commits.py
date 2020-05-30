import pandas as pd
import numpy as np
from include.get_repo_commits import requests, re, get_repo_commits
from include.display_curl_headers import *


def get_response_repos(your_username, my_token, page_idx):
    if my_token:
        response_repos = requests.get('https://api.github.com/users/%s/repos?page=%d' % (your_username,page_idx), headers={'Authorization': 'token %s' % my_token})
    else:
        response_repos = requests.get('https://api.github.com/users/%s/repos?page=%d' % (your_username,page_idx))
    return response_repos

def get_user_commits(your_username, my_token=""):
    """
    Gets no. of commits made by your_username to the respective default branch of his/her public, non-forked GitHub repositories.
    The necessary data is scraped from the GitHub API.
    
    Args:
        your_username: the GitHub username of the user whose commits you want to count and sort by repository.
        my_token: your own GitHub personal access token for authentication. Authenticated requests get a higher hourly API rate limit.
    
    Returns:
        Pandas dataframe of repositories sorted by no. of commits.
    
    Throws:
        TypeError: Exception if typo in command-line arguments / GitHub user has no repositories / my hourly API rate limit is exceeded.
    """
    page_idx = 1
    response_repos = get_response_repos(your_username, my_token, page_idx)
    df = pd.DataFrame(columns=['Name','Commits'], dtype=int)
    try:
        while (len(response_repos.json()) != 0):
            sub_df = pd.DataFrame(np.zeros([len(response_repos.json()),2]), columns=['Name','Commits'], dtype=int)
            repo_idx = 0
            for repo in response_repos.json():
                if not repo['fork']:
                    sub_df.loc[repo_idx,'Name'] = repo['name']
                    commits_url = re.sub('{/sha}', '?page=1', repo['commits_url'])
                    sub_df.loc[repo_idx,'Commits'] = get_repo_commits(commits_url, your_username, my_token)
                    repo_idx += 1
            df = pd.concat([df, sub_df[0:repo_idx]])
            page_idx += 1
            response_repos = get_response_repos(your_username, my_token, page_idx)
    except TypeError:
        print("ERROR: Check that the two arguments (your_username and my_token) do not contain any typos. Also, check that the GitHub user has repositories, and that you have not exceeded the hourly API rate limit:")
        crl = pycurl.Curl()
        crl.setopt(crl.URL, 'https://api.github.com')
        crl.setopt(crl.HEADERFUNCTION, display_curl_headers)
        if my_token:
            crl.setopt(pycurl.HTTPHEADER, ["Authorization: token %s" % my_token])
        crl.perform()
        print(curl_headers)
    return df.sort_values(by=['Commits'], ascending=False)
