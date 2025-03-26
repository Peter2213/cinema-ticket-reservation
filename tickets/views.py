from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Guest, Reservation, Movie
from rest_framework.decorators import api_view
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer
# Create your views here.

# GET, POST
@api_view(['GET', 'POST'])
def FBV_List(request):
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =  GuestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)  
        
