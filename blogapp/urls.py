from django.urls import path,include
from .views import*
urlpatterns = [
    path('',blog,name='home'),
    path('index',home,name='index'),
    path('contact',Contact,name='contact'),
    path('career',career,name='career'),
    path('expertise',expertise,name='expertise'),
    path('project',project,name='project'),
    path('addblog',addblog,name='addblog'),
    path('signup',signup,name='signup'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
    path('show',home,name='show'),
    path('rmore<int:id>',rmore,name='rmore'),
    path('editblog<int:id>',editblog,name='editblog'),
    path('deleteblog<int:id>',deleteblog,name='deleteblog'),
    path('ownblog',ownblog,name='ownblog'),
    path('imgupdate<int:id>',imgupdate,name='imgupdate'),
    path('profile',profile,name='profile'),
    # path('search',name='profile'),
    # path('addimg',addimg,name='addimg'),
    # path('showresult',showresult,name='showresult'),
    # path('home',home,name='show')

    ]
