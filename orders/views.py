from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from menu.models import MenuItem

from .models import Order, OrderItem
from .forms import CheckoutForm


def add_to_cart(request, item_id):

    item = get_object_or_404(
        MenuItem,
        id=item_id,
        is_available=True
    )

    cart = request.session.get('cart', {})

    item_id = str(item_id)

    cart[item_id] = cart.get(item_id, 0) + 1

    request.session['cart'] = cart

    messages.success(
        request,
        f'{item.name} added to cart.'
    )

    return redirect('cart')


def cart(request):

    cart_data = request.session.get('cart', {})

    cart_items = []
    total = Decimal('0.00')

    for item_id, quantity in cart_data.items():

        item = get_object_or_404(
            MenuItem,
            id=item_id,
            is_available=True
        )

        subtotal = item.price * quantity

        total += subtotal

        cart_items.append({
            'item': item,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(
        request,
        'orders/cart.html',
        {
            'cart_items': cart_items,
            'total': total,
        }
    )


def checkout(request):

    cart_data = request.session.get('cart', {})

    if not cart_data:
        messages.warning(request, 'Your cart is empty.')
        return redirect('cart')

    total = Decimal('0.00')
    items = []

    for item_id, quantity in cart_data.items():

        item = get_object_or_404(
            MenuItem,
            id=item_id,
            is_available=True
        )

        total += item.price * quantity

        items.append(
            (item, quantity)
        )

    if request.method == 'POST':

        form = CheckoutForm(request.POST)

        if form.is_valid():

            order = Order.objects.create(
                user=(
                    request.user
                    if request.user.is_authenticated
                    else None
                ),
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                total_amount=total,
            )

            for item, quantity in items:

                OrderItem.objects.create(
                    order=order,
                    menu_item=item,
                    quantity=quantity,
                    price=item.price,
                )

            request.session['cart'] = {}

            return redirect(
                'order_success',
                order_id=order.id
            )

    else:

        initial = {}

        if request.user.is_authenticated:
            initial['name'] = request.user.get_full_name()
            initial['email'] = request.user.email

        form = CheckoutForm(initial=initial)

    return render(
        request,
        'orders/checkout.html',
        {
            'form': form,
            'total': total,
        }
    )


def order_success(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id
    )

    return render(
        request,
        'orders/order_success.html',
        {
            'order': order,
        }
    )


@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).prefetch_related(
        'items__menu_item'
    ).order_by('-created_at')

    return render(
        request,
        'orders/my_orders.html',
        {
            'orders': orders,
        }
    )


@login_required
def order_detail(request, order_id):

    order = get_object_or_404(
        Order.objects.prefetch_related(
            'items__menu_item'
        ),
        id=order_id,
        user=request.user
    )

    status_steps = [
        ('pending', 'Order Placed'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('completed', 'Completed'),
    ]

    status_messages = {
        'pending': 'Your order has been received and is waiting for confirmation.',
        'confirmed': 'Your order has been confirmed by the café.',
        'preparing': 'Our team is preparing your order fresh.',
        'ready': 'Your order is ready.',
        'completed': 'Your order has been completed. Thank you for ordering with us.',
        'cancelled': 'Unfortunately, this order has been cancelled.',
    }

    current_status = order.status

    if current_status in ['pending', 'confirmed', 'preparing', 'ready', 'completed']:

        current_index = next(
            (
                index
                for index, (status, label) in enumerate(status_steps)
                if status == current_status
            ),
            0
        )

    else:
        current_index = -1

    return render(
        request,
        'orders/order_detail.html',
        {
            'order': order,
            'status_steps': status_steps,
            'current_index': current_index,
            'status_message': status_messages.get(
                current_status,
                'Your order status has been updated.'
            ),
        }
    )