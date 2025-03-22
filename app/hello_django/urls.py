from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse


def home(request, name="world"):
    return JsonResponse({"hello": name})


urlpatterns = [
    path('', home, name='home'),
    path('/<name>/', home, name='name'),
    path('admin/', admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
