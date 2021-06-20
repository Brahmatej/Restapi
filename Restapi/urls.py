from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Restapi import views
    


urlpatterns = [

    path('data/', views.HospitalsListbystate.as_view()),
    path('data/<str:state>/', views.HospitalsListbystate.as_view()),
    path('data/<str:state>/<str:city>/', views.StateCity.as_view()),
    path('data/<str:state>/<str:city>/<str:pincode>/', views.StateCityPincode.as_view()),
    path('search/<str:name>/', views.search.as_view()),
    path('next/<str:num>/', views.Next.as_view())


]
urlpatterns=format_suffix_patterns(urlpatterns)
