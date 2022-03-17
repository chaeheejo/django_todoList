from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views
app_name = 'todoList_restful_main'

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api-auth/', include('rest_framework.urls')),
    url(r'^$', views.Todo_restful_main.as_view(), name='todo'),
    url(r'^create/$', views.Todo_restful_create.as_view(), name='todo_create'),
    url(r'^(?P<pk>\d+)/update$', views.Todo_restful_update.as_view(), name='todo_update'),
    url(r'^(?P<pk>\d+)/delete$', views.Todo_restful_delete.as_view(), name='todo_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)