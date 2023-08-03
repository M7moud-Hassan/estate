from django.urls import path
from extras.views import (
    layouts_vertical_light_sidebar_view,
    layouts_vertical_compact_sidebar_view,
    layouts_vertical_icon_sidebar_view,
    layouts_vertical_boxed_view,
    layouts_vertical_colored_sidebar_view,
    layouts_horizontal_horizontal_view,
    layouts_horizontal_hori_topbar_light_view,
    layouts_horizontal_hori_boxed_view,
    authentication_login_view,
    authentication_login_2_view,
    authentication_register_view,
    authentication_register_2_view,
    authentication_recoverpw_view,
    authentication_recoverpw_2_view,
    authentication_lock_screen_view,
    authentication_lock_screen_2_view,
    extra_pages_timeline_view,
    extra_pages_invoice_view,
    extra_pages_directory_view,
    extra_pages_starter_page_view,
    extra_pages_404_view,
    extra_pages_500_view,
    extra_pages_pricing_view,
    extra_pages_gallery_view,
    extra_pages_maintenance_view,
    extra_pages_comingsoon_view,
    extra_pages_faq_view,
    email_templates_basic_view,
    email_templates_alerts_view,
    email_templates_billing_view
)

app_name = "extras"

urlpatterns = [
    # Layouts
    path("layouts/vertical/light-sidebar",view=layouts_vertical_light_sidebar_view,name="layouts.vertical.light_sidebar"),
    path("layouts/vertical/compact-sidebar",view=layouts_vertical_compact_sidebar_view,name="layouts.vertical.compact_sidebar"),
    path("layouts/vertical/icon-sidebar",view=layouts_vertical_icon_sidebar_view,name="layouts.vertical.icon_sidebar"),
    path("layouts/vertical/boxed",view=layouts_vertical_boxed_view,name="layouts.vertical.boxed"),
    path("layouts/vertical/colored-sidebar",view=layouts_vertical_colored_sidebar_view,name="layouts.vertical.colored_sidebar"),
    path("layouts/horizontal/horizontal",view=layouts_horizontal_horizontal_view,name="layouts.horizontal.horizontal"),
    path("layouts/horizontal/hori-topbar-light",view=layouts_horizontal_hori_topbar_light_view,name="layouts.horizontal.hori_topbar_light"),
    path("layouts/horizontal/hori-boxed-width",view=layouts_horizontal_hori_boxed_view,name="layouts.horizontal.hori_boxed_width"),
    # Authentication
    path("authentication/login",view=authentication_login_view,name="authentication.login"),
    path("authentication/login-2",view=authentication_login_2_view,name="authentication.login_2"),
    path("authentication/register",view=authentication_register_view,name="authentication.register"),
    path("authentication/register-2",view=authentication_register_2_view,name="authentication.register_2"),
    path("authentication/recoverpw",view=authentication_recoverpw_view,name="authentication.recoverpw"),
    path("authentication/recoverpw-2",view=authentication_recoverpw_2_view,name="authentication.recoverpw_2"),
    path("authentication/lock-screen",view=authentication_lock_screen_view,name="authentication.lock_screen"),
    path("authentication/lock-screen-2",view=authentication_lock_screen_2_view,name="authentication.lock_screen_2"),
    # Exra Pages
    path("extra-pages/timeline",view=extra_pages_timeline_view,name="pages.timeline"),
    path("extra-pages/invoice",view=extra_pages_invoice_view,name="pages.invoice"),
    path("extra-pages/directory",view=extra_pages_directory_view,name="pages.directory"),
    path("extra-pages/startter-page",view=extra_pages_starter_page_view,name="pages.starter_page"),
    path("extra-pages/error-404",view=extra_pages_404_view,name="pages.404"),
    path("extra-pages/error-500",view=extra_pages_500_view,name="pages.500"),
    path("extra-pages/pricing",view=extra_pages_pricing_view,name="pages.pricing"),
    path("extra-pages/gallery",view=extra_pages_gallery_view,name="pages.gallery"),
    path("extra-pages/maintenance",view=extra_pages_maintenance_view,name="pages.maintenance"),
    path("extra-pages/comingsoon",view=extra_pages_comingsoon_view,name="pages.comingsoon"),
    path("extra-pages/faq",view=extra_pages_faq_view,name="pages.faq"),
    # Email templates
    path("email-templates/invoice",view=email_templates_basic_view,name="email_templates.basic"),
    path("email-templates/timeline",view=email_templates_alerts_view,name="email_templates.alerts"),
    path("email-templates/directory",view=email_templates_billing_view,name="email_templates.billing")    
]
