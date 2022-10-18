from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import loader
from . models import saveMessage

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def savemsg(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message = request.POST.get('msg')
    s_data = saveMessage(name=name, email=email, phone=phone, msg=message)
    s_data.save()

  return render(request, 'contact.html')

# services page links=============================
def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def ad(request):
  template = loader.get_template('services/android_development.html')
  return HttpResponse(template.render())

def dm(request):
  template = loader.get_template('services/digital_Marketing.html')
  return HttpResponse(template.render())

def gd(request):
  template = loader.get_template('services/graphic_design.html')
  return HttpResponse(template.render())

def gyb(request):
  template = loader.get_template('services/Grow_your_business.html')
  return HttpResponse(template.render())

def ld(request):
  template = loader.get_template('services/logo_designing.html')
  return HttpResponse(template.render())

def mad(request):
  template = loader.get_template('services/mobile_app_development.html')
  return HttpResponse(template.render())

def wd(request):
  template = loader.get_template('services/web_development.html')
  return HttpResponse(template.render())

def wm(request):
  template = loader.get_template('services/website_maintenance.html')
  return HttpResponse(template.render())
