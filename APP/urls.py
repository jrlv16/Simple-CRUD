from django.urls import path
from . import views

urlpatterns = [
    # path('contact', views.contact, name='contact'),
    path('', views.index),
    # path('<str:pagename>', views.index, name = 'index'),
    ]