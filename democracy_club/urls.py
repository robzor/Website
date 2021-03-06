# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views

from core.views import HomeView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^logout/$', auth_views.logout,
        {'next_page': '/'}, name='auth_logout'),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'thanks/$', TemplateView.as_view(template_name="thanks.html")),
    url(r'thanks/finished$', TemplateView.as_view(template_name="thanks_finished.html")),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^privacy/$', TemplateView.as_view(template_name="privacy.html"), name="privacy"),
    url(r'^projects-and-data/$', TemplateView.as_view(template_name="projects-and-data.html"), name="projects-and-data"),
    url(r'^projects-and-data/polling-stations/$',
        TemplateView.as_view(template_name="polling-stations/home.html"),
        name="polling_one_pager"
        ),
    url(r'^projects-and-data/polling-stations/technical/$',
        TemplateView.as_view(template_name="polling-stations/technical.html"),
        name="polling_technical_explainer"
        ),
    url(r'^projects-and-data/polling-stations/faqs/$',
        TemplateView.as_view(template_name="polling-stations/faqs.html"),
        name="polling_faqs"
        ),
    url(r'^projects-and-data/polling-stations/embed/$',
        TemplateView.as_view(template_name="polling-stations/embed_code.html"),
        name="polling_embed_code"
        ),
    url(r'^projects-and-data/polling-stations/upload/$',
        TemplateView.as_view(template_name="polling-stations/upload_data.html"),
        name="polling_data_upload"
        ),
    url(r'^projects-and-data/polling-stations/techincal/$',
        RedirectView.as_view(url=reverse_lazy("polling_technical_explainer")),
        ),
    url(r'^projects-and-data/election-ids/reference/$',
        TemplateView.as_view(template_name="election-ids/reference.html"),
        name="election_ids_reference"
        ),
    url(r'^projects-and-data/election-ids/$',
        TemplateView.as_view(template_name="election-ids/home.html"),
        name="election_ids"
        ),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name="contact"),
    url(r'^members/', include('dc_members.urls')),
    url(r'^blog/', include('hermes.urls')),
    url(r'^research/', include('research.urls', namespace="research")),
    url(r'^donate/', include('donations.urls', namespace="donations")),
    url(r'^report_2016/', include('report_2016.urls', namespace="report_2016")),
    url(r'^quests/', include('backlog.urls', namespace="backlog")),
    url(r'^data/$',
        RedirectView.as_view(url=reverse_lazy("projects-and-data")),
    ),
    url(r'^projects/$',
        RedirectView.as_view(url=reverse_lazy("projects-and-data")),
    ),
    url(r'^projects/.*$',
        RedirectView.as_view(url=reverse_lazy("projects-and-data")),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
