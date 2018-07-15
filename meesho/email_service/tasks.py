from django.core.mail import send_mail


@shared_task
def send(*args):
	send_mail(*args)

