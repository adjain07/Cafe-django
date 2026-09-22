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
        'cart/update/',
        views.update_cart,
        name='update_cart'
    ),

    path(
        'cart/remove/<int:item_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
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
        'my-orders/<int:order_id>/',
        views.order_detail,
        name='order_detail'
    ),
]