from django.urls import path
from . import views
from .feeds import LatestArticlesFeed

app_name = 'articles'
urlpatterns = [
    path('', views.ArticlesList.as_view(), name='all_articles'),
    path('like/', views.article_like, name='like'),
    path('create_article/', views.CreateArticle.as_view(), name='create_article'),
    # path('<int:comment_id>/edit_comment/', views.edit_comment, name='edit_comment'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
    path('<slug:slug>/<int:comment_id>/update/', views.update_comment, name='update_comment'),
    path('<slug:slug>/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('<slug:slug>/update_article/', views.UpdateArticle.as_view(),
         name='update_article'),
    path('<slug:slug>/delete_article/', views.DeleteArticle.as_view(),
         name='delete_article'),
    path('<int:article_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.ArticlesList.as_view(), name='all_articles_by_tag'),
    path('feed/', LatestArticlesFeed(), name='article_feed'),
]

