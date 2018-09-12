from django.conf.urls import url , handler400
from . import views
urlpatterns = [
    url(r'^$', views.index, name="new"),
    url(r'^create/$', views.create, name="create"),
    url(r'^login/$', views.log, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
]
handler400 = 'login.views.nothing'



















# url(r'^(?P<user_id>\w+)$', views.wrong_num, name="wrong_num"),
#url(r'^(?P<user_id>\W+)$', views.wrong_num, name="wrong_num"),

# url(r'^login/(?P<user>\w+)$', views.wrong_num_login, name="wrong_num"),
# url(r'^login/(?P<user>\W+)$', views.wrong_num_login, name="wrong_num"),
# url(r'^login/(?P<user>\D+)$', views.wrong_num_login, name="wrong_num"),
# url(r'^login/(?P<user>\d+)/$', views.wrong_num_login, name="wrong_num"),