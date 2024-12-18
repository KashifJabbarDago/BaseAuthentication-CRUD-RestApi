from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializer import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser

# Create your views here.

class StudentCRUD(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
#   permission_classes = [IsAuthenticated] # Authenticate the user 
#   permission_classes = [AllowAny] # allowAny means anybody can manuplate we can set it on separately in class
    permission_classes = [IsAdminUser] # Only those will be access this class who has user.staff=True means staff status true


    # If want to apply this authentication for entire clasess in views file, you need to write that as globally see in
    # setting.py at the end that will apply for all clasess 

#    authentication_classes = [BasicAuthentication] # ask username, password to manuplate api
#    permission_classes = [IsAuthenticated] # allow only who is above passed by BasicAuthentication 


# this below allowAny means on all class will have secruity except AllowAny implemented class will not have any restriction
# Mean any one can manuplate as we made it AllowAny to manuplate 
class StudentCRUD2(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    

    