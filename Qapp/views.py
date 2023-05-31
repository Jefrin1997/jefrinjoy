from django.shortcuts import render,redirect
from Qapp.models import logindata,cartdata
from proapp.models import categorydata,productdata,invoicedata,contactdata
from django.contrib import messages

# Create your views here.
def web_page(request):
    data = categorydata.objects.all()
    return render(request, "webpage.html", {'data': data})
def login_page(request):
    return render(request, "login_page.html")
def save_login(request):
    if request.method == "POST":
        p = request.POST.get('email')
        q = request.POST.get('password')
        r = request.POST.get('cpass')
        obj = logindata(Email=p, Password=q, Cpass=r)
        obj.save()
        return redirect(login_page)
def products_page(request,catg):
    data = categorydata.objects.all()
    pro  = productdata.objects.filter(Name=catg)
    return render(request,"products.html", {'data': data, 'pro': pro})
def productsall(request):
    r = productdata.objects.all()
    return render(request,"allproducts.html", {'r': r})
def single_product_page(request,dataid):
    pro = productdata.objects.get(id=dataid)
    return render(request, "single_productpage.html", {'pro': pro})
def aboutus(request):
    return render(request, "aboutus.html")

def user_login(request):
    if request.method=="POST":
        a = request.POST.get('email')
        b = request.POST.get('password')
        if logindata.objects.filter(Email=a, Password=b).exists():

            request.session['email'] = a
            request.session['password'] = b

            return redirect(web_page)
        else:
            return redirect(login_page)
    return redirect(login_page)
def user_logout(request):
        del request.session['email']
        del request.session['password']
        return redirect(login_page)

def cart_page(request):
    cart = cartdata.objects.filter(User=request.session['email'])
    return render(request, "cartpage.html",{'cart': cart})
def save_cart(request):
    if request.method == "POST":
        q = request.POST.get('pname')

        r = request.POST.get('qty')
        s = request.POST.get('totalprice')
        t = request.POST.get('email')
        obj = cartdata(Pname=q, quantity=r, total_price=s, User=t)
        obj.save()
        messages.success(request, "added successfully")
        return redirect(web_page)

def cart_delete(request,dataid):
    data = cartdata.objects.filter(id=dataid)
    data.delete()
    return redirect(cart_page)
def invoice(request):
    data = cartdata.objects.filter(User=request.session['email'])
    return render(request, "placeorder.html",{'data': data})
def save_invoice(request):
    if request.method == "POST":
        q = request.POST.get('name')
        r = request.POST.get('emailid')
        s = request.POST.get('address')
        p = request.POST.get('phone')
        t = request.POST.get('description')
        obj = invoicedata(Uname=q, Emailid=r, Address=s, Phone=p, Description=t)
        obj.save()
        messages.success(request, "order placed  successfully")
        return redirect(web_page)
def contact_page(request):
    return render(request, "contact.html")
def save_contact(request):
    if request.method == "POST":
        q = request.POST.get('name')
        r = request.POST.get('emailid')
        p = request.POST.get('phone')
        s = request.POST.get('subject')
        t = request.POST.get('description')
        obj = contactdata(Name=q, Emailid=r, Subject=s, Phone=p, Description=t)
        obj.save()
        messages.success(request, "will contact you asap")
        return redirect(web_page)




