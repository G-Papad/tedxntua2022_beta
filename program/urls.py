from django.urls import path
from program import views

urlpatterns = [
    path('', views.hello, name='hello')
]