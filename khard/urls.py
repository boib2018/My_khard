from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static






 


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('events/', views.events, name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('gallery/<int:pk>/', views.gallery_detail, name='gallery_detail'),
    path('search/', views.search_view, name='search'),
 

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
