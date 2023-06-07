from django.contrib import admin
from django.urls import include, path

from django_socketio import SocketIOMiddleware

handler500 = "django.views.defaults.server_error"

urlpatterns = [
    path('', include('Dashboard.urls')),
    path('admin/', admin.site.urls),
    url(r'^socket\.io', include(SocketIOMiddleware.urls)),

]