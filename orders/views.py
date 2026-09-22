from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from menu.models import MenuItem

from .models import Order, OrderItem
from .forms import CheckoutForm


# =========================================================
# ADD TO CART
# =========================================================

def add_to_cart(request, item_id):

    item = get_object_or_404(
        MenuItem,
        id=item_id,
        is_available=True
    )

    cart = request.session.get('cart', {})

    item_id = str(item.id)

    current_quantity = cart.get(item_id, 0)

    try:
        current_quantity = int(current_quantity)
    except (ValueError, TypeError):
        current_quantity = 0

    cart[item_id] = current_quantity + 1

    request.session['cart'] = cart
    request.session.modified = True

    messages.success(
        request,
        f'{item.name} added to cart.'
    )

    return redirect('cart')


# =========================================================
# CART
# =========================================================

def cart(request):

    cart_data = request.session.get('cart', {})

    cart_items = []
    total = Decimal('0.00')

    # Invalid cart IDs ko remove karne ke liye
    clean_cart = {}

    for item_id, quantity in cart_data.items():

        # Empty/invalid item ID skip karo
        if not str(item_id).isdigit():
            continue

        try:
            item_id = int(item_id)
            quantity = int(quantity)
        except (ValueError, TypeError):
            continue

        # Invalid quantity skip/remove
        if quantity <= 0:
            continue

        item = MenuItem.objects.filter(
            id=item_id,
            is_available=True
        ).first()

        # Agar item database me nahi hai
        if not item:
            continue

        subtotal = item.price * quantity

        total += subtotal

        clean_cart[str(item_id)] = quantity

        cart_items.append({
            'item': item,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    # Clean cart session me save karo
    request.session['cart'] = clean_cart
    request.session.modified = True

    return render(
        request,
        'orders/cart.html',
        {
            'cart_items': cart_items,
            'total': total,
        }
    )


# =========================================================
# UPDATE CART
# =========================================================

def update_cart(request):

    if request.method != 'POST':
        return redirect('cart')

    cart = request.session.get('cart', {})

    new_cart = {}

    for field_name, quantity in request.POST.items():

        if not field_name.startswith('quantity_'):
            continue

        item_id = field_name.replace(
            'quantity_',
            '',
            1
        )

        # Empty ID ignore karo
        if not item_id.isdigit():
            continue

        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            continue

        # 0 ya negative = remove
        if quantity <= 0:
            continue

        # Maximum 20
        quantity = min(quantity, 20)

        # Check item actually exists
        if MenuItem.objects.filter(
            id=int(item_id),
            is_available=True
        ).exists():

            new_cart[item_id] = quantity

    request.session['cart'] = new_cart
    request.session.modified = True

    messages.success(
        request,
        'Cart updated successfully.'
    )

    return redirect('cart')


# =========================================================
# REMOVE FROM CART
# =========================================================

def remove_from_cart(request, item_id):

    cart = request.session.get('cart', {})

    item_id = str(item_id)

    cart.pop(item_id, None)

    request.session['cart'] = cart
    request.session.modified = True

    messages.success(
        request,
        'Item removed from cart.'
    )

    return redirect('cart')


# =========================================================
# CHECKOUT
# =========================================================

def checkout(request):

    cart_data = request.session.get('cart', {})

    # Check empty cart
    if not cart_data:

        messages.warning(
            request,
            'Your cart is empty.'
        )

        return redirect('cart')

    total = Decimal('0.00')
    items = []

    # Calculate cart total
    for item_id, quantity in cart_data.items():

        item = get_object_or_404(
            MenuItem,
            id=item_id,
            is_available=True
        )

        subtotal = item.price * quantity

        total += subtotal

        items.append(
            (item, quantity)
        )

    # POST
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

            # Create order items
            for item, quantity in items:

                OrderItem.objects.create(

                    order=order,

                    menu_item=item,

                    quantity=quantity,

                    price=item.price,
                )

            # Clear cart after successful order
            request.session['cart'] = {}
            request.session.modified = True

            messages.success(
                request,
                'Your order has been placed successfully.'
            )

            return redirect(
                'order_success',
                order_id=order.id
            )

    # GET
    else:

        initial = {}

        if request.user.is_authenticated:

            initial['name'] = request.user.get_full_name()

            initial['email'] = request.user.email

        form = CheckoutForm(
            initial=initial
        )

    return render(
        request,
        'orders/checkout.html',
        {
            'form': form,
            'total': total,
        }
    )


# =========================================================
# ORDER SUCCESS
# =========================================================

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


# =========================================================
# MY ORDERS
# =========================================================

@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).prefetch_related(
        'items__menu_item'
    ).order_by(
        '-created_at'
    )

    return render(
        request,
        'orders/my_orders.html',
        {
            'orders': orders,
        }
    )


# =========================================================
# ORDER DETAIL
# =========================================================

@login_required
def order_detail(request, order_id):

    order = get_object_or_404(

        Order.objects.prefetch_related(
            'items__menu_item'
        ),

        id=order_id,

        user=request.user
    )

    # Order tracking steps
    status_steps = [
        ('pending', 'Order Placed'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('completed', 'Completed'),
    ]

    # Messages for each status
    status_messages = {

        'pending':
            'Your order has been received and is waiting for confirmation.',

        'confirmed':
            'Your order has been confirmed by the café.',

        'preparing':
            'Our team is preparing your order fresh.',

        'ready':
            'Your order is ready.',

        'completed':
            'Your order has been completed. Thank you for ordering with us.',

        'cancelled':
            'Unfortunately, this order has been cancelled.',
    }

    current_status = order.status

    # Find current tracking step
    if current_status in [
        'pending',
        'confirmed',
        'preparing',
        'ready',
        'completed'
    ]:

        current_index = next(

            (
                index

                for index, (status, label)
                in enumerate(status_steps)

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