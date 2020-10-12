from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request,'page/mainpage.html')
def home(request):
    return render(request,'page/mainpage.html')
def about_us(request):
    return render(request,'page/about_us.html')
def products(request):
    return render(request,'page/products.html')
def rooms(request):
    return render(request,'page/rooms.html')
