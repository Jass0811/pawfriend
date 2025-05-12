from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import NewsletterSubscriptionForm
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        
        # Validate email format
        if not validate_email(email):
            messages.error(request, 'Please enter a valid email address.')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            
            # Send confirmation email
            subject = 'Welcome to Perfect Pawfriend Newsletter!'
            message = f'''Dear Subscriber,

Thank you for subscribing to Perfect Pawfriend's newsletter! We're excited to have you join our community of pet lovers.

You'll receive updates about:
- New pets available for adoption
- Pet care tips and advice
- Success stories
- Special events and promotions

If you wish to unsubscribe at any time, please click the unsubscribe link in our emails.

Best regards,
The Perfect Pawfriend Team'''
            
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for subscribing! Please check your email for confirmation.')
            except Exception as e:
                messages.warning(request, 'Subscription successful, but we could not send the confirmation email. Please check your email address.')
            
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            if 'email' in form.errors:
                messages.error(request, 'This email is already subscribed to our newsletter.')
            else:
                messages.error(request, 'There was an error processing your subscription. Please try again.')
    return redirect(request.META.get('HTTP_REFERER', '/'))
