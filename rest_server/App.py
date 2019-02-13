__author__ = "Gaurang Shah"
__version__ = "1.0.0"
__maintainer__ = "Gaurang Shah"
__email__ = "gaurangnshah@gmail.com"

from celery import Celery
from flask import Flask, jsonify
from flask_cors import CORS
from libs import db_utils
import config

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])

celery.conf.beat_schedule = {
    'add-every-few-seconds': {
        'task': 'tasks.celery_tasks.store_ambari_service_status_to_db',
        'schedule': config.fetch_interval,
    },
}
CELERY_IMPORTS = ("tasks",)
celery.conf.update(app.config)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/api/all_services")
def home():
    return jsonify(db_utils.get_status_data()), 200, {'Access-Control-Allow-Origin': '*'}


if __name__ == '__main__':
    app.run("0.0.0.0", 5005, debug=True)
