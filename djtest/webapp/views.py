from django.shortcuts import render 
# Create your views here.
from .serializers import ContactSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactUsModel
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(["GET", "POST"])
def contact(request):
    if request.method == "GET":
        contact = ContactUsModel.objects.all().order_by("-id")
        serializer = ContactSerializer(contact, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    if request.method == "POST":
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

@api_view(["GET", "PATCH", "DELETE"])
def get_contact(request, id):


    if request.method == "GET":
        contact = get_object_or_404(ContactUsModel, id=id)
        serializer = ContactSerializer(contact)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    if request.method == "PATCH":
        contact = get_object_or_404(ContactUsModel, id=id)
        serializer = ContactSerializer(instance=contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "DELETE":
        contact = get_object_or_404(ContactUsModel, id=id)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    

