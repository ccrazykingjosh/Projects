from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'financeforkidsapp/homepage.html')

def quizzes(request):
    return render(request, 'financeforkidsapp/quizzes.html')

def quizone(request):
    return render(request, 'financeforkidsapp/quizone.html')

def quiztwo(request):
    return render(request, 'financeforkidsapp/quiztwo.html')

def quizthree(request):
    return render(request, 'financeforkidsapp/quizthree.html')

def funfacts(request):
    return render(request, 'financeforkidsapp/funfacts.html')

def millionairetest(request):
    return render(request, 'financeforkidsapp/millionairetest.html')

def resources(request):
    return render(request, 'financeforkidsapp/resources.html')
