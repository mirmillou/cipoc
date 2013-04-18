# Create your views here.
from django import template
from django.template import Context
from django.http import HttpResponse
from hello.models import Hello
 
def index(request):
    hs = Hello.objects.all()
    t = template.loader.get_template('hello/index.html')
    c = Context({ 
        "hello_list" : hs
    })
    return HttpResponse(t.render(c))

