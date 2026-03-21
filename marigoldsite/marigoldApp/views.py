from django.shortcuts import render,redirect

from .forms import ContactForm
from .models import FAQ, Product, Review
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.
def home(request):
    featured = Product.objects.filter(is_active=True, is_featured=True)[:3]
    reviews  = Review.objects.filter(is_approved=True)[:3]
    return render(request, 'index.html', {'featured': featured, 'reviews': reviews})


def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            try:
                email_subject = 'Welcome to Marigold & Co. 🌻'
                email_body = f'Hi {email},\n\nThank you for subscribing to the Marigold & Co. newsletter!\n\nYou\'ll be the first to hear about new scents, seasonal collections, and behind-the-scenes updates.\n\nWith love,\nSandra\nMarigold & Co.'
                email_message = EmailMessage(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                )
                email_message.send()
                messages.success(request, "You're subscribed! Check your inbox.")
            except Exception as e:
                messages.error(request, "Something went wrong. Please try again.")
    return redirect('home')

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! Your message has been sent.")
            return redirect('contact')  

    return render(request, 'contact.html', {'form': form})

def shop(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'shop.html', {'products': products})

def faq(request):
    faqs = FAQ.objects.filter(is_active=True)
    return render(request, 'faq.html',{'faqs':faqs})