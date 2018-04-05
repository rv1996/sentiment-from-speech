from django.shortcuts import render
from django.http import JsonResponse
from textblob import TextBlob
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from .serializer import AudioFileSerializer
from .sentiment import predict_sentiment



# import cgi
# import contextlib
# import wave

class AudioView(APIView):
    parser_classes = (MultiPartParser, FormParser)


    def post(self,request, *args, **kwargs):
        
        audio_serializer = AudioFileSerializer(data=request.data)
        if audio_serializer.is_valid():

            # print(request.data.get('remark'))

            # with open('sample.mp3','wb') as f:
            #     f.write(request.data)
            #     f.close()

            print(audio_serializer.validated_data['file'])

            audio_serializer.save()

            # data = audio_serializer.data
            return Response(audio_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(audio_serializer.errors,status=status.HTTP_400_BAD_REQUEST)



def sentence(request):
    
    if request.method == 'GET':

        # print(request.GET.get('s'))
        sentence = request.GET.get('s')
        data = {
            "sentiment":predict_sentiment(sentence)[0],
            "algorithm":"SVM linear classifier",
            "polarity":TextBlob(sentence).polarity,
        }
        return JsonResponse(data)


# def audio_upload_view(request):