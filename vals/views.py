from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Customer
from .utils import send_yes_email
# Create your views here.



def main_page(request):
    return render(request, "main.html")


@csrf_protect
def main_detail(request, id):
    customer = Customer.objects.filter(id=id).first()
    
    if not customer: 
        return HttpResponse("Bad Request")
    
    if request.method == "POST":
        message = request.POST.get("msg")

        context = {"name": customer.name, "message": message}

        send_yes_email(customer.email, context)

        return render(request, "main.html", context)
    
    return render(request, "main.html")
    
    