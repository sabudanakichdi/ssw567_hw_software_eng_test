from http.client import HTTPException
import requests
import json
from constants import GITHUB_URL,USERS,REPOS,SLASH,COMMITS

class GitHubCL():

    def fetch_user_repo(username):
        fetch_repos_url = GITHUB_URL + USERS + SLASH + username + REPOS
        try:
            response = requests.get(fetch_repos_url)
            if(response.status_code != 200):
                raise HTTPException("Failed Request Error code: %s, Message: %s" % (response.status_code, response.json()))
            #print(response.status_code)
            #print(response.json())
            return json.loads(json.dumps(response.json()))
        except HTTPException as h:
            print(h)
            return HTTPException
        except Exception as e:
            print(e)
            return Exception

    def fetch_repo_commits(username,repos):
        fetch_commits_repos = GITHUB_URL + REPOS + SLASH + username + SLASH + repos + COMMITS
        try:
            response = requests.get(fetch_commits_repos)
            if(response.status_code != 200):
                raise HTTPException("Failed Request Error code: %s, Message: %s" % (response.status_code, response.json()))
            #print(response.status_code)
            #print(response.json())
            return json.loads(json.dumps(response.json()))
        except HTTPException as h:
            print(h)

