from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from apps.users.serializers import RegistrationSerializer

@api_view(["POST",])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            token, created = Token.objects.get_or_create(user=account)
            data = {
                'username': account.username,
                'email': account.email,
                'token': token.key
            }
            return Response(data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["POST",])
def logout_view(request):
    if request.method=="POST":
        try:
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        except AttributeError:
            return Response({"error": "No token found to delete."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET",])
@permission_classes([IsAuthenticated])
def get_profile_info(request):
    if request.method == "GET":
        data = {
            'username':request.user.username, 
            "email":request.user.email
        }
        return Response(data, status=status.HTTP_200_OK)
    
    