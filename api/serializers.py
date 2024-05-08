from rest_framework import serializers
from .models import  skills

class skillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = skills
        fields = ["name","content","video"]

        extra_kwargs = {
            'name': {'required': True},
            'content': {'required': True},
            'video': {'required': True}
                        } 

