from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Students
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def addData(request):
    return render(request,"add_data.html")

def add_student(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Now Allowed</h2>")
    else:
        # try:
        student=Students(name=request.POST.get('name',''),curso=request.POST.get('curso',''),colegio=request.POST.get('colegio',''),velocidad=request.POST.get('velocidad',''),resistencia=request.POST.get('resistencia',''))
        student.save()
        #     messages.success(request,'Agregado Exitosamente')
        # except:
        #     messages.error(request,'Error al agregar estudiante')
        return HttpResponseRedirect("/addData")

def show_all_data(request):
    all_student=Students.objects.all()

    return render(request,"show_data.html",{'students':all_student})

def delete_student(request,student_id):
    student=Students.objects.get(id=student_id)
    student.delete()
    # messages.error(request, "Deleted Successfully")
    return HttpResponseRedirect("/show_all_data")

def update_student(request,student_id):
    student=Students.objects.get(id=student_id)
    if student==None:
        return HttpResponse("Student Not Found")
    else:
        return render(request,"student_edit.html",{'student':student})

def edit_student(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        student=Students.objects.get(id=request.POST.get('id',''))
        if student==None:
            return HttpResponse("<h2>Student Not Found</h2>")
        else:
            student.name=request.POST.get('name','')
            student.curso=request.POST.get('curso','')
            student.colegio=request.POST.get('colegio','')
            student.velocidad=request.POST.get('velocidad','')
            student.resistencia=request.POST.get('resistencia','')
            student.save()

            # messages.success(request,"Updated Successfully")
            return HttpResponseRedirect("update_student/"+str(student.id)+"")

def LoginUser(request):
    #print(settings.SECRET_KEY)
    if request.user==None or request.user =="" or request.user.username=="":
        return render(request,"login_page.html")
    else:
        return HttpResponseRedirect("/homePage")

def RegisterUser(request):
    # if request.user==None:
        return render(request,"register_page.html")
    # else:
        # return HttpResponseRedirect("/homePage")

def SaveUser(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')

        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username,email,password)
            messages.success(request,"User Created Successfully")
            return HttpResponseRedirect('register')
        else:
            messages.error(request,"Email or Username Already Exist")
            return HttpResponseRedirect('register')

def DoLoginUser(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed")
    else:
        username=request.POST.get('username','')
        password=request.POST.get('password','')

        user=authenticate(username=username,password=password)

        if user!=None:
            login(request,user)
            return HttpResponseRedirect('/homePage')
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect('/login_user')

def HomePage(request):
    return render(request,"home_page.html")

def LogoutUser(request):
    logout(request)
    request.user=None
    return HttpResponseRedirect("/login_user")