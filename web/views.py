from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from web.models import *
import datetime
# Create your views here.

def main(request):
    return render(request, 'login.html')

def user_register(request):
    return render(request, 'register.html')


def authentication_login(request):

    username = request.POST['username']
    password = request.POST['password']

    # try:
    ob = Logins.objects.get(usernames=username, password=password)

    if ob is not None:
        if ob.user_type=='admin':
            return redirect('admin_pg')
        elif ob.user_type=='user':
            request.session['lid'] = ob.id
            return redirect('users_home')
    
    # except:
    #     return HttpResponse('''<script>alert('username or password mismatched');window.location="/"</script>''')


#admin dashboard
def admin_dashboard(request):
    return render(request, 'admin/admin_dash.html')


#admin home page
def admin_pg(request):
    ob = Products.objects.all()
    return render(request, 'admin/admin_index.html', {'val': ob})


#admin manage product page
def admin_manage_product(request):
    ob = Products.objects.all()
    return render(request, 'admin/manage.html', { 'val' : ob})

#admin product_adding page
def admin_product_adding(request):
    return render(request, 'admin/adding.html')


#adding to product table
def product_add(request):
    name = request.POST['product_name']
    description = request.POST['description']
    price = request.POST['price']
    image = request.FILES['file']
    fs = FileSystemStorage()
    fp = fs.save(image.name, image)

    ob = Products()
    ob.name = name
    ob.image = image
    ob.description = description
    ob.price = price
    ob.save()

    return HttpResponse('''<script>alert("success");window.location="/admin_manage_product"</script>''')


#update product deatils
def update_product(request,id):
    ob = Products.objects.get(id=id)
    request.session['sid'] = id
    return render(request, 'admin/update.html', {'val': ob})

#updating existing product
def update_pdt(request):

    try:
        name = request.POST['product_name']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']
        fs = FileSystemStorage()
        fp = fs.save(image.name, image)
    
        iob = Products.objects.get(id=request.session['sid'])
        iob.name = name
        iob.image = image
        iob.description = description
        iob.price = price
        iob.save()

        return HttpResponse('''<script>alert("success");window.location="/admin_manage_product"</script>''')

    except:
        name = request.POST['product_name']
        description = request.POST['description']
        price = request.POST['price']

        iob = Products.objects.get(id=request.session['sid'])
        iob.name = name
        iob.description = description
        iob.price = price
        iob.save()

        return HttpResponse('''<script>alert("success");window.location="/admin_manage_product"</script>''')


#deleting existing product
def delete_product(request, id):

    iob = Products.objects.get(id=id)
    iob.delete()

    return HttpResponse('''<script>alert("success");window.location="/admin_manage_product"</script>''')


# -------------------------------------------------------------------------------------------------------------------

#user registeration
def insert_user(request):

    name = request.POST['user_name']
    address = request.POST['address']
    phone = request.POST['phone']
    username = request.POST['username']
    password = request.POST['password']

    ob = Logins()
    ob.usernames = username
    ob.password = password
    ob.user_type = 'user'
    ob.save()

    iob = Users()
    iob.user_id = ob
    iob.name = name
    iob.address = address
    iob.phone = phone
    iob.save()

    return HttpResponse('''<script>alert("success");window.location="/"</script>''')


#users home page
def users_home(request):
    ob = Products.objects.all()
    return render(request, 'user/user_index.html', {'val': ob})

#user dashboard
def users_dashboard(request):
    return render(request, 'user/user_dashboard.html')

#product cartlist
def product_cartlist(request, id):
    ob = Products.objects.get(id=id)
    request.session['sid'] = id
    return render(request, 'user/product_cart.html', {'val': ob})

#product cart order
def product_order(request):
    ob=Cart.objects.all()
    print(len(ob),ob)
    ob = Cart.objects.filter(user_id__user_id__id=request.session['lid'])
    print(len(ob),ob,request.session['lid'])
    quantity = request.POST['quantity']
    product_id = Products.objects.get(id= request.session['sid'])
    if len(ob)>0:
        ob=ob[0]
    else:
        ob= Cart()
        ob.user_id = Users.objects.get(user_id__id=request.session['lid'])
        ob.date = datetime.datetime.today() 
        ob.amount = 0
        ob.save()
    iob = CartList()
    iob.cart_id = ob
    iob.product_id = product_id
    iob.quantity =quantity
    iob.save()
    p=int(product_id.price)*int(quantity)
    print(ob.amount,"=====================")
    ob.amount=int(ob.amount)+int(p)
    print(ob.amount,"===========================")
    ob.save()
    

    return HttpResponse('''<script>alert("success");window.location="users_home"</script>''')

#cartlist view
def view_cartlist(request):
    ob=CartList.objects.filter(cart_id__user_id__user_id__id=request.session['lid'])
    amt="0"
    if len(ob)>0:
        amt=ob[0].cart_id.amount
    return render(request, 'user/order_amt.html', {'val': ob,"amt":amt})

#cartlist remove item
def removes(request,id):
    ob = CartList.objects.get(id=id)
    print(ob)
    p=ob.quantity*ob.product_id.price
    ob1=ob.cart_id
    ob1.amount=ob1.amount-p
    ob1.save()
    ob.delete()
    
    return HttpResponse('''<script>alert("success");window.location="/view_cartlist"</script>''')

