import requests
import pytest

def test_request():
    r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    assert r.status_code == 200