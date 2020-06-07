from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.home,name='home'),

# VEHICLE SEGMENT
    path('vehicles/',views.vehicles,name='vehicles'),
    path('addVehicle/',views.addVehicle,name='addVehicle'),
    path('updateVehicle/<str:pk>/',views.updateVehicle,name='updateVehicle'),
    path('viewvehicle/<str:pk>/',views.viewvehicle,name='viewvehicle'),
    path('viewvehicle/<str:pk>/<str:cid>/',views.viewvehicle,name='viewvehicle'),
    path('deleteVehicle/<str:pk>/',views.deletevehicle,name='deleteVehicle'),

#VENDOR AUTHENTICATION PAGE
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('registration/',views.registration,name='registration'),
    path('deactivated/',views.deactivated,name='deactivated'),
    path('pending/',views.pending,name='pending'),
    path('unauthorized/',views.unauthorized),


#RESET PASSWORD SEGMENT
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='ticketsystem/reset_password.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='ticketsystem/reset_password_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='ticketsystem/reset_password_complete.html'), name='password_reset_complete'),

#VENDOR SEGMENT
    path('vendor/',views.vendorPage,name='vendor'),
    path('vendor_profile/<str:pk>/',views.user,name='vendor_profile'),
    path('update_profile/<str:pk>/',views.update_profile,name='update_profile'),
    path('uservehicle/', views.userVehicles, name='uservehicle'),


#RESERVATION SEGMENT
    path('newbooking/', views.newbooking,name='newbooking'),
    path('reservation/<str:pk>/<str:rd>/',views.reservation,name='reservation'),
    path('updatereservation/<str:pk>/<str:rid>/<str:rd>/',views.updatereservation,name='updatereservation'),
    path('reservation-list/',views.reservationList,name='reservation-list'),

#CKEDITOR FOR FILE UPLOAD USUAGE   




#ADMIN AUTHENTICATION PAGE
    path('super/',views.loginSuper, name='super'),
    path('vendorlist/',views.vendorlist,name='vendorlist'),
    path('viewcompany/<str:pk>/',views.viewCompany,name='viewcompany'),
    path('addseatplan/',views.addseatlayout, name='addseatplan'),
    path('updateseatplan/<str:pk>/',views.updateseatPlan, name='updateseatplan'),
    path('seatplan/',views.seatplanList, name='seatplan'),



]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
