import os

__author__ = "Gaurang Shah"
__version__ = "1.0.0"
__maintainer__ = "Gaurang Shah"
__email__ = "gaurangnshah@gmail.com"

local = {
    "username": "raj_ops",
    "password": "raj_ops",
    "url": "http://localhost:8080/api/v1/clusters/Sandbox/services/"
}
dev = {
    "username": "",
    "password": "",
    "url": "http://localhost:8080/api/v1/clusters/Sandbox/services/"
}


prod = {
    "username": "",
    "password": "",
    "url": "http://localhost:8080/api/v1/clusters/Sandbox/services/"
}

fetch_interval = 60

ENVIRONMENT = os.getenv("HADOOP_ENV", 'PROD')
if ENVIRONMENT == "DEV":
    AMBARI_CONFIG = dev
else:
    AMBARI_CONFIG = prod
