from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template.loader import get_template
from .utils import render_to_pdf
from ticketsystem.models import Reservation
from num2words import num2words
# Create your views here.




# class ViewPDF(View):
#     def get(self, request, *args, **kwargs):
#         print(request)
#         pdf=render_to_pdf('pdf/invoice_template.html',data)
#         return HttpResponse(pdf, content_type='application/pdf')

# data = Reservation.objects.filter(id=5).values().first()
#print(data)

def viewpdf(request,pk):
    data = Reservation.objects.filter(id=pk).values().first()
    vehicle = Reservation.objects.select_related('busid').filter(id=pk)
    inword=num2words(data['totalprice'])
    totalamt=data['totalprice']/1.13
    vatamt=totalamt*0.13
    context={'data':data,'inword':inword,'vehicle':vehicle,'totalamt':totalamt,'vatamt':vatamt}
    pdf=render_to_pdf('pdf/invoice_template.html',context)
    return HttpResponse(pdf, content_type='application/pdf')

    

def index(request):
	context = {}
	return render(request, 'app/index.html', context)