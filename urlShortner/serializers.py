from rest_framework import serializers 
# import model from models.py 
from .models import ShortURL

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = "__all__"
