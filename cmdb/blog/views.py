#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import *
from django import forms

#class UploadFile(models.Model):
#  upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
#class UploadFileForm(forms.ModelForm):
#  class Meta:
#    model = UploadFile


def index(request):
  return render(request,"index.html")

def postok(request):
  return render(request,"postok.html")

def upload(request):
  if request.method == 'POST':
    data_post_upload = UploadFileForm(request.POST,request.FILES)
    #判断上传数据是否合法
    if data_post_upload.is_valid():
    #  return HttpResponse(data_post_upload)
      data_post_upload.save()
      return HttpResponseRedirect('/postok/')
    else:
      return HttpResponse('upload error')
  else:
    data_post_upload = UploadFileForm()
  return render(request,'upload.html',{'data_post_upload':data_post_upload},)
#def handle_upload_file(f):

def right(request):
  if request.method == 'POST':
     data_post_save = CmdbInfoForm(request.POST)
     if data_post_save.is_valid():
       ip = data_post_save.cleaned_data['ip']
       data_post_save.save()
       return HttpResponseRedirect('/postok/')
     else:
       return HttpResponse('save error')
  else:
    data_post_save = CmdbInfoForm()
  data_get=CmdbInfo.objects.all()
  return render(request,'right.html',{'data_get':data_get,'data_post_save':data_post_save})

def left(request):
  return render(request,"left.html")

