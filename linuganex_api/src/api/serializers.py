from rest_framework import serializers
from .models import Application


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('title', 'publisher',"publishedYear", 'email')
