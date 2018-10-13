"""wadcourses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path  # For django versions from 2.0 and up

from django.conf import settings
from . import views
from django.conf.urls.static import static
from machina.app import board

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('account/', include("django.contrib.auth.urls")),
    path('', views.index, name='homepage'),
    path('login/', views.login, name='login'),
    path('forum/v1/', include(board.urls)),
    path('user',views.user,name = 'user'),
]

# debug_toolbar_URL
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
