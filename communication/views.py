from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NewsletterSubscription, ContactRequest
from .serializers import NewsletterSubscriptionSerializer, ContactRequestSerializer
from django.core.mail import send_mail
from rest_framework.throttling import ScopedRateThrottle

class SubscribeNewsletterView(APIView):
    throttle_scope = 'anon'
    throttle_classes = [ScopedRateThrottle]
    def post(self, request):
        serializer = NewsletterSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            subscriber=serializer.save()
            send_mail(
                subject='Newsletter Subscriber',
                message=f"Email: {subscriber.email}",
                from_email=subscriber.email,
                recipient_list=['kipitfresh@outlook.com']
            )
            return Response({"message": "Subscription successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactUsView(APIView):
    throttle_scope = 'anon'
    throttle_classes = [ScopedRateThrottle]
    def post(self, request):
        serializer = ContactRequestSerializer(data=request.data)
        if serializer.is_valid():
            contact_request = serializer.save()
            # Forward the contact request to an email
            send_mail(
                subject=contact_request.subject,
                message=f"Message from: {contact_request.email}\n\n{contact_request.message}",
                from_email=contact_request.email,
                recipient_list=['kipitfresh@outlook.com']
            )
            return Response({"message": "Contact request received"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
