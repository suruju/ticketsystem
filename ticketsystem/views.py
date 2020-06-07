from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Vehicle, VehicleCompany, Reservation, RouteDestination, Facility, SeatPlan
from .forms import VehicleForm, CreateVendorForm,CompanyprofileForm, ReservationForm, SeatPlanForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users, active_users
from django.db.models import Sum, DateField,Count
from django.db.models.functions import TruncMonth, ExtractMonth, ExtractYear, Cast
from datetime import date



#ADMIN PAGE =====================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def home(request):
    #LAST MONTH TICKET RESERVATION COUNT
    lastmonth=Reservation.objects.filter(departuredate__year=ExtractYear('departuredate'), departuredate__month=date.today().month-1).aggregate(total=Count('paymentmode'))
    #THIS MONTH TICKET RESERVATION COUNT
    thismonth=Reservation.objects.filter(departuredate__year=ExtractYear('departuredate'), departuredate__month=date.today().month).aggregate(total=Count('paymentmode'))
    #TICKET COUNTER PURCHASE COUNT
    offlinereserve=Reservation.objects.filter(paymentmode='Offline Payment').count()
    #ONLINE TICKET PURCHASE COUNT
    onlinereserve=Reservation.objects.filter(paymentmode='Online Payment').count()

    #OVERALL SALES GRAPH DONE USING THE SOFTWARE
    overallsalesG=Reservation.objects.annotate(month=ExtractMonth('departuredate'),year=ExtractYear('departuredate')).order_by().values('month', 'year').annotate(sales=Sum('totalprice')).values('month','year','sales')
    

    context={'lastmonth':lastmonth, 'thismonth':thismonth,'offlinereserve':offlinereserve, 'onlinereserve':onlinereserve,'overallsalesG':overallsalesG}
    return render(request,'ticketsystem/dashboard.html',context)

#ADMIN VENDOR PAGE
@allowed_users(allowed_roles=['Admin'])
def vendorlist(request):
    venlist=VehicleCompany.objects.all()
    context={'venlist':venlist}
    return render(request,'ticketsystem/vendorlist.html',context)


#ADMIN VENDOR COMPANY PAGE
@allowed_users(allowed_roles=['Admin'])
def viewCompany(request,pk):
    destinations=RouteDestination.objects.all()
    company=VehicleCompany.objects.get(id=pk)
    vehicles=Vehicle.objects.filter(vehicleowner=company.id)
    context={'company':company, 'vehicles':vehicles, 'destinations':destinations}
    return render(request,'ticketsystem/viewCompany.html',context)


#ADD NEW SEAT PLAN LAYOUT
@allowed_users(allowed_roles=['Admin']) 
def addseatlayout(request):
    form=SeatPlanForm()
    if request.method=='POST':
        form=SeatPlanForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('/seatplan/')
    
    context={'form':form}
    return render(request,'ticketsystem/seatplan.html',context)

@allowed_users(allowed_roles=['Admin'])
def updateseatPlan(request,pk):
    seat=SeatPlan.objects.get(id=pk)
    form=SeatPlanForm(instance=seat)
    if request.method=='POST':
        form=SeatPlanForm(request.POST,request.FILES,instance=seat)
        if form.is_valid:
            form.save()
            return redirect('/seatplan/')

    context={'form':form}
    return render(request, 'ticketsystem/seatplan.html',context)

@allowed_users(allowed_roles=['Admin','Vendor'])
def seatplanList(request):
    statusinfo=VehicleCompany.objects.get(user_auth=request.user)
    seats=SeatPlan.objects.all()
    context={'seats':seats,'statusinfo':statusinfo}
    return render(request,'ticketsystem/seatplanlist.html',context)



# VEHICLE SEGMENT
@active_users(allowed_user=['Active'])
def vehicles(request):
    vehicles=Vehicle.objects.all()
    context={'vehicles':vehicles}
    return render(request,'ticketsystem/vehicle_list.html',context)


@active_users(allowed_user=['Active'])
def userVehicles(request):
    statusinfo=VehicleCompany.objects.get(user_auth=request.user)
    vehicles=Vehicle.objects.filter(vehicleowner__user_auth=request.user)
    context={'vehicles':vehicles,'statusinfo':statusinfo}
    return render(request,'ticketsystem/user_vehicle.html',context)


@active_users(allowed_user=['Active'])
def addVehicle(request):
    route_location=RouteDestination.objects.all()
    statusinfo=VehicleCompany.objects.get(user_auth=request.user)
    form=VehicleForm()
    if request.method=='POST':
        form=VehicleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/uservehicle/')
    #print(route_permit)
    context={'form':form,'route_location':route_location,'statusinfo':statusinfo}
    return render(request,'ticketsystem/add_vehicle.html',context)

