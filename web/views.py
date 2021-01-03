from datetime import datetime
from json import JSONEncoder

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from web.models import Todos

# Create your views here.


# status = (ok and no)
@csrf_exempt
def postTodo(request):
    """ submit an Todo """

    try:# TODO: not working in new version
        now = datetime.now()
        Todos.save(
            request.POST['todo'],
            text = request.POST['text'],
            date = now,
        )
        return JsonResponse({
            'status': 'ok',
        }, encoder=JSONEncoder)  # return {'status':'ok'}

    except:
        return JsonResponse({
            'status': 'No',
        }, encoder=JSONEncoder)  # return {'status':'No'}

def TodoPage(request):
    context = {}
    return render(request, 'TodoPages.html', context)


def index(request):
    context = {}
    return render(request, 'index.html', context)
