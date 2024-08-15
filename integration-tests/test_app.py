#!/usr/bin/env python

import unittest
import os
import requests
import re
import time


class TestName(unittest.TestCase):
    frontend_url = os.getenv('FRONTEND_URL', 'http://127.0.0.1:8080')
    backend_url = os.getenv('BACKEND_URL', 'http://127.0.0.1:9000')
    time.sleep(10)
    def test_frontend_status(self):
        url = self.frontend_url + "/healthz"
        response = requests.get(url, timeout=1)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(re.match('healthy', response.text))

    # not really integration test, but just to have an extra test
    def test_backend_status(self):
        url = self.backend_url + "/fortunes"
        response = requests.get(url, timeout=1)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.text) > 0)


if __name__ == '__main__':
    print("Starting test run!", flush=True)
    unittest.main()
