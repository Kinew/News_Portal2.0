from .models import *
from rest_framework import serializers

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = News
       fields = ['id', 'name', ]


class SClassSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = articles
       fields = ['id', 'grade', ]