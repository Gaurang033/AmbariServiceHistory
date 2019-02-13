celery worker -A App.celery  --config=celeryconfig -B --concurrency=1 --loglevel=ERROR -f ambari_service_status.log --detach 
