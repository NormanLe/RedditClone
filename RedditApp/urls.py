from django.conf.urls import url

from . import views

app_name = 'RedditApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    # Ex: /hot
    url(r'^(?P<sorting>hot|new|rising|top|controversial)$', views.index, name='index_sorted'),
    
    # Ex: /r/learnprogramming/new
    url(r'^r/(?P<subblueit_name>\w+)/(?P<sorting>hot|new|rising|top|controversial)$',
        views.subblueit, name='subblueit_sorted'),
    
    # Ex: /r/learnprogramming
    url(r'^r/(?P<subblueit_name>\w+)$',
        views.subblueit, name='subblueit_detail'),
    
    # Ex: /r/learnprogramming/comments/1/How to use Django
    url(r'^r/(?P<subblueit_name>\w+)/comments/(?P<post_id>\d+)/(?P<post_name>\w+(\w|\s)+)/$',
        views.comments, name='post_detail'),

    # Ex: /r/learnprogramming/submit
    url(r'^r/(?P<subblueit_name>\w+)/submit$', views.submit, name='new_post'),

    # Ex: /user/DjangoProgrammer
    url(r'^user/(?P<username>\w+)$', views.user, name="user_detail"),
]
