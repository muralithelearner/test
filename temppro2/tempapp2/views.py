from django.shortcuts import render,redirect
from .models import Boysdata,Service,Hostelboysdata
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
# authenticate (validation purpose) if u set the login and logout must import above the code
from django.contrib.auth.decorators import login_required
from tempapp2.models import *   #not required because of all filters are not apply in search box


def homePage(request):
    if request.method == 'GET':
        service = Service.objects.all()
        return render(request,'homepage.html',{'service':service})
    
@login_required(login_url='login')
def studentsPage(request):
    if request.method =='GET':  #get the empty form means search box
        students = Boysdata.objects.all()
        return render(request,'student.html',{'key':students})
    else:
        living = request.POST.get('living_purpose')
        students = Boysdata.objects.filter(living_purpose = living )

        # occupation=request.POST.get('occupation')   #post  the search data and store in occupation
        # students = Boysdata.objects.filter(occupation=occupation)  # get the data what u want and stored in student
    
        # sharig_required=(request.POST.get('sharig_required')) 
        # if sharig_required is not None:
        #     sharig_required=int(sharig_required)
        #     students = Boysdata.objects.filter(sharig_required=sharig_required)

        return render(request,'student.html',{'key':students})     #display the data in sudent.html
        
        

# def servicePage(request):
#     return render(request,'servicePage.html')

@login_required(login_url='login')   
def Upservice(request):
    if request.method == 'GET':
        return render(request,'upservice.html')
    else:
        Service(
            shift =request.POST['shf'],
            monday =request.POST['mon'],
            tuesday = request.POST['tue'],
            wednesday =request.POST['wed'],
            thursday =request.POST['thu'],
            friday =request.POST['fri'],
            saturaday =request.POST['sat'],
            sunday =request.POST['sun'],
        ).save()
        return redirect(editservice)
    
@login_required(login_url='login') 
def editservice(request):
    service = Service.objects.all()
    return render(request,'editservice.html',{'service':service})

# @login_required(login_url='login') 
def contactPage(request):
    if request.method == 'GET':     # Here request method get it collect the empty form from the contactPage
        return render(request,'contactPage.html')
    else:
        Boysdata(  # This is working as like a dictonary
        name = request.POST['fname'],
        from_city=request.POST['from'],  
        living_purpose =request.POST['pur'],
        occupation=request.POST['ocp'],
        starting_date=request.POST['jdt'],
        sharig_required=request.POST['reqd']            
        ).save()
        return redirect(homePage)
        # return HttpResponse('Your data was saved succefully')


@login_required(login_url='login') 
def updateserv(request, id):
    update = Service.objects.get(id=id)
    return render(request,'updateserv.html',{'update':update})
#get the required data and set to the html page

@login_required(login_url='login') 
def updating_data(request,id):
    update = Service.objects.get(id=id)
    update.shift =request.POST['shf']
    update.monday =request.POST['mon']
    update.tuesday = request.POST['tue']
    update.wednesday =request.POST['wed']
    update.thursday =request.POST['thu']
    update.friday =request.POST['fri']
    update.saturaday =request.POST['sat']
    update.sunday =request.POST['sun']
    update.save()
    return redirect(editservice)


@login_required(login_url='login') 
def deleting_data(request, id):
    delete =  Service.objects.get(id=id)
    delete.delete()
    return redirect(editservice)


@login_required(login_url='login') 
def stu_delete(request,id):
    delete =Boysdata.objects.get(id=id)
    delete.delete()
    return redirect(studentsPage)


def login_page(request):
    if request.method =='GET':
        return render(request,'loginpage.html')
    else:    #(else means always post)
        user =request.POST['uname']
        pwd = request.POST['psw']
        user = authenticate(username=user,password=pwd)
        if user is not None:
            login(request,user)
            return redirect(studentsPage)
        else:
            return HttpResponse('Invalid user name or password')
        
def logout_page(request):
    logout(request)
    return redirect(login_page)

@login_required(login_url='login')
def hostelform(request):
    if request.method =='GET':
        return render(request,'boysdata.html')
    else:
        Hostelboysdata(
            name = request.POST['name'],
            mobile = request.POST['mbl'],
            email = request.POST['email'],
            block =request.POST['block'],
            share_members =request.POST['members'],
            room_no =request.POST['reqd'],
            joining_date =request.POST['jdt'],
            rent =request.POST['rent'],
            image =request.FILES['image']
        ).save()
        return redirect(hosteldata)

@login_required(login_url='login')
def hosteldata(request):
    hostel = Hostelboysdata.objects.all() 
    return render(request,'hosteldata.html',{'hostel':hostel}) 
        

   
