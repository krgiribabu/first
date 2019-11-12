from django.shortcuts import render
from django.views.generic.base import View
from .models import Employee
from django.core.serializers import serialize
from django.http import HttpResponse

class ReadOneEmployee(View):
    def get(self,request,emp_idno):
        res=Employee.objects.get(idno=emp_idno)
        json_data=serialize("json",[res])
        return HttpResponse(json_data,content_type="application/json")
