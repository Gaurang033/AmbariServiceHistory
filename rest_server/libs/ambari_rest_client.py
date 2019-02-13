from celery import Celery
import db_utils
from rest_server import config
from requests.auth import HTTPBasicAuth
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

__author__ = "Gaurang Shah"
__version__ = "1.0.0"
__maintainer__ = "Gaurang Shah"
__email__ = "gaurangnshah@gmail.com"


app = Celery()
AMBARI_CONFIG = config.AMBARI_CONFIG
auth = HTTPBasicAuth(AMBARI_CONFIG.get('username'), AMBARI_CONFIG.get('password'))
url = AMBARI_CONFIG.get('url')


def _get_status(status):
    # status.get('MAINTENANCE') >= 1 or status.get('UNKNOWN') >= 1 or
    if status.get('CRITICAL') >= 1 or status.get('WARNING') >= 1:
        return '0'
    else:
        return '1'


def get_services():
    s = requests.session()
    resp = s.get(url=url,
                 auth=auth,
                 verify=False)
    data = resp.json()
    return [uri.get('href') for uri in data.get('items')]


def get_status(service_uri):
    s = requests.session()
    resp = s.get(service_uri,
                 auth=auth,
                 verify=False)

    if resp.status_code == 200:
        service_name = resp.json().get('ServiceInfo').get('service_name')
        status = resp.json().get('alerts_summary')
        return {'service_name': service_name, 'status': _get_status(status)}
    return 'NotReachable'


def get_status_for_all_services():
    service_uris = get_services()
    for service_uri in service_uris:
        yield get_status(service_uri)


def store_status():
    for status in get_status_for_all_services():
        db_utils.update_table(status)


if __name__ == '__main__':
    store_status()
