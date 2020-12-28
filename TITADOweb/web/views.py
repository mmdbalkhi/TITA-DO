from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import JSONEncoder
from .models import TODO
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.

@csrf_exempt
def Todo(request):
    """ submit an expense """

    # TODO: revise validation for the amount
    this_date = request.POST['date'] if 'date' in request.POST else timezone.now()
    this_text = request.POST['text'] if 'text' in request.POST else ""
    this_amount = request.POST['amount'] if 'amount' in request.POST else "0"
    this_token = request.POST['token'] if 'token' in request.POST else ""
    this_user = get_object_or_404(User, token__token=this_token)

    TODO.objects.create(user=this_user, amount=this_amount,
                           text=this_text, date=this_date)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)  # return {'status':'ok'}

def index(request):
    context = {}
    return render(request, 'index.html', context)
