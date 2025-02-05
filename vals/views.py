from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import Customer
from .utils import send_yes_email, send_message_back
# Create your views here.



def main_page(request):
    return render(request, "old.html")


@csrf_protect
def main_detail(request, id):
    customer = Customer.objects.filter(id=id).first()
    
    if not customer: 
        return HttpResponse("Bad Request")
    
    if request.method == "POST":
        user_email = request.POST.get("user_email")
        # msg = request.POST.get("msg")

        context = {"name": customer.name, "main_message": customer.message_to_lover}

        send_yes_email(user_email, context)
        messages.success(request, "A surprise message has been sent to your email")
        
        # if not msg or msg == "": # not empty string
        #     send_yes_email(user_email, context)
        #     messages.success(request, "Check your email for a surprise.")
        
        # context.update({"text_message": msg})
        # send_yes_email(user_email, context)
        # send_message_back(customer.email, context)
        # messages.success(request, "Your mail has been sent and check your email for a surprise.")

        return render(request, "old.html", context)
    
    return render(request, "old.html")
    
    