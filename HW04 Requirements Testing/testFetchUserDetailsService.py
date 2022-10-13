import unittest as u
import json
from unittest.mock import Mock, patch
from fetchUserDetailsService import fetchUserDetailsServiceImpl as user
from githubClient import GitHubCL as repo_Call

class TestFetchUserDetailsService(u.TestCase):
    def test_fetch_user_repos(self):
        self.assertEqual(len(user().fetchUserRepos('sabudanakichdi')),9)
        print('testFetchUserRepos successful')

    def test_fetch_user_repos_blank_value(self):
        with self.assertRaises(ValueError):
            user().fetchUserRepos(' ')
        print('testFetchUserReposBlankValue successful')

    #Mock fetch user api
    @patch.object(repo_Call, "fetch_user_repo")
    def test_fetch_user_repo_mock_api(self, mock_fetch_user_repo):
        response_file = open('./json/response_fetch_user_repo.json')        
        repo_call_response = json.load(response_file)
        mock_fetch_user_repo.return_value = Mock(status_code = 200)
        mock_fetch_user_repo.return_value = json.loads(json.dumps(repo_call_response))
        response = repo_Call.fetch_user_repo('sabudanakichdi')
        #print(response)
        self.assertEqual(response[0]['name'],"chatbot_ner")
        response_file.close()

    #Mock fetch commit api
    @patch.object(repo_Call, "fetch_repo_commits")
    def test_fetch_repo_commits_mock_api(self, mock_fetch_user_repo):
        response_file = open('./json/response_fetch_repo_commits.json')        
        repo_call_response = json.load(response_file)
        mock_fetch_user_repo.return_value = Mock(status_code = 200)
        mock_fetch_user_repo.return_value = json.loads(json.dumps(repo_call_response))
        response = repo_Call.fetch_repo_commits('sabudanakichdi', ['ssw567_hw_software_eng_test'])
        #print(response)
        self.assertEqual(len(response),30)
        response_file.close()

if __name__ == "__main__":
    u.main()