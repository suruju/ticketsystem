from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    #path('',views.ViewPDF.as_view(),name='pdf_view'),
    path('<str:pk>/',views.viewpdf,name='pdf_view'),
]