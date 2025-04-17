from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileListSerializer
from django.shortcuts import render
from django.http import FileResponse
import os
import shutil

def home(request):
    return render(request, 'home.html')

def download(request , uid):
    return render(request , 'download.html' , context = {'uid' : uid})

class HandleFileUpload(APIView):
    def post(self, request):
        try:
            data = request.data

            serializer = FileListSerializer(data = data)

            if serializer.is_valid():
                data = serializer.save()
                return Response({'message': 'files uploaded succesfully','data': data})
            return Response({
                'message': 'something went wrong',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
        

def download_zip(request, uid):
    print("hello")
    file_path = os.path.join(settings.MEDIA_ROOT, "zip", f"{uid}.zip")
    extra_file_path = os.path.join(settings.MEDIA_ROOT, uid) 
    print(extra_file_path)
    if not os.path.exists(file_path):
        print('not found')
    
    response = FileResponse(open(file_path, "rb"), as_attachment=True)
    response["Content-Disposition"] = f'attachment; filename="{uid}.zip"'
    response.streaming = True 
    try:
        if os.path.exists(extra_file_path):  
            print('yes')
            shutil.rmtree(extra_file_path)

        if os.path.exists(file_path):  
            print('yes yes')
            os.remove(file_path)
    except Exception as e:
        print(f"Error deleting files: {e}")
    return response