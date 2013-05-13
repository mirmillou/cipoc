# Create your views here.
from django import template
from django.template import Context
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from hello.models import Friend, Feed

def index(request):
    friends = Friend.objects.all()
    t = template.loader.get_template('hello/index.html')
    c = Context({ 
        "friend_list" : friends
    })
    feeds = Feed.objects.all()
    t = template.loader.get_template('hello/index.html')
    c = Context({ 
        "feed_list" : feeds
    })
    return HttpResponse(t.render(c))

from django.views.generic import ListView,  DetailView

class FeedList(ListView):
    model = Feed
    
class FeedDetail(DetailView):
    model = Feed
