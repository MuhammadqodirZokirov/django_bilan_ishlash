# from itertools import product

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Contact, Category, RegisterTable, Add_Product
from .forms import Add_ProductForm
from django.db.models import Q
from django.core.mail import EmailMessage


def index(request):
    data = Contact.objects.all()
    category = Category.objects.all()
    context = {
        'contacts': data,
        'categories': category
    }
    return render(request, 'index.html', context)


def about(request):
    context = {}
    cats = Category.objects.all().order_by('cat_name')
    context['categories'] = cats
    return render(request, 'about.html', context)


def contact(request):
    context = {}
    cats = Category.objects.all().order_by('cat_name')
    context['categories'] = cats
    print('Data = ', request.POST)
    if request.method == 'POST':
        full = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        feed = request.POST['feedback']
        data = Contact(fullName=full, email=email, phone=phone, feedback=feed)
        data.save()
        res = f'Mr/Miss {full}  your feed created Successfully'
        return render(request, 'contact.html', {'status': res})

    return render(request, 'contact.html', context)


def register(request):
    # print(request.POST)
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        utype = request.POST['utype']

        usr = User.objects.create_user(username, email, password)
        usr.first_name = fname
        usr.last_name = lname
        if utype == 'sell':
            usr.is_staff = True
        usr.save()
        data = RegisterTable(user=usr, phone=phone)
        data.save()
        return render(request, 'register.html',
                      {'status': f'Mr/Miss {usr.first_name} successfully registered'})
    return render(request, 'register.html')


def check_user(request):
    if request.method == 'GET':
        un = request.GET['usern']
        check = User.objects.filter(username=un)
        if len(check) == 1:
            return HttpResponse('Exists')
        else:
            return HttpResponse("Not Exists")
    return HttpResponse('Called')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(username, password)
        if user:
            login(request, user)
            if user.is_superuser:
                return HttpResponseRedirect('/admin')
            else:
                return HttpResponseRedirect('/custom_dashboard')
        else:
            return render(request, 'index.html', {'status': 'Invalid username or password'})
    return HttpResponse('user login')


@login_required
def custom_dashboard(request):
    context = {}
    ch = RegisterTable.objects.filter(user__id=request.user.id)
    if len(ch) > 0:
        data = RegisterTable.objects.get(user__id=request.user.id)
        context['data'] = data
    return render(request, 'custom_dashboard.html', context)


