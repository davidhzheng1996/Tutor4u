from django.conf.urls import url

from . import views

app_name='tutor4u'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^tutor$', views.tutor_signup, name='signup2'),
    # url(r'^signup_tutor$', views.tutorsignup, name='tutorsignup'),
    url(r'^signup_complete$', views.signup_complete, name='signup_complete'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^form_upload$', views.form_upload, name='form_upload'),
    url(r'^signup$', views.tutee_signup, name='signup'),
    url(r'^signup_action$', views.signup_action, name='signup_action'),
    url(r'^result/(?P<user_id>[0-9]+)$',views.results, name='results'),
    url(r'^tutorresults/(?P<user_id>[0-9]+)$',views.tutorresults, name='tutorresults'),
    url(r'^user_login$', views.user_login, name='user_login'),
    url(r'^about$',views.about, name='about'),
    url(r'^locations$',views.locations, name='locations'),
    url(r'^subjects$',views.subjects, name='subjects'),
    url(r'^lv$',views.lv, name='lv')
]
