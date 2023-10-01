
from django.contrib import admin
from django.urls import path,include

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import MyPasswordChangeView, MyPasswordSetView

urlpatterns = [
    #enginners
    path('mgm-group/engineers/',include('engineers.urls')),
    path('mgm-group/reports/', include('reports.urls')),
    path('mgm-group/imported/', include('imported.urls')),
    path('mgm-group/admin/', admin.site.urls),
    path('mgm-group',include('home.urls')),
    path('mgm-group/projects/',include('projects.urls')),
    path('mgm-group', include('main.urls')),
    path('mgm-group/components/', include('components.urls')),
    path('mgm-group', include('extras.urls')),

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
