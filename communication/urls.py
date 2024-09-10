from django.urls import path
from .views import SubscribeNewsletterView, ContactUsView

urlpatterns = [
    path('newsletter/subscribe/', SubscribeNewsletterView.as_view(), name='subscribe-newsletter'),
    path('contact/', ContactUsView.as_view(), name='contact-us'),
]
