from urllib import request
from django.forms import forms
from django.http import HttpResponseRedirect
from home.models import message
from django.shortcuts import HttpResponsePermanentRedirect

# def messages(request):
#     if request.method == 'POST':
#         form = messages(request.POST)
#         if form.is_valid():
#             # process form data
#             obj = message() #gets new object
#             obj.name = form.cleaned_data['name']
#             obj.email = form.cleaned_data['email']
#             obj.phone = form.cleaned_data['phone']
#             obj.msg = form.cleaned_data['msg']
#             #finally save the object in db
#             obj.save()
#             return HttpResponseRedirect('/')