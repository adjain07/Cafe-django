from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),

    path(
        'cart/add/<int:item_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    path(
        'success/<int:order_id>/',
        views.order_success,
        name='order_success'
    ),

    path(
        'my-orders/',
        views.my_orders,
        name='my_orders'
    ),

    path(
        '<int:order_id>/',
        views.order_detail,
        name='order_detail'
    ),
]