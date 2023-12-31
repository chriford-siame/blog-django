from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    posts,
    management,
    model_form_data_create,
    post_forms_page,
    post_delete,
    post_update,
    post_view,
    comment,
    setting,
    about,
    comment_action,
)

app_name = "blog"
urlpatterns = [
    path("", posts, name="index"),
    path("blogs/view/", posts, name="posts"),
    path("blog/about/", about, name="about"),
    path("management/", management, name="management"),
    path("settings/", setting, name="settings"),
    path(
        "model-form/data/create/arg/<str:form_arg>",
        model_form_data_create,
        name="model-form-data-create",
    ),
    path("blog/forms/page/", post_forms_page, name="post-forms-page"),
    path("blog/<str:title>/status/<str:status>/blog/<int:pk>/", post_delete, name="post-delete"),
    path(
        "blog/comment/<int:pk>/action/<str:action_type>/update/",
        comment_action,
        name="comment_action",
    ),
    path("blog/<str:title>/update/blog/key/<int:pk>/", post_update, name="post-update"),
    path("blog/<str:title>/read/blog/key/<int:pk>/", post_view, name="post-view"),
    path("blog/pk/<int:pk>/title/<str:title>/comment/", comment, name="comment"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
