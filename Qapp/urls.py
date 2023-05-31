from django.urls import path
from Qapp import views

urlpatterns = [

    path('web_page/', views.web_page, name="web_page"),
    path('login_page/', views.login_page, name="login_page"),
    path('save_login/', views.save_login, name="save_login"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('products_page/<catg>', views.products_page, name="products_page"),
    path('productsall/', views.productsall, name="productsall"),
    path('single_product_page/<int:dataid>', views.single_product_page, name="single_product_page"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('save_cart/', views.save_cart, name="save_cart"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('cart_delete/<int:dataid>', views.cart_delete, name="cart_delete"),
    path('invoice/', views.invoice, name="invoice"),
    path('save_invoice/', views.save_invoice, name="save_invoice"),
    path('contact_page/', views.contact_page, name="contact_page"),
    path('save_contact/', views.save_contact, name="save_contact"),




]
