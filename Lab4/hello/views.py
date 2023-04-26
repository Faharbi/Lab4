from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
tax_rate = 0.15

def index(request):
    return render(request, 'hello/index.html')

def calculate_price(request, num):
    price = float(num) * (1 + tax_rate)
    context = {'price': price}
    return render(request, 'hello/price.html', context)

def show_tax_rate(request):
    context = {'tax_rate': tax_rate}
    return render(request, 'hello/tax_rate.html', context)
