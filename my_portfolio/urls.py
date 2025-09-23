from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hobbies/', include('hobbies.urls')), 
    path('', include('portfolio.urls')),        
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=BASE_DIR / "static")
