from django.shortcuts import render, redirect
from .models import User, UserPlace
import bcrypt
from django.contrib import messages
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'wild/index.html')


def login(request):
    check = User.userManager.checklog(request.POST['loginemail'], request.POST['loginpass'])

    if check[0] == True:
        request.session['id']=check[1].id
        return redirect('/main')
    else:
        for error in check:
            messages.error(request, error)
        return redirect ('/loginreg')

def register(request):
    check = User.userManager.checkreg(request.POST['name'], request.POST['email'], request.POST['pass'], request.POST['conf_pass'])

    if check == True:
        passinput = request.POST['pass'].encode()
        hashed = bcrypt.hashpw(passinput, bcrypt.gensalt())
        the_user = User.objects.create(name=request.POST['name'], email=request.POST['email'], password=hashed)
        request.session['id'] = the_user.id
        return redirect('/preferences/'+ str(the_user.id))
    else:
        for error in check:
            messages.error(request, error)
        return redirect('/loginreg')

def loginreg(request):
    return render(request, 'wild/loginreg.html')


def main(request):
    the_user = User.objects.get(id = request.session['id'])
    if the_user:
        context = {'user': the_user}
        return render(request, 'wild/main.html', context)
    else:
        return redirect('/loginreg')

def preferences(request):
    return render(request, 'wild/preferences.html')
