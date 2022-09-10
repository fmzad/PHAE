from django.shortcuts import render
from django.http import HttpResponse
from page.models import Page

# Create your views here.
def index(request):
    return render(request, 'dev_index.html')

def page_xml(request):
    from django.core import serializers
    data = serializers.serialize('xml', Page.objects.all())
    return HttpResponse(data, content_type='text/xml')