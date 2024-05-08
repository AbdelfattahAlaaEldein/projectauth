from django.urls import path
from . import views

urlpatterns=[
    
    path("skills/", views.skillsListCreate.as_view(), name="skills"),
    path("skills/<str:name>/", views.skillsRetrieveUpdateDestory.as_view(), name="SkillsName"),
]