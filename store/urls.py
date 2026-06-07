from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.stores, name='stores'),
    path('login/',views.login_view,name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('website/', views.stores, name='login'),
    path('feedback/', views.submit_feedback, name='feedback'),





    # #############


   path('electronics/', views.electronics, name='electronics'),
path('wooden/', views.wooden, name='wooden'),
path('clothes/', views.clothes, name='clothes'),
path('checkout/', views.checkout_view, name='checkout'),


################
    # path('chai/',include())
]
