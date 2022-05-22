from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["magic_shop"]
mycol = mydb["foods"]

# Create your views here.
def index(request):
    product_list = mycol.find({},{"_id": 0})
    contents = {
        'product_list': product_list,
    }
    return render(request, 'shop/index.html', contents)


def detail(request, name):
    myquery = { "name": name }
    product = mycol.find(myquery,{"_id": 0})
    contents = {
        'product': product[0],
    }
    return render(request, 'shop/detail.html', contents)


def result(request):
    return render(request, 'shop/result.html')


def buy(request, name):
    p_vote = request.POST['p_name']
    p_name = name
    contents = {
        'p_name': p_name,
        'p_vote': p_vote
    }
    return render(request, 'shop/result.html', {'contents': contents})
