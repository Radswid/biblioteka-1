# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from srkob.models import Books, Genre
from srkob.forms import UserForm, ProfileForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/srkob/')
            else:
                return HttpResponse("Twoje konto jest zablokowane.")

        else:
            print "NIepoprawna dane:  {0}, {1}".format(username, password)
            return HttpResponse("Nieporawne dane logowania.")
    else:
        return render_to_response('srkob/login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/srkob/')
