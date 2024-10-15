from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stocklist/', views.stocklist, name='stocklist'),
    path('stockprofile/', views.stockprofile, name='stockprofile'),
    path('testinput/', views.testinput, name='testinput'),
    path('testoutput/', views.testoutput, name='testoutput'),
    path('printurl/', views.printurl),
    path('companyprofile/', views.companyprofile, name='companyprofile'),
    path('predictionoutput/', views.predictionoutput, name='predictionoutput'),
]