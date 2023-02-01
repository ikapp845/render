from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction
from .models import Profile
from group.serializers import ProfileSerializer
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

class UserDataUpload(APIView):
  pasrser_classes = [MultiPartParser,FormParser]

  def post(self,request):
    req = request.data
    with transaction.atomic():
      try:
        profile = Profile.objects.get(name = req["username"])
        return Response("The user already exists")
      except:
        profile = Profile.objects.create(name = req["username"],gender = req["gender"],email = req["email"],image_url = req["image"])
        profile.save()
      return Response("successfully created")

@api_view(["POST"])
def post(request):
  req = request.data
  with transaction.atomic():
    try:
      profile = Profile.objects.get(name = req["username"])
      return Response("The user already exists")
    except:
      profile = Profile.objects.create(name = req["username"],gender = req["gender"],email = req["email"])
      profile.save()
    return Response("successfully created")



@api_view(["POST"])
def check_username(request):
  req = request.data
  
  try:
    name = Profile.objects.get(name = req["username"])
    return Response("Fail")
  except:
    return Response("Success")

    
@api_view(["GET"])
def delete_account(request,username):
  user = Profile.objects.get(name = username)
  user.delete()
  return Respone("delete")

@api_view(["GET"])
def check_email(request,mail):
  try:
    user = Profile.objects.get(email = mail)
    return Response("yes user")
  except:
    return Response("no user")

@api_view(["GET"])
def login(request,mail):
  user = Profile.objects.get(email = mail)
  serializer = ProfileSerializer(user,many = False)
  return Response(serializer.data)


    


  