from django.shortcuts import render
from . model import Info
from django.http import HttpResponse

# Create your views here.
def demo(request):
#     movie = Info.objects.all()
#     context={
#         'movie_list':movie
#     }
#     return render(request,"index.html",context)
return HttpResponse("hello")



