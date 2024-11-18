from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from contact.forms import ContactForm

# Create your views here.
class Home(TemplateView):
    template_name = "core/index.html"
    success_url = reverse_lazy('starter-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False) 
            contact.user = request.user  
            contact.save()  
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))
        
class ServiceDetails(TemplateView):
    template_name = "core/service-details.html"

class StarterPage(TemplateView):
    template_name = "core/starter-page.html"

class Blog(TemplateView):
    template_name = "core/implementation/blog.html"
class BlogDetails(TemplateView):
    template_name = "core/implementation/blog-details.html"
