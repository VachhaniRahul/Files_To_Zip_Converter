from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home),
    path('download/<uid>/' , views.download_zip),
    path('handle/', views.HandleFileUpload.as_view())
]
