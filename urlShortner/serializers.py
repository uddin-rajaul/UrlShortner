from rest_framework import serializers 
# import model from models.py 
from .models import Urlshortner

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urlshortner
        fields = "__all__"
