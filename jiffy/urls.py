from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jiffy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'submitform.views.index'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^uploadfile/$','submitform.views.processfile'),
	url(r'^login/$', 'submitform.views.user_login'),
	url(r'logout/$', 'submitform.views.user_logout'),
	url(r'^register/$', 'submitform.views.register'),
	url(r'^createq/$', 'submitform.views.createquestions'),
		
)
