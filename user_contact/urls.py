from django.conf.urls import url
from django.contrib import admin


from contact.views import login_view, main_view, logout_view
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^login/', login_view),
    url(r'^login/', login),
    url(r'^main/', main_view),
    url(r'^logout/', logout_view),
]
