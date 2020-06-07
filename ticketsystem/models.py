from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



# Creating Company Name i.e. Vendor of software subscribers
class VehicleCompany(models.Model):
    ACTIVATION_STATUS=(
        ('Active','Active'),
        ('Pending','Pending'),
        ('Deactivated','Deactivated')
    )
    user_auth = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    company_name=models.CharField(max_length=100,db_index=True)
    authorizedperson=models.CharField(null=True, max_length=100, verbose_name='Authorized Person')
    address=models.CharField(max_length=200, db_index=True)
    company_info=RichTextField(blank=True, null=True)
    phone=models.CharField(max_length=20)
    account_status=models.CharField(max_length=20,choices=ACTIVATION_STATUS, default='Pending')
    companylogo=models.ImageField(null=True, blank=True, verbose_name='Company Logo')
    slug=models.SlugField(max_length=100,db_index=True, null=True)
    

    class Meta:
        ordering=('company_name',)
        verbose_name='company'
        verbose_name_plural='companies'

    def __str__(self):
        return str(self.user_auth)



# Adding Route Location for desitination name consistency
class RouteDestination(models.Model):
    destinationlocation=models.CharField(max_length=100)

    class Meta:
        ordering=('destinationlocation',)
        verbose_name='route'
        verbose_name_plural='routes'

    def __str__(self):
        return self.destinationlocation


# Adding Facility provided in the vehicle
class Facility(models.Model):
    ammenities=models.CharField(max_length=100)

    class Meta:
        ordering=('ammenities',)
        verbose_name='facility'
        verbose_name_plural='facilities'


    def __str__(self):
        return self.ammenities

class Category(models.Model):
    category=models.CharField(max_length=100)

    class Meta:
        ordering=('category',)
        verbose_name='category'
        verbose_name_plural='categories'


    def __str__(self):
        return self.category



#Seat Planning
class SeatPlan(models.Model):
    formatname=models.CharField(max_length=100, verbose_name='Name', null=True)
    seatformt=RichTextField(blank=True, null=True)
    seatlayoutimage=models.ImageField(null=True, blank=True, verbose_name='Seat Layout')

    class Meta:
        ordering=('formatname',)
    
    def __str__(self):
        return self.formatname



# Adding Vehicle of Vehicle's Company subscriber
class Vehicle(models.Model):
    vehicle_name=models.CharField(max_length=100, db_index=True, null=True)
    vehicle_number=models.CharField(max_length=20, null=True)
    facility=models.ManyToManyField(Facility)
    category=models.ForeignKey(Category, related_name='vehiclecategory', null=True, on_delete=models.SET_NULL)
    departurefrom=models.IntegerField(null=True)
    departureto=models.IntegerField(null=True)
    departuretime=models.TimeField()
    seatplan=models.ForeignKey(SeatPlan, null=True, on_delete=models.SET_NULL)
    seatcapacity=models.PositiveIntegerField(null=True)
    ticketprice=models.PositiveIntegerField()
    vehicleowner=models.ForeignKey(VehicleCompany,related_name='company', null=True, on_delete=models.SET_NULL)
    vehicle_photo=models.ImageField(null=True,blank=True)
    slug=models.SlugField(max_length=100,db_index=True, unique=True)
    boardingpointone=models.CharField(max_length=200,null=True, blank=True)
    boardingpointtwo=models.CharField(max_length=200,null=True, blank=True)
    boardingpointthree=models.CharField(max_length=200,null=True, blank=True)
    dropoffpointone=models.CharField(max_length=200,null=True, blank=True)
    dropoffpointtwo=models.CharField(max_length=200,null=True, blank=True)
    dropoffpointthree=models.CharField(max_length=200,null=True, blank=True)

    class Meta:
        ordering=('vehicle_name',)
        index_together=(('id','slug'))

    def __str__(self):
        return self.vehicle_name    



class Reservation(models.Model):
    MODE_OF_PAYMENT=(
        ('Online Payment','Online Payment'),
        ('Offline Payment','Offline Payment')
    )

    fullname=models.CharField(max_length=100, db_index=True)
    address=models.CharField(max_length=200, db_index=True)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    busid=models.ForeignKey(Vehicle,related_name='bus', null=True, on_delete=models.SET_NULL)
    busName=models.CharField(max_length=100, null=True)
    departurefrom=models.CharField(max_length=100,null=True)
    departureto=models.CharField(max_length=100, null=True)
    departuredate=models.DateField()
    departuretime=models.TimeField()
    seatnumber=models.CharField(max_length=200)
    totalprice=models.PositiveIntegerField(default=0)
    paymentmode=models.CharField(max_length=50,choices=MODE_OF_PAYMENT)

    class Meta:
        ordering=('-departuredate',)
        

    def __str__(self):
        return self.fullname
  
