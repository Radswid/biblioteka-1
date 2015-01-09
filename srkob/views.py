# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from srkob.models import Books, Genre
from srkob.forms import UserForm, ProfileForm
from django.contrib.auth.models import Group

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': " "}
    return render_to_response('srkob/index.html', context_dict, context)
    
def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': " "}
    return render_to_response('srkob/about.html', context_dict, context)

def category(request):
    context =RequestContext(request)
    category_category = Genre.objects.order_by('-genre')[:5]
    context_dict = {'genres': category_category}

    return render_to_response('srkob/category.html', context_dict, context)
    
def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
         user_form = UserForm(data=request.POST)
         profile_form = ProfileForm(data=request.POST)
         if user_form.is_valid() and profile_form.is_valid():
              user = user_form.save()
              user.set_password(user.password)
              user.save()
              profile = profile_form.save(commit=False)
              profile.user = user
              profile.save()
              #dodawanie użytkownika do grupy  
              g = Group.objects.get(name='uzytkownik')
              g.user_set.add(user)
              registered = True
         else:
             print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    # 
    return render_to_response(
            'srkob/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)                  


