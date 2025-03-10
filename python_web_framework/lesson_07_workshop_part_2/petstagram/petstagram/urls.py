# main urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram.common.urls')),
    path('pets/', include('petstagram.pets.urls')),
    path('accounts/', include('petstagram.accounts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
