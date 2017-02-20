from django.conf.urls import url
from django.contrib import admin


from contact.views import login_view, main_view, logout_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view),
    url(r'^main/', main_view),
    url(r'^logout/', logout_view),
]
