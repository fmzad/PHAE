from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dev-index'),
    path('page/xml', views.page_xml, name='dev-page-xml'),
]