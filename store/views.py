from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Product,Order
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method=="POST":

        username=request.POST.get('username')
        password=request.POST.get('password')

        User.objects.create_user(username=username,password=password)

        return redirect('login')

    return render(request,'register.html')


def login_page(request):

    if request.method=="POST":

        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            login(request,user)
            return redirect('home')

    return render(request,'login.html')


def logout_page(request):
    logout(request)
    return redirect('login')


def home(request):

    products = Product.objects.all()

    return render(
        request,
        'home.html',
        {'products': products}
    )


from django.contrib.auth.decorators import login_required

@login_required
def add_product(request):

    if not request.user.is_superuser:
        return redirect('home')

    if request.method == "POST":
        Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
            stock=request.POST.get('stock'),
            image=request.FILES.get('image')
        )

        return redirect('home')

    return render(request,'add_product.html')

def checkout(request,id):

    product=Product.objects.get(id=id)

    if request.method=="POST":

        address=request.POST.get('address')

        Order.objects.create(user=request.user,product=product,address=address)

        return redirect('orders')

    return render(request,'checkout.html',{'product':product})


def orders(request,id):

    orders=Order.objects.all()

    return render(request,'orders.html',{'orders':orders})


def orders(request):

    if request.user.is_superuser:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user=request.user)

    return render(request, 'orders.html', {'orders': orders})


@login_required
def delete_product(request,id):

    if not request.user.is_superuser:
        return redirect('home')

    product = get_object_or_404(Product,id=id)

    product.delete()

    return redirect('home')


@login_required
def admin_dashboard(request):

    if not request.user.is_superuser:
        return redirect('home')

    products = Product.objects.all()

    return render(request, 'admin_dashboard.html', {
        'products': products
    })


def cancel_order(request, id):

    order = get_object_or_404(Order, id=id)

    if order.user == request.user or request.user.is_superuser:
        order.delete()

    return redirect('orders')