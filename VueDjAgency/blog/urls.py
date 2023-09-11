
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog import views


app_name = 'blog'
urlpatterns = [
    
    # /blog/post/99/
    path('post/<int:pk>/', views.PostDV.as_view(), name='post_detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)