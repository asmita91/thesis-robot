from django.urls import path
from . import views

urlpatterns = [
    path('encode/', views.encode_faces, name='encode_faces'),
    path('recognize/', views.recognize_face, name='recognize_face'),
]
