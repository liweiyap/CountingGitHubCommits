## Aims

* To count the respective number of commits that any GitHub user has made to the respective default branch of his/her **public** repositories, **excluding forked repositories**. The necessary data is scraped from the [API](https://api.github.com/) of the GitHub webpage.
* To sort these repositories according to the number of commits made by said GitHub user.

## Methods

The main program in [`main.py`](https://github.com/liweiyap/SortingGitHubReposByCommits/blob/master/main.py) takes 2 arguments from the command line:
* `your_username` **(mandatory)**: the GitHub username of the user whose commits you want to count and sort by repository.
* `my_token` **(optional but recommended)**: your own GitHub personal access token.

The latter argument is there only as a precaution; in case too many requests have been made for information from the GitHub API in the past hour, GitHub will return the following error message: `API rate limit exceeded`. To circumvent this, we can use a simple digest authentication of our requests by providing our own GitHub personal access token. This is because [authenticated requests have a higher hourly rate limit](https://developer.github.com/v3/#rate-limiting).

## Python Dependencies

* [requests](https://github.com/psf/requests)
* [json](https://github.com/python/cpython/blob/3.8/Lib/json/__init__.py)
* [re](https://github.com/python/cpython/blob/3.8/Lib/re.py)
* [pandas](https://github.com/pandas-dev/pandas)
* [numpy](https://github.com/numpy/numpy)
* [pycurl](https://github.com/pycurl/pycurl)

## Running

To create a local copy of this repository, clone it by first navigating to the path you want to store the local copy and then executing the following on the command line:
```
git clone https://github.com/liweiyap/SortingGitHubReposByCommits.git
```

[`run_main.sh`](https://github.com/liweiyap/SortingGitHubReposByCommits/blob/master/run_main.sh) is a Bash script that wraps around the running of [`main.py`](https://github.com/liweiyap/SortingGitHubReposByCommits/blob/master/main.py) on the command line. Optionally, follow the instructions in [this link](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) to generate your own personal access token (if you haven't already done so). Then, open up [`run_main.sh`](https://github.com/liweiyap/SortingGitHubReposByCommits/blob/master/run_main.sh) and set the `MY_TOKEN` variable to your generated token.

Next, to run, simply execute the following **in the root of the repository**:
```
./run_main.sh <your_username>
```
whilst filling in the desired/appropriate value for the `your_username` argument. The output will be printed on the command line as a [Pandas](https://github.com/pandas-dev/pandas) dataframe.

## Tests

I have tested the code with 40 of the GitHub users whom I am following.

For example, when running `./run_main.sh liweiyap`, the following output is obtained:
```
                               Name  Commits
                 LeetCode_Solutions       92
                 liweiyap.github.io       60
                  Conway_GameOfLife       53
 HackerRank-InterviewPreparationKit       43
                              MyCPU       40
                     ProteinFolding       34
          DataStructures_Algorithms       26
        SortingGitHubReposByCommits       23
                                PvZ       22
                      metawear-impl       21
   VectorMatrixElementaryOperations        5

Total repositories: 11
Total commits: 419
```
