from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class MainView(TemplateView):
    pass


dashboard_view = MainView.as_view(template_name='main/index.html')
calendar_view = MainView.as_view(template_name='main/calendar.html')
email_inbox_view = MainView.as_view(template_name='main/email/email-inbox.html')
email_read_view = MainView.as_view(template_name='main/email/email-read.html')
email_compose_view = MainView.as_view(template_name='main/email/email-compose.html')
