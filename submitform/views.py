from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from models import Response
from django.template import RequestContext
from forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


import xlrd

def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)

def register(request):
    
    context = RequestContext(request)

    registered = False

   
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

   
        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True

        
        else:
            print user_form.errors, profile_form.errors

    
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

   
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)
			

def user_login(request):
  
    context = RequestContext(request)

   
    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        
        if user:
           
            if user.is_active:
                
                login(request, user)
                return HttpResponseRedirect('/uploadfile/')
            else:
               
                return HttpResponse("Your account is disabled.")
        else:
            
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    
    else:
        
        return render_to_response('login.html', {}, context)

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    return HttpResponseRedirect('/')
			
@login_required()
def processfile(request):
	if request.method == 'POST':
		c = {}
		c.update(csrf(request))
		form = UploadFileForm(request.POST)
		if form.is_valid():
			p1 = Response(response_one = form.cleaned_data['title'])
			p1.save()
			
			return render_to_response('thanks.html')
	else:
		form = UploadFileForm()
		return render_to_response('uploadfile.html', {'form':form}, context_instance=RequestContext(request))
	

