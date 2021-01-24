from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about/', views.about),
    path('articles/', include('articles.urls')),
]

# will check if we're in debug mode and serve up static files 
urlpatterns += staticfiles_urlpatterns()