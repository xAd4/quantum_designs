from django import template
from ..forms import ContactForm

register = template.Library()

@register.inclusion_tag("contact/form/contact_form.html", takes_context=True)
def contact_form(context):
    request = context["request"]
    form = None
    
    if request.method == "POST":
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
        
    return {"form": form}