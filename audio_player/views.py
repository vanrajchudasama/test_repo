from django.shortcuts import render
from audio_player.models import Audio
import requests
from bs4 import BeautifulSoup
from audio_player.seriealizers import AudioSeriealizer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from audio_player.seriealizers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.
@api_view(['GET', 'POST'])
def audio_list(request,format=None):

    if request.method == 'GET':
        try:
            list_audio = Audio.objects.all()
            if list_audio:

                serializer = AudioSeriealizer(list_audio, many=True)
                return Response(serializer.data)
            else:
                return Response("Not Found",status=status.HTTP_404_NOT_FOUND)

        except:
            return Response("Not Found",status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        
        serializer = AudioSeriealizer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # json_data = JSONRenderer().render(seriealizer_data.data)
    # print(json_data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(seriealizer_data.data,safe=False)
