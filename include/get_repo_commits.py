import requests
import re
import json


def get_repo_commits(commits_url, your_username, my_username, my_password):
    response_user = requests.get('https://api.github.com/users/%s' % your_username, auth=(my_username,my_password))
    your_name = response_user.json()['name']
    
    page_idx = 1
    response_commits = requests.get(commits_url, auth=(my_username, my_password))
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
            response_commits = requests.get(commits_url, auth=(my_username, my_password))
            commits = json.loads(response_commits.content)
    except TypeError:  # empty GitHub repo
        pass
    return n_commits
