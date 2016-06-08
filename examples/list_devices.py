from losantrest import Client

client = Client('my_token')
result = client.devices.get(applicationId='myAppId')

print(result)

""" Example result
{
    'page': 0,
    'sortField': 'name',
    '_type': 'devices',
    'totalCount': 1,
    '_links': {
        'self': { 'href': '/applications/myAppId/devices' },
        'application': { 'href': '/applications/myAppId' }
    },
    'perPage': 100,
    'count': 1,
    'applicationId': 'myAppId',
    'items': [{
        'deviceClass': 'standalone',
        '_type': 'device',
        'connectionInfo': { 'connected': 0, 'time': '2016-06-01T17:16:02.324Z' },
        '_links': {
            'devices': {'href': '/applications/myAppId/devices' },
            'self': { 'href': '/applications/myAppId/devices/myDevId' },
            'application': { 'href': '/applications/myAppId' }
        },
        'attributes': [
            { 'name': 'voltage', 'dataType': 'number' },
            { 'name': 'isOn', 'dataType': 'boolean' }
        ],
        'tags': [],
        'name': 'Python Client Testing',
        'lastUpdated': '2016-05-31T14:47:32.288Z',
        'id': 'myDevId',
        'deviceId': 'myDevId',
        '_etag': '"174-u7/3je4oFyaKGePPbcelww"',
        'description': '',
        'creationDate': '2016-01-31T17:58:57.541Z',
        'applicationId': 'myAppId'
    }],
    'sortDirection': 'asc'
}
"""
