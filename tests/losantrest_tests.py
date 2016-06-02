# pylint: disable=C0111,W0212,R0903,W0201,C0301,E0401
import unittest
import requests_mock
import json
import re
from losantrest import Client, LosantError

class TestClient(unittest.TestCase):

    @requests_mock.Mocker()
    def test_basic_call_no_auth(self, mock):
        expected_body = {"token": "a token", "userId": "theUserId"}
        creds = {"email": "example@losant.com", "password": "qwerqwer"}
        mock.post("https://api.losant.com/auth/user", json=expected_body)

        resp = Client().auth.authenticate_user(credentials=creds)

        self.assertEqual(resp, expected_body)
        request = mock.request_history[0]
        self.assertEqual(request.headers["Accept"], "application/json")
        self.assertNotIn("Authorization", request.headers)
        self.assertTrue(re.search(r"^https://api.losant.com/auth/user\?", request.url))
        self.assertEqual(json.loads(request.body), creds)

    @requests_mock.Mocker()
    def test_basic_call_with_auth(self, mock):
        expected_body = {"name": "Python Client Testing", "_type": "device", "applicationId": "anapp", "id": "adevice"}
        mock.get("https://api.losant.com/applications/anapp/devices/adevice", json=expected_body)

        resp = Client("a token").device.get(applicationId="anapp", deviceId="adevice")

        self.assertEqual(resp, expected_body)
        request = mock.request_history[0]
        self.assertEqual(request.headers["Accept"], "application/json")
        self.assertEqual(request.headers["Authorization"], "Bearer a token")
        self.assertTrue(re.search(r"^https://api.losant.com/applications/anapp/devices/adevice\?", request.url))
        self.assertIsNone(request.body)

    @requests_mock.Mocker()
    def test_failure_call(self, mock):
        expected_body = {"message": "Unauthorized", "type": "Unauthorized"}
        mock.post("https://api.losant.com/auth/user", json=expected_body, status_code=401)
        creds = {"email": "example@losant.com", "password": "qwerqwer"}

        with self.assertRaises(LosantError) as cm:
            Client().auth.authenticate_user(credentials=creds)

        the_exception = cm.exception
        self.assertEqual(the_exception.status, 401)
        self.assertEqual(the_exception.data, expected_body)
