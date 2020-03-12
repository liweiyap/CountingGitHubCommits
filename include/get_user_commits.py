import pandas as pd
import numpy as np
from include.get_repo_commits import *


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
                commits_url = re.sub('{/sha}', '?page=1', repo['commits_url'])
                sub_df.loc[repo_idx,'Commits'] = get_repo_commits(commits_url, your_username, my_username, my_password)
                repo_idx += 1
        df = pd.concat([df, sub_df[0:repo_idx]])
        page_idx += 1
        response_repos = requests.get('https://api.github.com/users/%s/repos?page=%d' % (your_username,page_idx), auth=(my_username,my_password))
    return df.sort_values(by=['Commits'], ascending=False)
