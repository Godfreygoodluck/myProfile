from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .models import Message, Contact, Profile, MySkill, What_i_do, Ecommerce, Portfolio, Blog, Message
from .form import ClientsMessageForm
import os   
# Create your views here.


def index(request):
    
    page = request.GET.get('page', 1)
    #Ajax..................................................................................
    limit = request.GET.get('limit')
    start = request.GET.get('start')

    #Ecommerce.........................................
    ecommerce = Ecommerce.objects.all().order_by('-created_on')
    
    #Portfolio.........................................
    portfolio = Portfolio.objects.all().order_by('-created_on')
    
    #Ecommerce.........................................
    blog = Blog.objects.all().order_by('-created_on')  

    #contact............................................
    contact = Contact.objects.all()

    #contact............................................
    mySkill = MySkill.objects.all()

    #contact............................................
    what_i_do = What_i_do.objects.all()

    #message............................................
    form = ClientsMessageForm()
    if request.method == 'POST':
        form = ClientsMessageForm(request.POST)
        if form.is_valid():
            message = Message(
                name=form.cleaned_data["name"],
                phone=form.cleaned_data["phone"],
                message=form.cleaned_data["message"],
                mail=form.cleaned_data["email"],
            )
            message.save()

    #profile............................................
    profile = Profile.objects.all()

    #...................................................
    context = {
        'ecommerce' : ecommerce,
        'portfolio' : portfolio,
        'blog' : blog,
        'contact' : contact,
        'profile' : profile, 
        'mySkill' : mySkill,
        'what_i_do' : what_i_do,
        'form' : form,
    }

    return render(request, 'index.html', context=context)



