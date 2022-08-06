from codecs import namereplace_errors
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.listBook, name='list'),
    path('autherlist', views.listAuther, name='autherlist'),
    path('detail <int:pk>/', views.bookdetail, name='detail'),
    path('autherdetails <int:pk>/', views.autherdetail, name='autherdetails'),
    path('bookinsert', views.bookinsert, name='bookinsert'),
    path('autherinsert', views.autherinsert, name='autherinsert'),
    path('bookupdate <int:pk>/', views.bookupdate, name='bookupdate'),
    path('autherupdate <int:pk>/ ', views.autherupdate, name='autherupdate'),
    path('bookdelete/<int:pk>/', views.bookdelete, name='bookdelete'),
    path('autherdelete/<int:pk>/', views.autherdelete, name='autherdelete'),
]
