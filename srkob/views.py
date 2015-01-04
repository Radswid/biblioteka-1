# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from srkob.models import books, genre
def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('srkob/index.html', context_dict, context)
    
def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('srkob/about.html', context_dict, context)

def category(request):
    context =RequestContext(request)
    category_category = genre.objects.order_by('-genre_main')[:5]
    context_dict = {'genres': category_category}

    # Render the response and send it back!
    return render_to_response('srkob/category.html', context_dict, context)
    
