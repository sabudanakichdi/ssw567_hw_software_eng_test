from githubClient import GitHubCL as ghcl
from constants import USERNAME

class fetchUserDetailsServiceImpl():
    def __init__(self) -> None:
        pass

    def fetchUserRepos(self, username):
        print("User IN")
        try:
            if not username.strip():
               raise ValueError("Username cannot be null")
            responseList = ghcl.fetch_user_repo(username)
            reposList = []
            for repo in responseList:
                if(repo['name'].strip()):
                    reposList.append(repo['name'])
                else:
                    raise ValueError("Repo Name cannot be null. Username: %s" % (username))
            return self.fetchReposCommits(username, reposList)
        except ValueError as e:
            print(e)
            raise ValueError

    def fetchReposCommits(self, username, reposList):
        print("REPO IN")
        username = USERNAME if not username.strip() else username
        outputList = []
        try:
            if(len(reposList)>0):
                for repos in reposList:
                    responseList = ghcl.fetch_repo_commits(username,repos)
                    output = {
                              "Repo": repos, 
                              "Number of commits": len(responseList)
                              }
                    outputList.append(output)
            else:
                raise Exception("No Repos found for username: %s" % (USERNAME))
        except Exception as e:
            print(e)
        [print (output) for output in outputList]
        return outputList

if __name__ == "__main__":
    #fetchUserDetailsServiceImpl().fetchUserRepos(" ")
    fetchUserDetailsServiceImpl().fetchUserRepos("sabudanakichdi")
