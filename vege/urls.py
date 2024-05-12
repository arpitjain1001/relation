from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
 path('receipes/',views.receipes),
 path('del_receipe/<id>/', views.del_receipe),
 path('update_receipe/<id>/', views.update_receipe),
 path('login/',views.login_page),
 path('register/',views.register_page),
  path('logout/',views.logout_page),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root = settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()

