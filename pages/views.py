from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Post
from .forms import TextForm
from django.http import HttpResponseRedirect
import random as rand
# Create your views here.

def HomePageView(request):
    return render(request, 'home.html')

class MessagePageView(TemplateView):
    template_name = 'message.html'
    def get(self, request, **kwargs):
        form = TextForm()
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, **kwargs):
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'thanks.html', {"form": form})



def WallPageView(request):
    model = Post
    context = {}
    text_all = model.objects.all()
    text_random = rand.choice(text_all)
    context['random_post']= text_random
    return render(request, 'wall.html', context)

class ThanksPageView(TemplateView):
    template_name = 'thanks.html'