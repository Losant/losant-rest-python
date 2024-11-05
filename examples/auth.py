from platformrest import Client
client = Client()


user_response = client.auth.authenticate_user(credentials={
    'email': 'example@losant.com',
    'password': 'your_password'
})

print(user_response)
""" Example user result
{
    'token': 'an auth token string',
    'userId': 'theUserId'
}
"""


device_response = client.auth.authenticate_device(credentials={
    'deviceId': 'myDeviceId',
    'key': 'my_app_access_key',
    'secret': 'my_app_access_secret'
})

print(device_response)
""" Example device result
{
    'applicationId': 'myAppId',
    'token': 'an auth token string',
    'restricted': False,
    'deviceId': 'myDeviceId',
    'deviceClass': 'standalone'
}
"""
