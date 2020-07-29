"""nfmakeupstudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    # example - path('link/',include('appname.urls'))
    # add include from django.urls
    # path('link/', views.link_view_name),

    path('admin/', admin.site.urls),
    path('',views.mainpage, name='mainpage'),
    # path('', views.main_page , name='mainpage'),
    path('home/', include('myapp.urls',namespace='myapp')),
    # path('tinymce/', include('tinymce.urls')),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += staticfiles_urlpatterns()
#
# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ]

#https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
