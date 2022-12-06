from django.shortcuts import render, redirect
from login.models import Customer 
from login.forms import FormCustomer
from django.contrib import messages

# Create your views here.
def indexlogin(request):
    customer = Customer.objects.all()

    konteks = {
        'customer': customer,
    }

    return render(request, 'bukalogin.html')


def register(request):
        if request.POST:
            form = FormCustomer(request.POST)
            if form.is_valid():
                form.save()
                form = FormCustomer()
                pesan = "Data berhasil disimpan"

                konteks = {
                    'form': form,
                    'pesan': pesan,
                }
                return render(request, 'home.html', konteks)
            
        else: 

                form = FormCustomer()

                konteks = {
                'form' : form,
                }

        return render(request, 'register.html', konteks)
