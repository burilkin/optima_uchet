from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('billing.views',
    url(r'^$', 'home'),
    url(r'^invoices/$', 'invoices'),
    url(r'^invoices/(\d{1,5})/$', 'invoice_edit'),
    url(r'^invoices/(new)/$', 'invoice_edit'),
    url(r'^invoices/page/(\d{1,5})/$', 'invoices'),
    url(r'^insert/$', 'insert'),
    url(r'^inv/$', 'fff'),
    # Examples:
    # url(r'^$', 'Optima_Uchet.views.home', name='home'),
    # url(r'^Optima_Uchet/', include('Optima_Uchet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
