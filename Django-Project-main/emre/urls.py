from django.contrib import admin
from django.urls import path, include
from urunler.views import *
from user.views import *
from django.conf.urls.static import static
from django.conf import settings
from iletisim.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('iletisim/',mesaj, name='mesaj'),
    path('', include('urunler.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
