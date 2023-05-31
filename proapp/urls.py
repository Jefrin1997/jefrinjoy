from django.urls import path
from proapp import views


urlpatterns = [
       path('index_page/', views.index_page, name="index_page"),
       path('add_items/', views.add_items, name="add_items"),
       path('save_data/', views.save_data, name="save_data"),
       path('display_items/', views.display_items, name="display_items"),
       path('edit_items/<int:dataid>', views.edit_items, name="edit_items"),
       path('update_items/<int:dataid>', views.update_items, name="update_items"),
       path('items_delete/<int:dataid>', views.items_delete, name="items_delete"),
       path('product/', views.product, name="product"),
       path('save_product/', views.save_product, name="save_product"),
       path('display_product/', views.display_product, name="display_product"),
       path('edit_product/<int:productid>', views.edit_product, name="edit_product"),
       path('update_product/<int:productid>', views.update_product, name="update_product"),
       path('product_delete/<int:productid>', views.product_delete, name="product_delete"),
       path('admin_page/', views.admin_page, name="admin_page"),
       path('admin_login/', views.admin_login, name="admin_login"),
       path('admin_logout/', views.admin_logout, name="admin_logout"),
]