from unicodedata import name
from django.urls import path
from main.views import (
    dashboard_view,
    calendar_view,
    email_inbox_view,
    email_read_view,
    email_compose_view
)

app_name = 'main'

urlpatterns = [
    path("",view=dashboard_view,name="dashboard"),
    path("calendar",view=calendar_view,name="calendar"),
    # Email
    path("email/inbox",view=email_inbox_view,name="email.inbox"),
    path("email/read",view=email_read_view,name="email.read"),
    path("email/compose",view=email_compose_view,name="email.compose")
]
