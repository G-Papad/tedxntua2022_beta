from django.urls import path
from about import views

urlpatterns = [
    path('', views.hello2, name='hello2')
]