@active_users(allowed_user=['Active'])
def updateVehicle(request,pk):
    statusinfo=VehicleCompany.objects.get(user_auth=request.user)
    route_location=RouteDestination.objects.all()
    vehicle=Vehicle.objects.get(id=pk)
    form=VehicleForm(instance=vehicle)
    if request.method=='POST':
        form=VehicleForm(request.POST,request.FILES,instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('/uservehicle/')
    context={'form':form,'route_location':route_location,'vehicle':vehicle,'statusinfo':statusinfo}
    return render(request,'ticketsystem/updateVehicle.html',context)

@active_users(allowed_user=['Active'])
def deletevehicle(request,pk):
    vehicle=Vehicle.objects.get(id=pk)
    vehicle.delete()
    return redirect('/uservehicle/')
    # context={'vehicles':vehicles}
    # return render(request,'ticketsystem/user_vehicle.html',context)


@active_users(allowed_user=['Active'])
def viewvehicle(request,pk,cid=None):
    destination=RouteDestination.objects.all()
    vehicle=Vehicle.objects.get(id=pk)
    context={'vehicle':vehicle,'destination':destination}
    return render(request,'ticketsystem/viewvehicle.html',context)







#USER PROFILE SEGMENT
@active_users(allowed_user=['Active'])
def user(request,pk):
    user=VehicleCompany.objects.get(user_auth=pk)
    context={'user':user}
    return render(request,'ticketsystem/userprofile.html',context)

@allowed_users(allowed_roles=['Admin','Vendor'])
def update_profile(request,pk):
    profile=VehicleCompany.objects.get(id=pk)
    form=CompanyprofileForm(instance=profile)
    if request.method=='POST':
        form=CompanyprofileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/vendor_profile/19')
    context={'form':form}
    return render(request,'ticketsystem/update_profile.html',context)







#REGISTRATION PAGE
@unauthenticated_user
def registration(request):
    form=CreateVendorForm()
    if request.method=='POST':
        form=CreateVendorForm(request.POST)
        if form.is_valid():
            user=form.save()
            vendor=form.cleaned_data.get('first_name')+' '+form.cleaned_data.get('last_name')
            messages.info(request,'Account was created for ' + vendor)
            return redirect('/login/')
    context={'form':form}
    return render(request,'ticketsystem/registration.html',context)



#SUPER ADMIN LOGIN PAGE
@unauthenticated_user
def loginSuper(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Username OR Password is incorrect.')  

    context={}
    return render(request, 'ticketsystem/login.html', context)



#LOGIN PAGE
@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            statusinfo=VehicleCompany.objects.get(user_auth=request.user)
            print(statusinfo.account_status)
            if statusinfo.account_status == 'Active':
                return redirect('/vendor/')
            elif statusinfo.account_status == 'Deactivated':
                return redirect('/deactivated/')
            else:
                return redirect('/pending/')
        else:
            messages.info(request,'Username OR Password is incorrect.')  

    context={}
    return render(request, 'ticketsystem/login.html', context)


def deactivated(request):
    return render(request,'ticketsystem/deactivated.html')


def pending(request):
    return render(request, 'ticketsystem/pending.html')

# LOGOUT PAGE
def logoutUser(request):
    logout(request)
    return redirect('login') 

#RESET PASSWORD SEGMENT
def reset_password(request):
    context={}
    return render(request, 'ticketsystem/reset_password.html',context)





#VENDOR LOGGED IN DASHBOARD SEGMENT
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Vendor'])
def vendorPage(request):
    statusinfo=VehicleCompany.objects.get(user_auth=request.user)
    if statusinfo.account_status == 'Active':
        vehicles=Vehicle.objects.filter(vehicleowner__user_auth=request.user)
        #Monthly Overall Sales of the Vehicle
        monthlyvehicles = [{'vehicle_name':vehicle.vehicle_name,'monthwise': Reservation.objects.annotate(month=ExtractMonth('departuredate'),year=ExtractYear('departuredate')).filter(busName=vehicle.vehicle_name,departuredate__year=date.today().year).values('month','year').annotate(sale=Sum('totalprice')).values('month','sale','year').order_by('month')} for vehicle in vehicles]
        print(monthlyvehicles)
        

        
     
        #Previous Month Overall Sales of the Company
        previousmonthsales=Reservation.objects.filter(busid__vehicleowner__user_auth=request.user,departuredate__year=ExtractYear('departuredate'), departuredate__month=date.today().month-1).annotate(month=ExtractMonth('departuredate'),year=ExtractYear('departuredate')).order_by().values('month','year').aggregate(sales=Sum('totalprice'))
        
        
        #Monthly Overall Sales of the Company
        monthlyoverallsales=Reservation.objects.annotate(month=ExtractMonth('departuredate'),year=ExtractYear('departuredate')).filter(busid__vehicleowner__user_auth=request.user).order_by().values('month','year').annotate(sales=Sum('totalprice')).values('month','year','sales')
        #print(monthlyoverallsales)
        
        #Overall sales of the company
        overallsales=Reservation.objects.filter(busid__vehicleowner__user_auth=request.user).aggregate(overall=Sum('totalprice'))
        
        #Overall sales of the company in this Year till date
        overallsalesannum=Reservation.objects.filter(busid__vehicleowner__user_auth=request.user, departuredate__year=date.today().year).annotate(year=ExtractYear('departuredate')).aggregate(overall=Sum('totalprice'))
        
        #Overall sales of the company in Previous Year
        overallsalesprevannum=Reservation.objects.filter(busid__vehicleowner__user_auth=request.user, departuredate__year=date.today().year-1).annotate(year=ExtractYear('departuredate')).aggregate(overall=Sum('totalprice'))
        
        # Total sales according to the Bus Agent (ie Greenline Pvt. Ltd.)
        totalsales=[{'vehicle_name':vehicle.vehicle_name, 'salesrecord':Reservation.objects.filter(busName=vehicle.vehicle_name).aggregate(Sum('totalprice'))} for vehicle in vehicles] 
        cal={1,2,3,4,5,6,7,8,9,10,11,12}
        context={'totalsales':totalsales, 'overallsales':overallsales,'monthlyoverallsales':monthlyoverallsales,'monthlyvehicles':monthlyvehicles,'overallsalesannum':overallsalesannum,'previousmonthsales':previousmonthsales,'thisyear':date.today().year,'thismonth':date.strftime(date.today(), '%B'),'statusinfo':statusinfo,'cal':cal}
        
        return render(request,'ticketsystem/vendorDashboard.html',context)
    elif statusinfo.account_status == 'Deactivated':
        return redirect('/deactivated/')
    else:
        return redirect('/pending/')



#RESERVATION SEGMENT
@active_users(allowed_user=['Active'])
def newbooking(request):
    statusinfo=VehicleCompany.objects.get(user_auth=request.user)
    route_location=RouteDestination.objects.all()
    owner=VehicleCompany.objects.get(user_auth=request.user.id)
    vehicles=Vehicle.objects.filter(vehicleowner=owner.id)
    context={'vehicles':vehicles,'route_location':route_location,'statusinfo':statusinfo}
    return render(request,'ticketsystem/vehicleticket.html',context)
#Displaying list of vehicles and date selection for reservation

@active_users(allowed_user=['Active'])
def reservation(request,pk,rd):
    statusinfo=VehicleCompany.objects.get(user_auth=request.user)
    seat_booked=Reservation.objects.filter(departuredate=rd)
    route_location=RouteDestination.objects.all()
    vehicle_id=Vehicle.objects.get(id=pk)
    seats=SeatPlan.objects.get(formatname=vehicle_id.seatplan)
    form=ReservationForm(instance=vehicle_id)
    if request.method=='POST':
        form=ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/reservation-list/')
    context={'form':form,'route_location':route_location,'vehicle_id':vehicle_id,'rd':rd,'seats':seats,'seat_booked':seat_booked,'statusinfo':statusinfo}
    return render(request,'ticketsystem/reservation.html',context)


@active_users(allowed_user=['Active'])
def updatereservation(request,pk,rid,rd):
    statusinfo=VehicleCompany.objects.get(user_auth=request.user)
    seat_booked=Reservation.objects.filter(departuredate=rd)
    ticket=Reservation.objects.get(id=rid)
    vehicle_id=Vehicle.objects.get(id=pk)
    seats=SeatPlan.objects.get(formatname=vehicle_id.seatplan)
    form=ReservationForm(instance=ticket)
    if request.method=='POST':
        form=ReservationForm(request.POST,instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('/reservation-list/')
    context={'form':form,'vehicle_id':vehicle_id,'rd':rd,'seats':seats,'seat_booked':seat_booked,'statusinfo':statusinfo}
    return render(request,'ticketsystem/updatereservation.html',context)

#@active_users(allowed_user=['Active'])
@allowed_users(allowed_roles=['Admin','Vendor'])
def reservationList(request):

    if request.user.is_staff:
        booking=Reservation.objects.all()
        
    else:
        
        #booking=Reservation.objects.filter(busid__vehicleowner__user_auth=request.user)
        statusinfo=VehicleCompany.objects.get(user_auth=request.user)
        booking=Reservation.objects.select_related('busid').filter(busid__vehicleowner__user_auth=request.user)
    context={'booking':booking,'statusinfo':statusinfo}
    return render(request,'ticketsystem/reservationList.html',context)



def unauthorized(request):
    return render(request,'ticketsystem/unauthorized.html')
     