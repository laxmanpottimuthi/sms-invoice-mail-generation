from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'

    def ready(sefl):
    	import orders.signals
