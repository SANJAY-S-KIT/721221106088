from django.urls import path
from .import views
urlpatterns = [
     path('',views.getData),
     path('',views.getDataProduct),
     path('update',views.saveData),
     path('update',views.saveDataProduct),
 ]