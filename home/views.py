from django.shortcuts import render
from home.models import Customer, Product, Order, OrderItem, ShippingAddress 

# Create your views here.
def indexhome(request):
    customer = Customer.objects.all()
    product = Product.objects.all()
    order = Order.objects.all()
    orderitem = OrderItem.objects.all()
    shippingaddress = ShippingAddress.objects.all()

    konteks = {
        'customer': customer,
        'product': product,
        'order': order,
        'orderitem': orderitem,
        'shippingaddress': shippingaddress,
    }

    return render(request, 'bukahome.html')