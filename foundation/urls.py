from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns = patterns('',
    (r'^starter/', TemplateView.as_view(template_name="foundation/starter.html")),
)