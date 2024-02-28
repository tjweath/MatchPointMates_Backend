from .models import  Player
from rest_framework import viewsets, permissions, status, generics
from .serializers import PlayerSerializer
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class PlayerViewSet(viewsets.ModelViewSet):
    # queryset = Player.objects.all()
    # permission_classes = [permissions.IsAuthenticated] 
    serializer_class = PlayerSerializer
    # http_method_names = ['get', 'post', 'patch', 'put', 'delete']
    
    def get_queryset(self):
        user = self.request.user
        return Player.objects.filter(owner=user)
    
    # def post(self, request):
    #     serializer = PlayerSerializer(data=request.data)  # Simplified
    #     if serializer.is_valid():
    #         serializer.save(owner=request.user)  # Ensure the owner is set
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)  # Use 400 for Bad Request
    
    def put(self, request, pk=None):
        try:
            player = Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
def home_view(request):
    return HttpResponse("This is the home page.")

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            new_user = User.objects.create(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

