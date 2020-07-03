# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Categorys,Image,Location
# Create your views here.
def welcome(request):
    
    return render(request,'welcome.html')
def convert_dates(dates):
    '''
    function that gets the weekely number of the date.
    '''
    day_number = dt.date.weekday(dates)
    days =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    '''
    returning the actual day of the week 
    '''
    day = days[day_number]
    return day

def image_today(request):
    gallery = Image.gallery_images()
    category= Categorys.objects.all()
    location= Location.objects.all()
    return render(request,'all-images/gallery-images.html',{"gallery":gallery,'category':category,"location":location})

def search_results(request):
    category= Categorys.objects.all()
    location= Location.objects.all()
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"images": searched_image,'category':category,"location":location})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})

def category_imge(request,category_id):
    category=Category.query.get(id=category_id)
    return render(request,'category.html',locals())

def category_image(request,category_id):
    images=Image.objects.filter(category__name=category_id)
    category= Categorys.objects.all()
    location= Location.objects.all()
    return render(request,'all-images/gallery-images.html',{'gallery':images,'category':category,'location':location})

def location_image(request,location_id):
    gallery = Image.objects.filter(location__name=location_id)
    location = Location.objects.all()
    category= Categorys.objects.all()

    return render(request,"all-images/gallery-images.html", {"gallery":gallery,"location":location,'category':category})

    
