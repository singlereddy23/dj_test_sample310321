from django.http import HttpResponse
from django.shortcuts import render
import os

file_path=os.path.abspath(__file__)
pro11_dir_path=os.path.dirname(file_path)
dir_path=os.path.dirname(pro11_dir_path)

def html_respo(request):
    file_addr=os.path.join(dir_path,"sample.html")
    fp=open(file_addr,"r")
    data=fp.read()
    return HttpResponse(data)

def rend_demo(request):
        return render(request,"sample.html")