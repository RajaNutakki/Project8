from typing import Dict

from django.db.models import QuerySet
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Product
class HomeView(View):
    def get(self,request):
        return render(request,template_name='home.html')
class InsertInput(View):
    def get(self,request):
        return render(request,template_name='productinput.html')
class InsertView(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p_name=request.GET["t2"]
        p_cost=float(request.GET["t3"])
        p_mfdt=request.GET["t4"]
        p_expdt=request.GET["t5"]
        p1=Product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        resp=HttpResponse("product inserted successfully")
        return resp
class DisplayView(View):
    def get(self,request):
        qs=Product.objects.all()
        con_dic={"records":qs}
        return render(request,template_name="display.html")
class DeleteInputView(View):
    def get(self,request):
        return render(request,template_name="deleteinput.html")
class DeleteView(View):
    def get(self,request):
        P_id=int(request.GET["t1"])
        prod=Product.objects.filter(pid=P_id)
        prod.delete()
        resp=HttpResponse("product successfully deleted")
        return resp
class UpdateInputView(View):
    def get(self,request):
        return render(request,template_name="updateinput.html")
class UpdateView(View):
    def get(self,request):
        P_id=int(request.POST["t1"])
        P_name=request.POST["t2"]
        P_cost=float(request.POST["t3"])
        P_mfdt=request.POST["t4"]
        P_expdt=request.POST["t5"]
        prod=Product.objects.get(pid=P_id)
        prod.pname=P_name
        prod.pcost=P_cost
        prod.pmfdt=P_mfdt
        prod.pexpdt=P_expdt
        prod.save()
        resp=HttpResponse("Product updated Successfully")
        return resp
