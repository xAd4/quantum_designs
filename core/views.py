from django.views.generic import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "core/index.html"

class ServiceDetails(TemplateView):
    template_name = "core/service-details.html"

class StarterPage(TemplateView):
    template_name = "core/starter-page.html"