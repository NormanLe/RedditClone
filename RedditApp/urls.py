from django.conf.urls import include, url
from . import views as RedditApp_views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'subblueits', RedditApp_views.SubblueitViewSet)
router.register(r'posts', RedditApp_views.PostViewSet)
router.register(r'comments', RedditApp_views.CommentViewSet)
router.register(r'users', RedditApp_views.UserViewSet)


app_name = 'RedditApp'
urlpatterns = [
    url(r'^$', RedditApp_views.index, name='index'),

    # Ex: /hot
    url(r'^(?P<sorting>hot|new|top)$', RedditApp_views.index_ordered, name='index_ordered'),

    # Ex: /r/learnprogramming/new
    url(r'^r/(?P<subblueit_name>\w+)/(?P<sorting>hot|new|top)$',
        RedditApp_views.subblueit_ordered, name='subblueit_ordered'),

    # Ex: /r/learnprogramming
    url(r'^r/(?P<subblueit_name>\w+)$',
        RedditApp_views.subblueit, name='subblueit_detail'),

    # Ex: /r/learnprogramming/comments/1/How to use Django
    url(r'^r/(?P<subblueit_name>\w+)/comments/(?P<post_id>\d+)/(?P<post_name>\w+(\w|\s)+)/$',
        RedditApp_views.comments, name='post_detail'),

    # Ex: /r/learnprogramming/submit
    url(r'^r/(?P<subblueit_name>\w+)/submit$', RedditApp_views.submit, name='new_post'),

    # Ex: /user/DjangoProgrammer
    url(r'^user/(?P<username>\w+)$', RedditApp_views.user, name='user_detail'),

# LOGIN URLS
    # /login
    url(r'^login/$', auth_views.LoginView.as_view(template_name="RedditApp/login.html"),name='login'),
    # /logout
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="RedditApp/index.html"), name='logout'),

    # /signup
    url (r'^signup/$', RedditApp_views.signup, name='signup'),

# REST FRAMEWORK URLS
    # url(r'^users/$', RedditApp_views.UserList.as_view(), name='user-list'),
    # url(r'^users/(?P<pk>[0-9]+)/$', RedditApp_views.UserDetail.as_view()),
    url(r'^api/', include(router.urls)),
    ]
