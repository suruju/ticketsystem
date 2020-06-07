from django.contrib import admin
from .models import Vehicle, VehicleCompany, Reservation, RouteDestination, Facility, Category, SeatPlan



class VehicleCompanyAdmin(admin.ModelAdmin):
    list_display= ['authorizedperson','company_name','phone','account_status']
    list_filter=['company_name','account_status']
    list_editable=['account_status',]
    prepopulated_fields={'slug':('company_name',)}


class VehicleAdmin(admin.ModelAdmin):
    list_display=['vehicle_name','category','departuretime','seatcapacity','ticketprice']
    list_filter=['vehicle_name','category','departuretime','ticketprice']
    list_editable=['category','seatcapacity','ticketprice']
    prepopulated_fields={'slug':('vehicle_name',)}


class ReservationAdmin(admin.ModelAdmin):
    list_display=['fullname','departurefrom','departureto','departuredate','paymentmode']
    list_filter=['fullname', 'departurefrom','departuredate','paymentmode']
    list_editable=['departurefrom','departureto']  


admin.site.register(VehicleCompany,VehicleCompanyAdmin)
admin.site.register(RouteDestination)
admin.site.register(Facility)
admin.site.register(Category)
admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(SeatPlan)