from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meesho.settings')

app = Celery('meesho')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.update(
	CELERY_QUEUE=(
		Queue('default', routing_key='default'),
		Queue('email_service', routing_key='email_service'),
		Queue('invoice', routing_key='invoice')
		),
	CELERY_ROUTES=(
		'invoice.tasks.send_invoice': {
			'queue' : 'invoice',
			'routing_key' : 'invoice'
		},
		'email_service.tasks.send': {
			'queue' : 'email_service',
			'routing_key' : 'email_service'
		}
		)

	)



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

