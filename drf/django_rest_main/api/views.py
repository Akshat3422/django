from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def StudentView(request):
    students={
        'id':1,
        'name':'Rathan',
        'class':2
    }
    return JsonResponse(students)
