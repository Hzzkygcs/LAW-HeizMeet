from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from hello_world.models import HelloWorldMessage


def index(request):
    messages = HelloWorldMessage.objects.all()
    return render(request, "hello-world.html", {
        'messages': [o.message for o in messages]
    })


@require_http_methods(["POST"])
def msg(request):
    if "msg" not in request.POST:
        return redirect('helloworld')
    msg = HelloWorldMessage()
    msg.message = request.POST['msg']
    msg.save()
    return redirect('helloworld')

# Create your views here.
