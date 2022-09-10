from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Profile

@login_required(login_url='signin')
def index(request):
  products = Product.objects.all()
  return render(request, 'index.html', {
    'products':products, 
  })

def contact(request, pk):
  product = Product.objects.get(id=pk)
  return render(request, 'contact.html', {'product':product})

def signup(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2'] 

    if username=="" and email=='' and password=='' and password2=='':
      messages.info(request, 'Input Your Details') 
      return redirect('signup')
    elif username=="" or email=='' or password=='' or password2=='':
      messages.info(request, 'Incomplete Credential') 
      return redirect('signup')  
    else:  
      if password == password2:
        if User.objects.filter(email=email).exists():
          messages.info(request, 'Email Taken')
          return redirect('signup')
        elif User.objects.filter(username=username).exists():
          messages.info(request, 'Username Taken')
          return redirect('signup')
        else:
          user = User.objects.create_user(username=username, email=email, password=password)
          user.save()    
      # log user in and redirect to settiongs page
          user_login = auth.authenticate(username=username, password=password)
          auth.login(request, user_login)


      # create a profile object for new user
        user_model = User.objects.get(username=username)     
        new_profile = Profile.objects.create(user=user_model,  id_user=user_model.id)
        new_profile.save()
        return redirect('setting')

      else:
        messages.info(request, 'Password Not Identical')
        return redirect('signup')

  else:
    return render(request, 'signup.html' )

def signin(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    # if username == '' and password == '':
    #   messages.info(request, 'Input Username and Password')
    #   return redirect('signin')
    # else:
    if username == '':
      messages.info(request, 'Input Username')
      return redirect('signin')
    elif password == '':
      messages.info(request, 'Input Password') 
      return redirect('signin')
    else:
      if user is not None:
        auth.login(request, user)
        return redirect('/')
      else:
        messages.info(request, 'invalid input')
        return redirect('signin')   
  else:
    return render(request, 'signin.html')

@login_required(login_url='signin',)
def logout(request):
  auth.logout(request,)
  return redirect('signin')


@login_required(login_url='signin')
def setting(request):
  user_profile = Profile.objects.get(user=request.user)

  if request.method == 'POST':

    if request.FILES.get('image') == None:
      image = user_profile.profileimg
      location = request.POST['location']

      user_profile.profileimg = image
      user_profile.location = location
      user_profile.save()
    
    if request.FILES.get('image') != None:
      image = request.FILES.get('image')
      location = request.POST['location']

      user_profile.profileimg = image
      user_profile.location = location
      user_profile.save()

    return redirect('setting')
  return render(request, 'setting.html', {'user_profile':user_profile} )






