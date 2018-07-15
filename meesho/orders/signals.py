from django.db.models.signals import post_save
from sms import tasks as sms_tasks
from notification import tasks as notification_tasks
from invoice import tasks as invoice_tasks
from .models import Order


@receiver(post_save, sender=Order, dispatch_uid="update_stock_count")
def post_save_order(sender, instance, **kwargs):
	order = instance
	sms_tasks.send_sms.delay(order.id)
	notification_tasks.send_notification.delay(order.id)
	invoice_tasks.send_invoice.delay(order.id)

