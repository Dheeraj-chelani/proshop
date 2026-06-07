from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
from .models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Cart, CartItem
def stores(request):
    product =Product.objects.all()
    return render(request,'store/all_store.html',{'product':product})
def dheeraj(response):
    return HttpResponse("hello i am dheeraj")



def add_to_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)

        cart, created = Cart.objects.get_or_create(user=request.user)

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        if not created:
            item.quantity += 1
            item.save()

        return HttpResponse("added")


from django.contrib.auth.decorators import login_required

@login_required
def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart = Cart.objects.filter(user=request.user).first()

    items = []
    total = 0

    if cart:
        for item in CartItem.objects.filter(cart=cart):
            subtotal = item.product.price * item.quantity
            total += subtotal

            items.append({
                'product': item.product,
                'quantity': item.quantity,
                'subtotal': subtotal
            })

    return render(request, 'store/cart.html', {
        'items': items,
        'total': total
    })


def remove_from_cart(request, product_id):
    cart = Cart.objects.filter(user=request.user).first()

    if cart:
        item = CartItem.objects.filter(cart=cart, product_id=product_id).first()
        
        if item:
            if item.quantity > 1:
                item.quantity -= 1
                item.save()
            else:
                item.delete()

    return redirect('cart')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'store/register.html')



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('stores')
        else:
            return HttpResponse("Invalid credentials")

    return render(request, 'store/login.html')
def logout_view(request):
    logout(request)
    return redirect('login')

from .models import Feedback

def submit_feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Feedback.objects.create(
            name=name,
            email=email,
            message=message
        )
        return render(request, 'store/feedback.html')
    return redirect('stores')



 #######################


def electronics(request):
    eleproducts = Product.objects.filter(category="electronics")
    return render(request, 'store/category.html', {'eleproducts': eleproducts})

def wooden(request):
    products = Product.objects.filter(category="wooden")
    return render(request, 'store/wooden.html', {'wooproducts': products})

def clothes(request):
    products = Product.objects.filter(category="clothes")
    return render(request, 'store/clothes.html', {'cloproducts': products})


########################




# Naya Code - File ke last mein add karein
from .models import Order, OrderItem

@login_required
def checkout_view(request):
    cart = Cart.objects.filter(user=request.user).first()
    
    # Agar cart khali hai toh wapas bhej do
    if not cart or not CartItem.objects.filter(cart=cart).exists():
        return redirect('cart')

    cart_items = CartItem.objects.filter(cart=cart)
    total = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == "POST":
        # Form se details nikalna
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')

        # Naya Order banana
        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            phone=phone,
            address=address,
            city=city,
            pincode=pincode,
            total_amount=total
        )

        # Cart ke items ko Order mein daalna
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # Order complete hone ke baad Cart khali karna
        cart_items.delete()
        
        # Success page par bhej dena
        return HttpResponse("<h2 style='text-align:center; margin-top:50px; font-family:sans-serif;'>🎉 Order Placed Successfully! <br><br> <a href='/store' style='color:blue; text-decoration:none;'>Go back to Home</a></h2>")

    return render(request, 'store/checkout.html', {'items': cart_items, 'total': total})