from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
def home(request):
    if request.method=="POST":
        name=request.POST['name']
        message=request.POST['message']
        Email=request.POST['Email']
        send_mail(
            'Contact Form',
            message,
            'settings.EMAIL_HOST_USER',
            [Email],
            fail_silently=False
        )
    return render(request,'index.html')     
        
      
        
         
       
            
       
    		

		   
       
        
    		
        
   

# Create your views here.
