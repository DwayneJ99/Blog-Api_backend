from .models import Blog
from rest_framework import viewsets, permissions
from .serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permissions_classes = [permissions.AllowAny]
