## Aims

* To count the respective number of commits that any GitHub user has made to his/her **public** repositories, **excluding forked repositories**. The necessary data is scraped from the API of the GitHub webpage.
* To sort these repositories according to the number of commits made by said GitHub user.

## Methods

The main program in [`main.py`](https://github.com/liweiyap/SortingGitHubReposByCommits/blob/master/main.py) **must** take 3 arguments from the command line:
* `your_username`: the GitHub username of the user whose commits you want to count and sort by repository.
* `my_username`: your own GitHub username.
* `my_password`: your own GitHub password.

The latter two arguments are there only as a precaution; in case too many requests have been made for information from the GitHub API, GitHub will return the following error message: `API rate limit exceeded`. To circumvent this, we can use a simple digest authentication of our requests by providing our own GitHub username and password. This is because [authenticated requests get a higher rate limit](https://developer.github.com/v3/#rate-limiting).

## Python Dependencies

* [requests](https://github.com/psf/requests)
* [json](https://github.com/python/cpython/blob/3.8/Lib/json/__init__.py)
* [re](https://github.com/python/cpython/blob/3.8/Lib/re.py)
* [numpy](https://github.com/numpy/numpy)
* [pandas](https://github.com/pandas-dev/pandas)

## Running

To create a local copy of this repository, simply click 'Download'. Alternatively, clone it by first navigating to the path you want to store the local copy and then executing the following on the command line:
```
git clone https://github.com/liweiyap/SortingGitHubReposByCommits.git
```

Next, to run, simply execute the following in the root of the repository:
```
python main.py <your_username> <my_username> <my_password>
```
whilst filling in the desired/appropriate values for the 3 arguments.
