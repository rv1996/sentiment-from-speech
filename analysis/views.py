from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from .serializer import AudioFileSerializer
from .sentiment import predict_sentiment

class AudioView(APIView):
    parser_classes = (MultiPartParser, FormParser)


    def post(self,request, *args, **kwargs):
        
        audio_serializer = AudioFileSerializer(data=request.data)
        if audio_serializer.is_valid():
            audio_serializer.save()

            # data = audio_serializer.data
            return Response(audio_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(audio_serializer.errors,status=status.HTTP_400_BAD_REQUEST)



def sentence(request):
    
    if request.method == 'GET':
        print(__name__)

        print(request.GET.get('s'))
        data = {
            "data":predict_sentiment(request.GET.get('s')),
        }
        return JsonResponse(data)


# def audio_upload_view(request):