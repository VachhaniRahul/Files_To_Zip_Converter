from rest_framework import serializers
from .models import Folder, Files
import shutil

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length = 100000, allow_empty_file = False, use_url = False)
    )
 
    def zip_files(self,folder):
        shutil.make_archive(f'media/zip/{str(folder)}', 'zip', f'media/{folder}')


    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
    
        for file in files:
            files_obj = Files.objects.create(folder = folder, file = file)

        self.zip_files(folder.uid)
        
        return {'files': {}, 'folder':str(folder.uid)}


