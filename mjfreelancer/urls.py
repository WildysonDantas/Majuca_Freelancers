from django.conf.urls import include, url 
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'mjfreelancer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('mjfreelancer.login.urls')),
   

]

if settings.DEBUG:
	urlpatterns == static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
