from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import home, downloadfile  # Import the donloadfile view

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin interface
    path('', home, name="home"),    
    path('<str:id>/', downloadfile, name="download"),  # URL for the "donloadfile" view
]

# If DEBUG is True, serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
