from grpc import Status
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .models import Blog
from .serializers import BlogSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.throttling import ScopedRateThrottle


class LoginView(APIView):
    throttle_scope = 'login'
    throttle_classes = [ScopedRateThrottle]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Login successful!"
            })
        return Response({"message": "Invalid credentials"}, status=Status.HTTP_400_BAD_REQUEST)

class BlogListCreateView(generics.ListCreateAPIView):
    throttle_scope = 'user'
    throttle_classes = [ScopedRateThrottle]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    

    def perform_create(self, serializer):
        serializer.save()

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'user'
    throttle_classes = [ScopedRateThrottle]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            # Allow unauthenticated access for the retrieve action
            return [permissions.AllowAny()]
        else:
            # Require authentication for update and delete actions
            return [permissions.IsAuthenticated()]


class MakeFeaturedStoryView(APIView):
    throttle_scope = 'user'
    throttle_classes = [ScopedRateThrottle]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            blog.is_featured_story = True
            blog.save()
            return Response({"message": "Blog marked as featured story"})
        except Blog.DoesNotExist:
            return Response({"message": "Blog not found"}, status=404)

class FeaturedBlogsListView(generics.ListAPIView):
    throttle_scope = 'anon'
    throttle_classes = [ScopedRateThrottle]
    queryset = Blog.objects.filter(is_featured_story=True)
    serializer_class = BlogSerializer
    permission_classes = []
