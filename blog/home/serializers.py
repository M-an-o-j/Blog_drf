from rest_framework import serializers
from .models import Blog

class Blogserializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ['created_at','updated_at']
    
    # def create(self, data):
    #     blog_data = Blog.objects.create(
    #         title = data['title'],
    #         blog_text = data['blog_text'],
    #         main_image = data['main_image']
    #     )
    #     blog_data.save()

    #     return data