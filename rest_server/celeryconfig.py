__author__ = "Gaurang Shah"
__version__ = "1.0.0"
__maintainer__ = "Gaurang Shah"
__email__ = "gaurangnshah@gmail.com"


# Celery configuration file
BROKER_URL = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = ''

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ENABLE_UTC = True

CELERY_IMPORTS = ("tasks.celery_tasks",)
