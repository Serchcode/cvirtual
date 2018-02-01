from ..models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','post_img', 'post_title', 'post_content','post_date','slug')