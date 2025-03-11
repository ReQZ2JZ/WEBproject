from django.contrib import admin
from .models import Game, Build, AdminInvite

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ('game', 'name', 'created_at')
    list_filter = ('game', 'created_at')

@admin.register(AdminInvite)
class AdminInviteAdmin(admin.ModelAdmin):
    list_display = ('github_username', 'email', 'is_used', 'created_at', 'used_at')
    list_filter = ('is_used', 'created_at', 'used_at')
    readonly_fields = ('code', 'created_at', 'used_at')
    search_fields = ('github_username', 'email')
