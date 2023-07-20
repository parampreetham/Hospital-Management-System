from django.shortcuts import render,redirect
from .models import admins,hostels,students,visitors,warden
from .forms import studentForm,visitorsForm,hostelForm


def home(request):
    if request.method=='POST':
        phone=request.POST['phone']
        password=request.POST['password']
        try:

            user=admins.objects.get(phone=phone,password=password)

            return redirect('admin_panal',phone)
        except:
            print('error')
        
    else:
        print('invalid')
    return render(request,'home.html')

def signup(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        password=request.POST['password']
        conpassword=request.POST['conpassword']
        

        if password==conpassword:
            if admins.objects.filter(phone=phone).exists():
                print('username Taken')
            else:
                user=admins.objects.create(fname=fname,lname=lname,password=password,phone=phone)
                # user.save()
                return redirect('home')

    return render(request,'signup.html')
   

def admin_panal(request,phone):
    User=admins.objects.get(phone=phone)
    hostel=hostels.objects.all()
    return render(request,'admin.html',{'User':User,'hostel':hostel})


def students_list(request,host_id):
    warden_details=warden.objects.get(hostel_id=host_id)
    student=students.objects.filter(hostel_id=host_id).values()
    count=student.count()
    return render(request,'students.html',{'student_list':student,'count':count,'host_id':host_id,'warden':warden_details})

def student_delete(request,student_id):
    student=students.objects.get(id=student_id)
    hostel_id=hostels.objects.get(name=student.hostel_id).pk
    student.delete()

    return redirect('students_list',hostel_id)

def view_edit_student(request,student_id):

    student_info=students.objects.get(id=student_id)
    hostel_id=hostels.objects.get(name=student_info.hostel_id).pk
    form = studentForm(request.POST or None,instance=student_info)
    if form.is_valid():
        form.save()
        return redirect('students_list',hostel_id)
    # return redirect('patients_list')
    return render(request,'view_edit_student.html',{'form':form,'host_id':hostel_id,'student_info':student_info})

def add_student(request,host_id):
    if request.method=="POST":
        form = studentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('students_list',host_id)
    form = studentForm
    return render(request,'add_student.html',{'form':form,'host_id':host_id})

def visitors_list(request,student_id):
    visitor_list=visitors.objects.filter(student_id=student_id).values()
    host_id=students.objects.get(id=student_id).hostel_id.pk
    count=visitor_list.count()
    return render(request,'visitors_list.html',{'visitors_list':visitor_list,'count':count,'student_id':student_id,'host_id':host_id})

def view_edit_visitor(request,visitor_id):
    visitor_info=visitors.objects.get(id=visitor_id)
    student_id=visitor_info.student_id.pk
    form = visitorsForm(request.POST or None,instance=visitor_info)
    if form.is_valid():
        form.save()
        return redirect('visitors_list',student_id)
    return render(request,'view_edit_visitor.html',{'form':form,'visitor_info':visitor_info,'student_id':student_id})

def add_visitors(request,student_id):
    if request.method=="POST":
            form = visitorsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('visitors_list',student_id) #host_id
    form = visitorsForm
    return render(request,'add_visitors.html',{'form':form,'student_id':student_id})

def visitor_delete(request,visitor_id):
    visitor=visitors.objects.get(id=visitor_id)
    student_id=visitor.student_id.pk
    visitor.delete()

    return redirect('visitors_list',student_id)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def add_hostel(request,phone):
    if request.method=="POST":
        form = hostelForm(request.POST,request.FILES)
        print('ok')
        if form.is_valid():
            print('pass')
            form.save()
            return redirect('admin_panal',phone)
    form = hostelForm
    return render(request,'add_hostel.html',{'form':form})

def search(request):
    name=request.GET['name']
    
    host_id=request.GET['host_id']
    warden_details=warden.objects.get(hostel_id=host_id)
    student=students.objects.filter(fname=name,hostel_id=host_id).values() 
    try:
        room_no=int(name)
        print(room_no)
        student=students.objects.filter(room_no=room_no,hostel_id=host_id).values()
    except:
        pass
    
    return render(request,'students.html',{'student':student,'host_id':host_id,'warden':warden_details})