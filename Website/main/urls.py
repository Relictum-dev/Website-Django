from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('skills', views.skills),
    path('works', views.works),
    path('contacts', views.contacts),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