@login_required
def seller_dashboard(request):
    context = {}
    ch = RegisterTable.objects.filter(user__id=request.user.id)
    if len(ch) > 0:
        data = RegisterTable.objects.get(user__id=request.user.id)
        context['data'] = data
    return render(request, 'seller_dashboard.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def edit_profile(request):
    context = {}
    ch = RegisterTable.objects.filter(user__id=request.user.id)
    if len(ch) > 0:
        data = RegisterTable.objects.get(user__id=request.user.id)
        context['data'] = data
    data = RegisterTable.objects.get(user__id=request.user.id)
    context['data'] = data
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        age = request.POST['age']
        city = request.POST['city']
        occupation = request.POST['occupation']
        gender = request.POST['gender']
        about = request.POST['about']
        user = User.objects.get(id=request.user.id)
        user.first_name = fname
        user.last_name = lname
        user.email = email
        user.save()
        data.phone = contact
        data.age = age
        data.city = city
        data.occupation = occupation
        data.gender = gender
        data.about = about
        data.save()
        print(request.FILES)
        if 'image' in request.FILES:
            img = request.FILES['image']
            print(img)
            data.profile_img = img
            data.save()
        context['status'] = 'Changes saved successfully !!!'
    return render(request, 'edit_profile.html', context)


def change_password(request):
    context = {}
    ch = RegisterTable.objects.filter(user__id=request.user.id)
    if len(ch) > 0:
        data = RegisterTable.objects.get(user__id=request.user.id)
        context['data'] = data
    if request.method == 'POST':
        current = request.POST['current_password']
        new_password = request.POST['new_password']
        user = User.objects.get(id=request.user.id)
        username = user.username
        check = user.check_password(current)

        if check == True:
            context['msg'] = 'Password changed successfully!!!'
            context['error'] = 'alert-success'
            # user=User.objects.filter(id=request.user.id)
            user.set_password(new_password)
            user.save()
            user = User.objects.get(username=username)
            login(request, user)
        else:
            context['msg'] = 'Incorrect your password'
            context['error'] = 'alert-danger'
    return render(request, 'change_password.html', context)


def add_product(request):
    context = {}
    ch = RegisterTable.objects.filter(user__id=request.user.id)
    if len(ch) > 0:
        data = RegisterTable.objects.get(user__id=request.user.id)
        context['data'] = data
    if request.method == 'POST':
        form = Add_ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            data.seller = user
            data.save()
            context['status'] = f'{data.product_name} added Successfully!!!'
    else:
        form = Add_ProductForm()
    context['form'] = form
    return render(request, 'addProduct.html', context)


def my_products(request):
    context = {}
    ch = RegisterTable.objects.filter(user__id=request.user.id)
    if len(ch) > 0:
        data = RegisterTable.objects.get(user__id=request.user.id)
        context['data'] = data
    ch = RegisterTable.objects.filter(user__id=request.user.id)
    if len(ch) > 0:
        data = RegisterTable.objects.get(user__id=request.user.id)
        context['data'] = data
    all = Add_Product.objects.filter(seller__id=request.user.id)
    context['products'] = all
    print(f"products {context.get('products')}")
    return render(request, 'myProduct.html', context)


def single_product(request):
    context = {}
    if "pid" in request.GET:
        proId = request.GET["pid"]
        data = Add_Product.objects.get(id=proId)
        context["product"] = data
        # print(f'proId {proId}')
    return render(request, 'single_product.html', context)


def update_product(request):
    context = {}
    cats = Category.objects.all().order_by('cat_name')
    context['cats'] = cats
    if 'pid' in request.GET:
        proId = request.GET['pid']
        # product = Add_Product.objects.get(id=proId)
        product = get_object_or_404(Add_Product, id=proId)
        # print(product)
        context['product'] = product
    if request.method == 'POST':
        p_name = request.POST['p_name']
        p_price = request.POST['p_price']
        s_price = request.POST['s_price']
        p_cat = request.POST['p_cat']
        p_det = request.POST['p_details']

        cat = Category.objects.get(id=p_cat)

        product.product_name = p_name
        product.product_category = cat
        product.product_price = p_price
        product.sale_price = s_price
        product.details = p_det
        product.save()
        if 'p_img' in request.FILES:
            img = request.FILES['p_img']
            product.product_img = img
            product.save()

        context['status'] = 'Product Changes Succesfully !!!'
    return render(request, 'update_product.html', context)


def delete_product(request):
    context = {}

    if "pid" in request.GET:
        proId = request.GET["pid"]
        proRemove = get_object_or_404(Add_Product, id=proId)
        context['product'] = proRemove

        if 'action' in request.GET:
            proRemove.delete()
            context['status'] = str(proRemove.product_name) + 'removed Successfully!!!'

    return render(request, 'delete_product.html', context)


def allProducts(request):
    context = {}
    cats = Category.objects.all().order_by('cat_name')
    context['categories'] = cats
    products = Add_Product.objects.all().order_by('product_name')
    context['products'] = products

    if request.method=='POST':
        proName=request.POST['pId']
        # data = Add_Product.objects.filter(product_name__contains=proName)
        data = Add_Product.objects.filter(Q(product_name__contains=proName) | Q(product_category__cat_name__contains=proName))
        context['products'] = data
        context['abcd'] = 'search'

    if 'cat' in request.GET:
        catId= request.GET['cat']
        products=Add_Product.objects.filter(product_category__id=catId)

        context['products'] = products
        context['abcd'] = 'search'

    return render(request, 'allProducts.html', context)


def sendEmail(request):
    context = {}
    if request.method=='POST':
        to=request.POST['to']
        subject= request.POST['subject']
        message= request.POST['msg']
        try:
            msg=EmailMessage(subject,message,to=[to])
            msg.send()
            context['status']= 'Successfully send message'
            context['col']="alert-success"
        except:
            context['status'] = 'Please check your internet or your email'
            context['col'] = "alert-danger"

    return render(request,'sendEmail.html',context)


def forgot_password(request):
    return render(request, 'forgot_password.html')

def reset_password(request):
    context = {}
    if request.method=='GET':
        un=request.GET['usern']
        user=get_object_or_404(User,username=un)
        context['user']=user
    # return render(request, 'reset_password.html')
    return HttpResponse(un)