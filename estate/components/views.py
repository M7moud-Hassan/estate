from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



class ComponentsView(TemplateView):
    pass

# UI-Components
components_ui_elements_alerts_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-alerts.html"  )
components_ui_elements_buttons_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-buttons.html" )
components_ui_elements_cards_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-cards.html" )
components_ui_elements_carousel_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-carousel.html" )
components_ui_elements_dropdowns_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-dropdowns.html" )
components_ui_elements_grid_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-grid.html" )
components_ui_elements_images_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-images.html" )
components_ui_elements_lightbox_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-lightbox.html" )
components_ui_elements_modals_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-modals.html" )
components_ui_elements_offcanvas_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-offcanvas.html" )
components_ui_elements_rangeslidebar_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-rangeslider.html" )
components_ui_elements_sessiontimeout_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-session-timeout.html" )
components_ui_elements_progressbars_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-progressbars.html" )
components_ui_elements_sweetalert_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-sweet-alert.html" )
components_ui_elements_tabs_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-tabs-accordions.html" )
components_ui_elements_typography_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-typography.html" )
components_ui_elements_video_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-video.html" )
components_ui_elements_general_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-general.html" )
components_ui_elements_colors_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-colors.html" )
components_ui_elements_rating_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-rating.html" )
# Forms
components_forms_elements_view = ComponentsView.as_view(template_name = "components/forms/form-elements.html")
components_forms_validation_view = ComponentsView.as_view(template_name = "components/forms/form-validation.html")
components_forms_advanced_view = ComponentsView.as_view(template_name = "components/forms/form-advanced.html")
components_forms_editors_view = ComponentsView.as_view(template_name = "components/forms/form-editors.html")
components_forms_fileupload_view = ComponentsView.as_view(template_name = "components/forms/form-uploads.html")
components_forms_xeditable_view = ComponentsView.as_view(template_name = "components/forms/form-xeditable.html")
components_forms_repeater_view = ComponentsView.as_view(template_name = "components/forms/form-repeater.html")
components_forms_wizard_view = ComponentsView.as_view(template_name = "components/forms/form-wizard.html")
components_forms_mask_view = ComponentsView.as_view(template_name = "components/forms/form-mask.html")
# Charts
components_charts_morris_view =ComponentsView.as_view(template_name ="components/charts/charts-morris.html")
components_charts_chartist_view =ComponentsView.as_view(template_name ="components/charts/charts-chartist.html")
components_charts_chartjs_view =ComponentsView.as_view(template_name ="components/charts/charts-chartjs.html")
components_charts_flot_view =ComponentsView.as_view(template_name ="components/charts/charts-flot.html")
components_charts_knob_view =ComponentsView.as_view(template_name ="components/charts/charts-knob.html")
components_charts_sparkline_view =ComponentsView.as_view(template_name ="components/charts/charts-sparkline.html")
# Tables
components_tables_basic_view =ComponentsView.as_view(template_name ="components/tables/tables-basic.html")
components_tables_datatable_view =ComponentsView.as_view(template_name ="components/tables/tables-datatable.html")
components_tables_responsive_view =ComponentsView.as_view(template_name ="components/tables/tables-responsive.html")
components_tables_editable_view =ComponentsView.as_view(template_name ="components/tables/tables-editable.html")
# Icons
components_icons_dripicons_view =ComponentsView.as_view(template_name ="components/icons/icons-dripicons.html")
components_icons_fontawesome_view =ComponentsView.as_view(template_name ="components/icons/icons-fontawesome.html")
components_icons_ion_view =ComponentsView.as_view(template_name ="components/icons/icons-ion.html")
components_icons_material_view =ComponentsView.as_view(template_name ="components/icons/icons-material.html")
components_icons_themify_view =ComponentsView.as_view(template_name ="components/icons/icons-themify.html")
components_icons_typicons_view =ComponentsView.as_view(template_name ="components/icons/icons-typicons.html")
# Maps
components_maps_google_view =ComponentsView.as_view(template_name ="components/maps/maps-google.html")
components_maps_vector_view =ComponentsView.as_view(template_name ="components/maps/maps-vector.html")