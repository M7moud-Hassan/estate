
from django.contrib import admin
from django.urls import path,include

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import MyPasswordChangeView, MyPasswordSetView

urlpatterns = [
    #enginners
    path('mtm-group/engineers/',include('engineers.urls')),
    path('mtm-group/reports/', include('reports.urls')),
    path('mtm-group/imported/', include('imported.urls')),
    path('mtm-group/admin/', admin.site.urls),
    path('mtm-group/',include('home.urls')),
    path('mtm-group/projects/',include('projects.urls')),
    path('mtm-group/', include('main.urls')),
    path('mtm-group/components/', include('components.urls')),
    path('mtm-group/', include('extras.urls')),

    path(
        "account/password/change/",
        login_required(MyPasswordChangeView.as_view()),
        name="account_change_password",
    ),
    path(
        "account/password/set/",
        login_required(MyPasswordSetView.as_view()),
        name="account_set_password",
    ),
    # All Auth
    path('account/', include('allauth.urls')),
]
