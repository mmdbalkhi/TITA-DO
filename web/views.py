from json import JSONEncoder

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from web.models import Todos, Token, User
# Create your views here.


# status = (ok and no)
@csrf_exempt
def postTodo(request):
    """ submit an Todo """

    try:# TODO: not working in new version
        this_token = request.POST['token']
        this_user = User.objects.filter(token__token = this_token.get())
        now = datetime.now()
        Todos.object.create(user = this_user, todo = request.POST['todo'],
                            text = request.POST['text'], date = now)
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
