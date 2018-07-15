from orders.models import Order, UserInfo as user
from celery import shared_task
from email_service.tasks import send_email

@shared_task
def send_invoice(order_id):
	order = Order.objects.get(id=order_id)
	html = """
	Order ID: {}
	Order Data: {}
	""".format(order.id)
	description = 'some data'
	user = order.user
	user_email = user.email
	send_email.delay(html, description, 'meesho@gmail.com', [user_email], fail_silently=False)
