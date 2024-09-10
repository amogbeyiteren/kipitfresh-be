# admin.py

from django.contrib import admin
from .models import NewsletterSubscription, ContactRequest

admin.site.register(NewsletterSubscription)
admin.site.register(ContactRequest)
