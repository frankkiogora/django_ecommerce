import debug_toolbar
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('__debug__/', include(debug_toolbar.urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
