from django.db import models

# Create your models here.
class admins(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    phone=models.PositiveBigIntegerField()
    password=models.CharField(max_length=20)


    def __str__(self):
        return self.fname+' '+self.lname

class hostels(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

depts=[
    ('CSE','CSE'),('ISE','ISE'),('EC','EC'),('EEE','EEE'),('MECHANICAL','MECHANICAL'),('CIVIL','CIVIL'),
]

class students(models.Model):
    fname=models.CharField(max_length=255)
    mname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    father=models.CharField(max_length=255)
    mother=models.CharField(max_length=255)
    phone=models.PositiveBigIntegerField()
    dept=models.CharField(max_length=50,choices=depts,verbose_name="Department")
    jyear=models.DateField()
    room_no=models.PositiveIntegerField()
    hostel_id=models.ForeignKey(hostels,on_delete=models.CASCADE)

    def __str__(self):
        return self.fname+' '+self.lname

relation=[
    ('Father','Father'),('Mother','Mother'),('Brother/Sister','Brother/Sister'),('Guardian','Guardian')
]

class visitors(models.Model):
    name=models.CharField(max_length=255)
    date=models.DateField()
    student_id=models.ForeignKey(students,on_delete=models.CASCADE)
    relationship=models.CharField(max_length=100,choices=relation,verbose_name="Relationship")
    in_time=models.TimeField()
    out_time=models.TimeField()

    def __str__(self):
        return self.name

class warden(models.Model):
    name=models.CharField(max_length=255)
    dob=models.DateField()
    phone=models.PositiveBigIntegerField()
    mail=models.EmailField()
    hostel_id=models.ForeignKey(hostels,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name