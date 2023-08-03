from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ExtraView(TemplateView):
    pass
# Vertical 
layouts_vertical_light_sidebar_view = ExtraView.as_view(template_name="extras/layouts/vertical/layouts-light-sidebar.html")
layouts_vertical_compact_sidebar_view = ExtraView.as_view(template_name="extras/layouts/vertical/layouts-compact-sidebar.html")
layouts_vertical_icon_sidebar_view = ExtraView.as_view(template_name="extras/layouts/vertical/layouts-icon-sidebar.html")
layouts_vertical_boxed_view = ExtraView.as_view(template_name="extras/layouts/vertical/layouts-boxed.html")
layouts_vertical_colored_sidebar_view = ExtraView.as_view(template_name="extras/layouts/vertical/layouts-colored-sidebar.html")
# Horizontal
layouts_horizontal_horizontal_view = ExtraView.as_view(template_name="extras/layouts/horizontal/layouts-horizontal.html")
layouts_horizontal_hori_topbar_light_view = ExtraView.as_view(template_name="extras/layouts/horizontal/layouts-hori-topbar-light.html")
layouts_horizontal_hori_boxed_view = ExtraView.as_view(template_name="extras/layouts/horizontal/layouts-hori-boxed.html")
#  Authentication
authentication_login_view = ExtraView.as_view(template_name="extras/authentication/pages-login.html")
authentication_login_2_view = ExtraView.as_view(template_name="extras/authentication/pages-login-2.html")
authentication_register_view = ExtraView.as_view(template_name="extras/authentication/pages-register.html")
authentication_register_2_view = ExtraView.as_view(template_name="extras/authentication/pages-register-2.html")
authentication_recoverpw_view = ExtraView.as_view(template_name="extras/authentication/pages-recoverpw.html")
authentication_recoverpw_2_view = ExtraView.as_view(template_name="extras/authentication/pages-recoverpw-2.html")
authentication_lock_screen_view = ExtraView.as_view(template_name="extras/authentication/pages-lock-screen.html")
authentication_lock_screen_2_view = ExtraView.as_view(template_name="extras/authentication/pages-lock-screen-2.html")
# Extra Pages
extra_pages_timeline_view = ExtraView.as_view(template_name="extras/extra-pages/pages-timeline.html")
extra_pages_invoice_view = ExtraView.as_view(template_name="extras/extra-pages/pages-invoice.html")
extra_pages_directory_view = ExtraView.as_view(template_name="extras/extra-pages/pages-directory.html")
extra_pages_starter_page_view = ExtraView.as_view(template_name="extras/extra-pages/pages-starter.html")
extra_pages_404_view = ExtraView.as_view(template_name="extras/extra-pages/pages-404.html")
extra_pages_500_view = ExtraView.as_view(template_name="extras/extra-pages/pages-500.html")
extra_pages_pricing_view = ExtraView.as_view(template_name="extras/extra-pages/pages-pricing.html")
extra_pages_gallery_view = ExtraView.as_view(template_name="extras/extra-pages/pages-gallery.html")
extra_pages_maintenance_view = ExtraView.as_view(template_name="extras/extra-pages/pages-maintenance.html")
extra_pages_comingsoon_view = ExtraView.as_view(template_name="extras/extra-pages/pages-comingsoon.html")
extra_pages_faq_view = ExtraView.as_view(template_name="extras/extra-pages/pages-faq.html")
# Email Templates
email_templates_basic_view = ExtraView.as_view(template_name="extras/email-templates/email-template-basic.html")
email_templates_alerts_view = ExtraView.as_view(template_name="extras/email-templates/email-template-alert.html")
email_templates_billing_view = ExtraView.as_view(template_name="extras/email-templates/email-template-billing.html")