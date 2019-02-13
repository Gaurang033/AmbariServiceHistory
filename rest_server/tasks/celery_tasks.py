from App import celery

__author__ = "Gaurang Shah"
__version__ = "1.0.0"
__maintainer__ = "Gaurang Shah"
__email__ = "gaurangnshah@gmail.com"

from libs import ambari_rest_client


@celery.task
def store_ambari_service_status_to_db():
    ambari_rest_client.store_status()
