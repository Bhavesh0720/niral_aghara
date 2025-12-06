
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('cources', views.cources, name='cources'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('terms', views.terms, name='terms'),
    path('youtube', views.youtube, name='youtube'),
]
