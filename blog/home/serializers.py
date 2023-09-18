from rest_framework import serializers
from .models import Blog

class Blogserializer(serializers.Serializer):
    class Meta:
        model = Blog
        exclude = ['created_at','updated_at']
    
    def create(self, data):
        blog_data = Blog.objects.create(data)
        blog_data.save()