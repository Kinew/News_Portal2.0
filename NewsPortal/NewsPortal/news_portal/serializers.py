from .models import *
from rest_framework import serializers

class NewsSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = News
       fields = ['id', 'name', ]


class PostSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Post
       fields = ['id', 'grade', ]