import requests
import re
import json
import sys
import pandas as pd
import numpy as np


def get_user_commits(your_username, my_username, my_password):
    page_idx = 1
    response_repos = requests.get('https://api.github.com/users/%s/repos?page=%d' % (your_username,page_idx), auth=(my_username,my_password))
    df = pd.DataFrame(columns=['Name','Commits'], dtype=int)
    while (len(response_repos.json()) != 0):
        sub_df = pd.DataFrame(np.zeros([len(response_repos.json()),2]), columns=['Name','Commits'], dtype=int)
        repo_idx = 0
        for repo in response_repos.json():
            if not repo['fork']:
                sub_df.loc[repo_idx,'Name'] = repo['name']
                commits_url = re.sub('{/sha}', '', repo['commits_url'])
                sub_df.loc[repo_idx,'Commits'] = get_repo_commits(commits_url, my_username, my_password)
                repo_idx += 1
        df = pd.concat([df, sub_df[0:repo_idx]])
        page_idx += 1
        response_repos = requests.get('https://api.github.com/users/%s/repos?page=%d' % (your_username,page_idx), auth=(my_username,my_password))
    return df.sort_values(by=['Commits'], ascending=False)

def get_repo_commits(commits_url, my_username, my_password):
    response_commits = requests.get(commits_url, auth=(my_username, my_password))
    commits = json.loads(response_commits.content)
    n_commits = len(commits)
    if response_commits.headers.get('link'):
        next_commits_url = get_next_commits_url(response_commits)
        if next_commits_url:
            n_commits += get_repo_commits(next_commits_url, my_username, my_password)
    return n_commits

def get_next_commits_url(response_commits):
    links = response_commits.headers['link']
    for link in links.split(','):
        link_next, link_last = link.split(';')
        if link_last.strip() == 'rel="next"':
            return link_next.strip()[1:-1]  # remove '<' and '>'

def main():
    try:
        if (len(sys.argv) > 4):
            print("WARNING: Only three arguments needed: your_username, my_username, and my_password.")
        df = get_user_commits(sys.argv[1], sys.argv[2], sys.argv[3])
        print(df.to_string(index=False))
        print("\nTotal repositories:", len(df.index))
        print("Total commits:", df['Commits'].sum())
    except IndexError:
        print("ERROR: Check that there are exactly three arguments: your_username, my_username, and my_password.")
    except TypeError:
        print("ERROR: Check that the three arguments (your_username, my_username, and my_password) do not contain any typos.")

#-------------------------#

if __name__ == "__main__":
    main()