import unittest
import warnings
import requests
from unittest.mock import patch
from io import StringIO
from vulnerability_checker import get_url_list, check_vulnerabilities

warnings.filterwarnings("ignore", category=ResourceWarning)

class TestGetUrlList(unittest.TestCase):
    def test_returns_list(self):
        session = requests.Session()
        url = "http://127.0.0.1"
        result = get_url_list(session, url)
        self.assertIsInstance(result, list)
    def test_returns_list1(self):
        session = requests.Session()
        url = "http://google.com"
        result = get_url_list(session, url)
        self.assertIsInstance(result, list)

class TestCheckVulnerabilities(unittest.TestCase):
    def test_no_vulnerabilities(self):
        session = requests.Session()
        url_list = ['/page1', '/page2', '/page3']
        host = "http://127.0.0.1"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            result = check_vulnerabilities(session, url_list, host)
        self.assertEqual(result, (0, 0, 0))
        self.assertEqual(fake_output.getvalue(), "")


if __name__ == '__main__':
    unittest.main()
