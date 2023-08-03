
from django.contrib import admin
from django.urls import path,include

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import MyPasswordChangeView, MyPasswordSetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('projects/',include('projects.urls')),
    path('', include('main.urls')),
    path('components/', include('components.urls')),
    path('', include('extras.urls')),

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
