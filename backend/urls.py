from django.contrib import admin
from django.urls import path, include
from tickets import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/fbvlist/', views.FBV_List)
]
