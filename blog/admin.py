from django.contrib import admin
from blog.models import (
    Category,
    Post,
    Comment,
    Setting,
    Favorite,
    Trash,
    Image,
    Voke,
    Subscriber,
    About,
)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = [
        "text",
    ]

@admin.register(Voke)
class VokeAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "entry_pk",
        "table",
        "is_liked",
        "is_disliked",
    ]
    search_fields = [
        "like",
    ]
    list_per_page = 20


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = [
        "name",
    ]
    list_per_page = 20


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "comment", "created_at", "updated_at"]
    search_fields = [
        "comment",
    ]
    list_per_page = 20


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ["theme", "default_category", "created_at", "updated_at"]
    search_fields = [
        "theme",
    ]
    list_filter = ["default_category"]
    list_per_page = 20


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ["post", "display", "created_at", "updated_at"]
    search_fields = ["post", "display"]
    list_filter = ["post"]
    list_per_page = 20


@admin.register(Trash)
class TrashAdmin(admin.ModelAdmin):
    list_display = [
        "owner",
        "title",
        "body",
        "category",
        "created_at",
        "deleted_at",
        "updated_at",
    ]
    search_fields = [
        "owner",
        "title",
    ]
    list_filter = ["category"]
    list_per_page = 20


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "is_subscribed",
    ]
    search_fields = [
        "user",
        "is_subscribed",
    ]
    list_per_page = 40


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["post"]
    search_fields = ["post"]
    list_per_page = 20


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "owner",
        "title",
        "category",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "title",
        "owner",
    ]
    list_filter = [
        "category",
    ]
    list_per_page = 25
