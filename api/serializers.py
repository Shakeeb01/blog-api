from rest_framework import serializers
from .models import BlogPost

# Our Serializers

class BlogPostSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()
    class Meta:
        model = BlogPost
        fields = ['id','title','content','published_date']