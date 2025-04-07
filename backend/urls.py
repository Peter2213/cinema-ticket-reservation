from django.contrib import admin
from django.urls import path, include
from tickets import views 
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('guest', views.GuestViewSet, basename='guest')
router.register('movie', views.MovieViewSet, basename='guest')
router.register('reservation', views.ReservationViewSet, basename='guest')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/fbvlist/', views.FBV_List),
    path('rest/fbvpk/<int:pk>', views.FBV_pk),
    path('rest/cbvlist/', views.CBV_List.as_view()),
    path('rest/cbvpk/<int:pk>', views.CBV_pk.as_view()),
    path('rest/mixinslist/', views.Mixins_List.as_view()),
    path('rest/mixinspk/<int:pk>/', views.Mixins_pk.as_view()),    
    path('rest/GenericList', views.Generic_List.as_view()),
    path('rest/Genericpk/<int:pk>', views.Generic_pk.as_view()),
    path('rest/viewset/', include(router.urls)),
]
