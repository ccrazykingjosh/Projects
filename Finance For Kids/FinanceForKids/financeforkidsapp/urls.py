from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('quizzes', views.quizzes, name='quizzes'),
    path('quizone',views.quizone, name='quizone'),
    path('quiztwo',views.quiztwo, name='quiztwo'),
    path('quizthree',views.quizthree, name='quizthree'),
    path('funfacts', views.funfacts, name='funfacts'),
    path('millionairetest', views.millionairetest, name='millionairetest'),
    path('resources', views.resources, name='resources'),

]
