import unittest as u
from fetchUserDetailsService import fetchUserDetailsServiceImpl as user

class TestFetchUserDetailsService(u.TestCase):
    def testFetchUserRepos(self):
        self.assertEquals(len(user().fetchUserRepos('sabudanakichdi')),9)
        print('testFetchUserRepos successful')

    def testFetchUserReposBlankValue(self):
        with self.assertRaises(ValueError):
            user().fetchUserRepos(' ')
        print('testFetchUserReposBlankValue successful')

if __name__ == "__main__":
    u.main()