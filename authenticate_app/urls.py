from django.conf.urls import url
from authenticate_app import views
from django.urls import path
urlpatterns = [
    path('threads', views.display_all_threads, name = "viewforum"),
    path('view/<int:id>', views.view_thread, name = "viewthread"),
    path('createthread/', views.createthread, name = "createthread"),
    path('upvotethread/<int:id>', views.upthread, name = "upthread"),
    path('downvotethread/<int:id>', views.downthread, name="downthread"),
    path('upreply<int:id>', views.upreply, name = "upreply"),
    path('downreply<int:id>', views.downreply, name="downreply"),
]
