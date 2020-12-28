from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import encoder
# Create your views here.

@csrf_exempt
def Todo(request):
    print(request.POST)

    return JsonResponse({
        'status' : 'lk',
    }, encoder = encoder)

def index(request):
    context = {}
    return render(request, 'index.html', context)
