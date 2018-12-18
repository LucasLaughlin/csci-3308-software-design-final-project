import unittest
from selenium import webdriver
import requests

class BasicTest(unittest.TestCase):
    def setUp(self):

        # Username and authey below
        self.username = "chhi5098@colorado.edu"
        self.authkey  = "uf33c324018390c0"

        self.api_session = requests.Session()
        self.api_session.auth = (self.username,self.authkey)

        self.test_result = None

        caps = {}
        
        caps['name'] = 'Basic Test Example'
        caps['build'] = '1.0'
        caps['browserName'] = 'Chrome'
        caps['version'] = '61x64'
        caps['platform'] = 'Windows 7 64-Bit'
        caps['screenResolution'] = '1366x768'

        # start the remote browser on crossbrowsertesting server
        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username,self.authkey)
        )

        self.driver.implicitly_wait(20)

    def test_CBT(self):
        # We wrap this all in a try/except so we can set pass/fail at the end
        try:
            # load the page url
            print('Loading Url')
            self.driver.get('http://10.201.64.35/cgi-bin/webgui2.py')

            # maximize the window - DESKTOPS ONLY
            #print('Maximizing window')
            #self.driver.maximize_window()
            
            #check the title
            print('Checking title')
            self.assertEqual("", self.driver.title)

            # if we are still in the try block after all of our assertions that 
            # means our test has had no failures, so we set the status to "pass"
            self.test_result = 'pass'

        except AssertionError as e:

            # if any assertions are false, we take a snapshot of the screen, log 
            # the error message, and set the score to "during tearDown()".

            snapshot_hash = self.api_session.post('https://crossbrowsertesting.com/api/v3/selenium/' + self.driver.session_id + '/snapshots').json()['hash']
            self.api_session.put('https://crossbrowsertesting.com/api/v3/selenium/' + self.driver.session_id + '/snapshots/' + snapshot_hash,
                data={'description':"AssertionError: " + str(e)})
            self.test_result = 'fail'
            raise

    def tearDown(self):
        print("Done with session %s" % self.driver.session_id)
        self.driver.quit()
        # Here we make the api call to set the test's score.
        # Pass it it passes, fail if an assertion fails, unset if the test didn't finish
        if self.test_result is not None:
            self.api_session.put('https://crossbrowsertesting.com/api/v3/selenium/' + self.driver.session_id, 
                data={'action':'set_score', 'score':self.test_result})


if __name__ == '__main__':
    unittest.main()