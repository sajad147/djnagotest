from django.shortcuts import render
from django.core.mail import send_mail
def home(request):
    return render(request, 'home.html', {'address': 'isfahan' , 'email':'sajad147@outlook.com'})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(message_name,message,message_email,['sajad_games@yahoo.com'],fail_silently=False)
        return render(request, 'contact.html', {'message':'Message Sent!'})
    else:
        return render(request, 'contact.html')