from django.shortcuts import render, redirect
from proapp.models import categorydata, productdata

from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.
def index_page(request):
    return render(request, "index.html")

def add_items(request):
    return render(request,"add_items.html")
def save_data(request):
    if request.method=="POST":
        x = request.POST.get('name')
        y = request.POST.get('description')
        z = request.FILES['image']
        obj = categorydata(Cname=x,Description=y,Image=z)
        obj.save()
        return redirect(add_items)
def display_items(request):
    data = categorydata.objects.all()
    return render(request, "display_items.html",{'data':data})

def edit_items(request,dataid):
    data = categorydata.objects.get(id=dataid)
    return render(request,"edit_items.html",{'data':data})


def update_items(request, dataid):
  if request.method=="POST":
       x = request.POST.get('name')
       y = request.POST.get('description')
       try:
            z = request.FILES['image']
            j = FileSystemStorage()
            file = j.save(z.name,z)
       except MultiValueDictKeyError:
            file = categorydata.objects.get(id=dataid).Image
       categorydata.objects.filter(id=dataid).update(Cname=x, Description=y, Image=file)
       return redirect(display_items)

def items_delete(request,dataid):
    data = categorydata.objects.filter(id=dataid)
    data.delete()
    return redirect(display_items)

def product(request):
    p = categorydata.objects.all()
    return render(request,"product.html",{'p':p})

def save_product(request):
    if request.method == "POST":
        p = request.POST.get('name')
        q = request.POST.get('pname')
        r = request.POST.get('quantity')
        s = request.POST.get('price')
        t = request.POST.get('pdescription')
        u = request.FILES['pimage']
        obj = productdata(Name=p, Pname=q, Quantity=r, Price=s, Pdescription=t, Pimage=u)
        obj.save()
        return redirect(product)

def display_product(request):
    p = productdata.objects.all()
    return render(request, "display_product.html", {'p': p})

def edit_product(request,productid):
    data = categorydata.objects.all()
    p = productdata.objects.get(id=productid)
    return render(request,"edit_items.html", {'p': p, 'data': data})

def update_product(request,productid):
    if request.method == "POST":
        p = request.POST.get('name')
        q = request.POST.get('pname')
        r = request.POST.get('quantity')
        s = request.POST.get('price')
        t = request.POST.get('pdescription')
        try:
            u = request.FILES['pimage']
            k = FileSystemStorage()
            file = k.save(u.name, u)
        except MultiValueDictKeyError:
            file = productdata.objects.get(id=productid).Image
        productdata.objects.filter(Name=p, Pname=q, Quantity=r, Price=s, Pdescription=t, Pimage=file)
        return redirect(display_product)

def product_delete(request,productid):
    p = productdata.objects.filter(id=productid)
    p.delete()
    return redirect(display_product)

def admin_page(request):
    return render(request, "admin.html")
def admin_login(request):
    if request.method=="POST":
        a = request.POST.get('username')
        b = request.POST.get('password')
        if User.objects.filter(username__contains=a).exists():
            user=authenticate(username=a, password=b)
            if user is not None:
                login(request,user)
                request.session['username']=a
                request.session['password']=b
                return redirect(index_page)
            else:
                return redirect(admin_page)
        else:
            return redirect(admin_page)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_page)



