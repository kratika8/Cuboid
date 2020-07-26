from django.shortcuts import get_object_or_404,HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# relative import of forms
from .models import Cuboid
from .forms import CuboidForm

def index(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["psw"]
        user = User.objects.create_user(username = username , email = email , password = password)

        user.save()
        print("usercreated")
        messages.info(request, "Registered Successfully. Please Login")
        return render(request, "register.html")
    else:
        return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["psw"]
        user = auth.authenticate(username = username ,password = password )
        if user is not None :
            auth.login(request, user)
            return render(request, "home.html")
        else :
            messages.info (request ,'invalid credentials')

    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return render(request, "home.html")


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = CuboidForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "add.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Cuboid.objects.all()
    return render(request, "listAll.html", context)


def detail_view(request,id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Cuboid.objects.get(id = id)
    print(id)
    print(context)

    return render(request, "detail_view.html", context)


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Cuboid, id=id)

    # pass the object as instance in form
    form = CuboidForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/list")

        # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Cuboid, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)
# import csv, io
#
# from django.contrib import messages
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Cuboid
# from django.http import HttpResponse
# from django.db.models import Q
# import pandas as pd
# import os
# from .forms import CuboidForm
# from django.http import HttpResponseRedirect
#
#
#
# def index(request):
#     return render(request, 'home.html')
#
# def car_upload(request):
#     template = "cars.html"
#     prompt = {
#         'order': ' '
#     }
#     if request.method == "GET":
#         return render(request, template, prompt)
#
#     csv_file = request.FILES['file']
#     dfs = pd.read_csv(csv_file)
#     dfs = pd.DataFrame(dfs)
#     dfs['Date of Purchase'] = pd.to_datetime(dfs['Date of Purchase'] )
#     dfs['Date of Purchase'] = dfs['Date of Purchase'].dt.date
#     for i in range(len(dfs)) :
#         Cuboid.objects.update_or_create(
#         sales_id= dfs.iloc[i, 0],
#         pub_date= dfs.iloc[i, 1],
#         Customer_id=dfs.iloc[i, 2],
#         Fuel=dfs.iloc[i, 3],
#         VEHICLE_SEGMENT=dfs.iloc[i, 4],
#         SellingPrice=dfs.iloc[i, 5],
#         Power_steering=dfs.iloc[i, 6],
#         airbags= dfs.iloc[i, 7],
#         sunroof=dfs.iloc[i, 8],
#         Matt_finish= dfs.iloc[i, 9],
#         music_system= dfs.iloc[i, 10],
#         Customer_Gender=dfs.iloc[i, 11],
#         Customer_Incomegroup=dfs.iloc[i, 12],
#         Customer_Region=dfs.iloc[i, 13],
#         Customer_Marital_status=dfs.iloc[i, 14],
#         )
#
#     context = {}
#     return render(request, template, context)
#
# def fetch(request):
#     all_cars = Cuboid.objects.all()
#     return render(request, "index.html", {'ListCars':all_cars})
#
#
# def searchposts(request):
#     if request.method == 'POST':
#
#         srch = request.POST['srh']
#         if srch:
#             match = Cuboid.objects.filter(Q(sales_id__icontains=srch) | Q(Customer_id__icontains=srch))
#
#             if match:
#                 return render(request, "listAll.html", {'sr': match})
#             else:
#                 messages.error(request, 'no result found')
#         else:
#             return HttpResponseRedirect('/seachdata/')
#
#     return render(request, 'listAll.html')
#
#
# def addData(request):
#     return render(request, 'add.html')
#
# def submitadd(request):
#     length  = request.POST['length']
#     breadth = request.POST['breadth']
#     height = request.POST['height']
#
#     data_put = Cuboid(length=length, breadth=breadth, height=height)
#
#     data_put.save()
#     return render(request, 'add.html')

# def update_view(request, sales_id):
#     obj = get_object_or_404(Cars, sales_id=sales_id)
#     form = CarsForm(request.POST or None, instance = obj)
#     if form.is_valid():
#         form.save()  
#         return redirect(sales_id+'/update_view/') 
#     else:
#         form = CarsForm(instance=obj)
#     context = {'form' : form } 
#     return render(request, "update_view.html", context)