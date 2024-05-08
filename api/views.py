
from rest_framework import generics
from .models import skills
from .serializers import  skillsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
# @permission_classes([IsAuthenticated])
class skillsListCreate(generics.ListCreateAPIView):
    
    queryset = skills.objects.all()
    serializer_class = skillsSerializer

class skillsRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = skills.objects.all()
    serializer_class = skillsSerializer
    lookup_field = "name"       
