from json import JSONEncoder

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from web.models import Todos, Token, User

# Create your views here.


# submit an expanse to system (api) , input : token(POST) , output :
# status = (ok)
@csrf_exempt
@require_POST
def postTodo(request):
    """ submit an Todo """

    # TODO: revise validation for the amount
    
    this_date = request.POST['date'] if 'date' in request.POST else timezone.now()
    this_text = request.POST['text'] if 'text' in request.POST else ""
    this_todo = request.POST['todo'] if 'todo' in request.POST else ""
    this_token = request.POST['token'] if 'token' in request.POST else ""
    CheckBox = request.POST['checkBox'] if 'checbox' in request.POST else ""
    this_user = get_object_or_404(User, token__token=this_token)

    Todos.objects.create(user=this_user, todo=this_todo,
                           text=this_text, date=this_date)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)  # return {'status':'ok'}


def index(request):
    context = {}
    return render(request, 'index.html', context)
