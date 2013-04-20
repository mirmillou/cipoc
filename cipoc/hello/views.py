# Create your views here.
from django import template
from django.template import Context
from django.http import HttpResponse
from hello.models import Friend
 
def index(request):
    friends = Friend.objects.all()
    t = template.loader.get_template('hello/index.html')
    c = Context({ 
        "friend_list" : friends
    })
    return HttpResponse(t.render(c))

