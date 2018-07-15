from django.shortcuts import render
from .models import Order, Product

# Create your views here.



def place_order(request):
	product_ids = request.PUT['product_ids']
	products = Product.objects.filter(id__in=product_ids)

	order = Order()
	order.save()
	order.products.add(*products)
	return HttpResponse(status=200)
