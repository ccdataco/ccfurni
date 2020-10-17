from django.urls import path
from . import views
urlpatterns = [
    path('',views.mainpage),
    path('home',views.home, name = 'home'),

    path('about_us',views.about_us, name = 'about_us'),
    path('products',views.products, name = 'products'),
    path('rooms',views.rooms, name = 'rooms'),
     path('forB2BCustomer',views.forB2BCustomer, name = 'forB2BCustomer'),
    # path('products',views.products),
    # path('rooms',views.rooms),
    # path('sale',views.sale),
    # path('for_b2bc',views.for_b2bc),
    # path('cart',views.cart),
    # path('account',views.account),
    
    
]