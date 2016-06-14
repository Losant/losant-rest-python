# pylint: disable=C0111,W0212,R0903,W0201,C0301,E0401
import unittest
import requests_mock
import json
import sys
from losantrest import Client, LosantError

if sys.version_info[0] == 3:
    from urllib.parse import urlparse, parse_qs
else:
    from urlparse import urlparse, parse_qs

class TestClient(unittest.TestCase):

    @requests_mock.Mocker()
    def test_basic_call_no_auth(self, mock):
        expected_body = {"token": "a token", "userId": "theUserId"}
        expected_qs = {"_links": ["true"], "_actions": ["false"], "_embedded": ["true"]}
        creds = {"email": "example@losant.com", "password": "qwerqwer"}
        mock.post("https://api.losant.com/auth/user", json=expected_body)

        resp = Client().auth.authenticate_user(credentials=creds)

        self.assertEqual(resp, expected_body)
        request = mock.request_history[0]
        parsed_url = urlparse(request.url)
        self.assertEqual(expected_qs, parse_qs(parsed_url.query))
        self.assertEqual(parsed_url.path, "/auth/user")
        self.assertEqual(parsed_url.path, "/auth/user")
        self.assertEqual(request.headers["Accept"], "application/json")
        self.assertEqual(request.headers["Content-Type"], "application/json")
        self.assertNotIn("Authorization", request.headers)
        self.assertEqual(json.loads(request.body), creds)

    @requests_mock.Mocker()
    def test_basic_call_with_auth(self, mock):
        expected_body = {"name": "Python Client Testing", "_type": "device", "applicationId": "anapp", "id": "adevice"}
        expected_qs = {"_links": ["true"], "_actions": ["false"], "_embedded": ["true"]}
        mock.get("https://api.losant.com/applications/anapp/devices/adevice", json=expected_body)

        resp = Client("a token").device.get(applicationId="anapp", deviceId="adevice")

        self.assertEqual(resp, expected_body)
        request = mock.request_history[0]
        parsed_url = urlparse(request.url)
        self.assertEqual(expected_qs, parse_qs(parsed_url.query))
        self.assertEqual(parsed_url.path, "/applications/anapp/devices/adevice")
        self.assertEqual(request.headers["Accept"], "application/json")
        self.assertEqual(request.headers["Authorization"], "Bearer a token")
        self.assertIsNone(request.body)

    @requests_mock.Mocker()
    def test_failure_call(self, mock):
        expected_body = {"message": "Unauthorized", "type": "Unauthorized"}
        expected_qs = {"_links": ["true"], "_actions": ["false"], "_embedded": ["true"]}
        mock.post("https://api.losant.com/auth/user", json=expected_body, status_code=401)
        creds = {"email": "example@losant.com", "password": "qwerqwer"}

        with self.assertRaises(LosantError) as cm:
            Client().auth.authenticate_user(credentials=creds)

        the_exception = cm.exception
        self.assertEqual(the_exception.status, 401)
        self.assertEqual(the_exception.data, expected_body)
        request = mock.request_history[0]
        parsed_url = urlparse(request.url)
        self.assertEqual(expected_qs, parse_qs(parsed_url.query))
        self.assertEqual(parsed_url.path, "/auth/user")
        self.assertEqual(request.headers["Accept"], "application/json")
        self.assertNotIn("Authorization", request.headers)
        self.assertEqual(json.loads(request.body), creds)

    @requests_mock.Mocker()
    def test_nested_query_param_call(self, mock):
        expected_body = {"count": 0, "items": []}
        expected_qs = {
            "_links": ["true"],
            "_actions": ["false"],
            "_embedded": ["true"],
            "tagFilter[0][key]": ["key2"],
            "tagFilter[1][value]": ["value1"],
            "tagFilter[1][key]": ["key1"],
            "tagFilter[2][value]": ["value2"]
        }
        mock.get("https://api.losant.com/applications/anapp/devices", json=expected_body)

        resp = Client("a token").devices.get(applicationId="anapp", tagFilter=[
            {"key": "key2"},
            {"key": "key1", "value": "value1"},
            {"value": "value2"},
        ])
        self.assertEqual(resp, expected_body)
        request = mock.request_history[0]
        parsed_url = urlparse(request.url)
        self.assertEqual(expected_qs, parse_qs(parsed_url.query))
        self.assertEqual(parsed_url.path, "/applications/anapp/devices")
        self.assertEqual(request.headers["Accept"], "application/json")
        self.assertEqual(request.headers["Authorization"], "Bearer a token")
        self.assertIsNone(request.body)
