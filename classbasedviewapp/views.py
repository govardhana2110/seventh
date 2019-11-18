from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
class getinput(View):
    def get(self,request):
        return render(request,'get.html')
class postinput(View):
    def get(self,request):
        return render(request,'post.html')
class add(View):
    def get(self,request):
        try:
            a = request.GET['t1']
            b = request.GET['t2']
            x= int(a)
            y = int(b)
            z = x + y
            return HttpResponse("""<html><body bgcolor=green>sum is:""" + str(z)+ """</body></html>""")
        except(ValueError):
            return HttpResponse("invalid input")

    def post(self, request):
        try:
            a = request.POST['t1']
            b = request.POST['t2']
            x = int(a)
            y = int(b)
            z = x + y
            return HttpResponse("""<html><body bgcolor=green>sum is:""" + str(z) + """</body></html>""")
        except(ValueError):
            return HttpResponse("invalid input")



