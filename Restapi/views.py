from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import HospitalSerializer
from .models import hospital
class HospitalsListbystate(APIView):
    def get(self, request, state=None):
        if state==None:
            hospitals=hospital.objects.all()
            serializer=HospitalSerializer(hospitals, many=True)
            return Response(serializer.data)
        elif state:
            hospitals=hospital.objects.filter(state__iexact=state)
            serializer=HospitalSerializer(hospitals, many=True)
            return Response(serializer.data)
class StateCity(APIView):
    def get(self, request, state=None, city=None):
        hospitals=hospital.objects.filter(state__iexact=state)
        hospitals=hospitals.filter(city__iexact=city)
        serializer=HospitalSerializer(hospitals, many=True)
        return Response(serializer.data)
class StateCityPincode(APIView):
    def get(self, request, state=None, city=None, pincode=None):
        hospitals=hospital.objects.filter(state__iexact=state).filter(city__iexact=city).filter(pincode__iexact=pincode)
        serializer=HospitalSerializer(hospitals, many=True)
        return Response(serializer.data)
class search(APIView):
    def get(self, request, name=None):
        hospitals=hospital.objects.filter(name__iexact=name)
        serializer=HospitalSerializer(hospitals, many=True)
        return Response(serializer.data)



   