from django.urls import path

from . import views

urlpatterns = [
    path('<int:page_id>', views.page_view, name="page-view"),
    path('all', views.page_all, name="page-all"),
    path('create', views.page_create, name="page-create"),
    path('edit/<int:page_id>', views.page_edit, name="page-edit"),
    path('move/<int:page_id>', views.page_move, name="page-move"),
    path('revisions/<int:page_id>', views.page_revisions_view, name="page-revisions"),
]