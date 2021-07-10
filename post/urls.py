from django.urls import path
from django.urls.conf import include 
from post import views


urlpatterns = [
    path('', views.HomeView.as_view(), name= 'home'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/category/<slug:slug>/',views.PostByCategory.as_view(), name='posts_by_category'),
    path('post/tag/<slug:slug>/',views.PostByTag.as_view(), name='posts_by_tag'),
    path('search/', views.SearchView.as_view(), name='post_search'),
    path('api/', include ('post.api.urls'))
     






]