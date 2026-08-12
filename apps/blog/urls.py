from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.blog.views import BlogItemView, BlogListCreateView, CategoryViewSet, CommentCreateView

router = DefaultRouter(trailing_slash=False)
router.register(
    r"blog/categories",
    CategoryViewSet,
    basename="category",
)

urlpatterns = [
    path("blog", BlogListCreateView.as_view(), name="blog_list_create"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog_item"),
    path("comment", CommentCreateView.as_view(), name="comment_create"),
    *router.urls,
]
