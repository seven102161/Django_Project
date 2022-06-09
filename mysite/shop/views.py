from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from .forms import DetailForm
import pymongo
import re


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["magic_shop"]
mycol = mydb["foods"]


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return mycol.find({},{"_id": 0})


def detail(request, name):
    price = mycol.find({'name':name},{'_id':0})[0]['price']

    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid:
            pieces = request.POST['pieces']
            total = int(re.findall('\d+', price)[0]) * int(pieces)
            total = '{}元'.format(total)
            context = {
                'form': form,
                'name': name,
                'pieces': pieces,
                'price': price,
                'total': total,
            }
            return render(request, 'shop/detail.html', context)
    else:
        form = DetailForm({'pieces': 1})
        context = {
                'form': form,
                'name': name,
                'price': price,
                'total': '',
            }
        return render(request, 'shop/detail.html', context)


