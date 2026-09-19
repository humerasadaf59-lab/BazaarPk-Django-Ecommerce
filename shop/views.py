from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CheckoutForm, RegisterForm
from .models import Category, Order, OrderItem, Product

SHIPPING=Decimal('199')

def cart_data(request):
    cart=request.session.get('cart',{})
    products=Product.objects.filter(id__in=cart.keys(),active=True)
    rows=[]; subtotal=Decimal('0')
    for p in products:
        qty=max(1,int(cart.get(str(p.id),cart.get(p.id,1))))
        qty=min(qty,p.stock)
        line=p.price*qty; subtotal+=line
        rows.append({'product':p,'qty':qty,'line':line})
    shipping=SHIPPING if subtotal else Decimal('0')
    return rows,subtotal,shipping,subtotal+shipping

def home(request):
    return render(request,'shop/home.html',{'featured':Product.objects.filter(active=True,featured=True)[:8],'categories':Category.objects.all()})

def shop(request):
    qs=Product.objects.filter(active=True).select_related('category')
    q=request.GET.get('q','').strip(); category=request.GET.get('category',''); sort=request.GET.get('sort','newest')
    if q: qs=qs.filter(name__icontains=q)
    if category: qs=qs.filter(category__slug=category)
    if sort=='price_low': qs=qs.order_by('price')
    elif sort=='price_high': qs=qs.order_by('-price')
    else: qs=qs.order_by('-created_at')
    return render(request,'shop/shop.html',{'products':qs,'categories':Category.objects.all(),'active_category':category,'q':q,'sort':sort})

def product_detail(request,slug):
    p=get_object_or_404(Product,slug=slug,active=True)
    related=Product.objects.filter(active=True,category=p.category).exclude(pk=p.pk)[:4]
    return render(request,'shop/product_detail.html',{'product':p,'related':related})

def add_to_cart(request,product_id):
    p=get_object_or_404(Product,id=product_id,active=True)
    cart=request.session.setdefault('cart',{})
    key=str(p.id); current=int(cart.get(key,0)); cart[key]=min(current+1,p.stock); request.session.modified=True
    messages.success(request,f'{p.name} added to your cart.')
    return redirect(request.POST.get('next') or request.META.get('HTTP_REFERER') or 'shop')

def cart(request):
    rows,subtotal,shipping,total=cart_data(request)
    return render(request,'shop/cart.html',locals())

def update_cart(request,product_id):
    p=get_object_or_404(Product,id=product_id,active=True); qty=max(0,int(request.POST.get('quantity',1)))
    cart=request.session.setdefault('cart',{}); key=str(p.id)
    if qty==0: cart.pop(key,None)
    else: cart[key]=min(qty,p.stock)
    request.session.modified=True; return redirect('cart')

def remove_from_cart(request,product_id):
    request.session.setdefault('cart',{}).pop(str(product_id),None); request.session.modified=True; return redirect('cart')

@transaction.atomic
def checkout(request):
    rows,subtotal,shipping,total=cart_data(request)
    if not rows: messages.info(request,'Your cart is empty.'); return redirect('shop')
    if request.method=='POST':
        form=CheckoutForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False); order.user=request.user if request.user.is_authenticated else None
            order.subtotal=subtotal; order.shipping=shipping; order.total=total; order.save()
            for row in rows:
                OrderItem.objects.create(order=order,product=row['product'],product_name=row['product'].name,price=row['product'].price,quantity=row['qty'])
                row['product'].stock=max(0,row['product'].stock-row['qty']); row['product'].save(update_fields=['stock'])
            request.session['cart']={}; request.session.modified=True
            return redirect('order_success',order_id=order.id)
    else:
        initial={}
        if request.user.is_authenticated: initial={'email':request.user.email,'full_name':request.user.get_full_name()}
        form=CheckoutForm(initial=initial)
    return render(request,'shop/checkout.html',locals())

def order_success(request,order_id):
    order=get_object_or_404(Order,id=order_id)
    return render(request,'shop/order_success.html',{'order':order})

@login_required
def account(request):
    return render(request,'shop/account.html',{'orders':request.user.orders.prefetch_related('items').order_by('-created_at')})

def register(request):
    if request.user.is_authenticated: return redirect('account')
    form=RegisterForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        user=form.save(); login(request,user); messages.success(request,'Welcome to BazaarPK!'); return redirect('account')
    return render(request,'registration/register.html',{'form':form})
