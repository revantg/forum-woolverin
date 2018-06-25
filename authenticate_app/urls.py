from django.conf.urls import url
from authenticate_app import views
from django.urls import path
urlpatterns = [
    url(r'^threads', views.display_all_threads, name = "viewforum"),
    # url(r'^createthread', views.create_thread, name = 'create_thread'),
    path('view/<int:id>', views.view_thread, name = "viewthread"),
    # url(r'^view_thread2', views.view_thread2, name="thread2"),
    path(r'thread/<slug:subject>/post', views.post, name='post'),
    # url(r'thread2/post', views.post2, name='post2'),
    url(r'^successful', views.success, name = "success"),
    path('createthread/', views.createthread, name = "createthread")
]
