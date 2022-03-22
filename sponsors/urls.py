from django.urls import path
from sponsors import views

urlpatterns = [
    path('', views.hello, name='hello')
]
