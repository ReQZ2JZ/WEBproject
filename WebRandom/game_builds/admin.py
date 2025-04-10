from django.contrib import admin
from .models import Game, Build, AdminInvite
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import redirect
from django.contrib import messages

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')
    actions = ['delete_selected_games']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def delete_selected_games(self, request, queryset):
        queryset.delete()
    delete_selected_games.short_description = "Delete selected games"

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

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'admin_actions')
    list_filter = ('is_staff', 'is_superuser')
    actions = ['make_admin', 'make_superuser_action', 'remove_admin', 'remove_superuser_action']

    def admin_actions(self, obj):
        if obj.is_superuser:
            return format_html(
                '<a class="button" href="{}">Убрать суперадмин</a>',
                f'/admin/auth/user/{obj.id}/remove-superuser/'
            )
        else:
            return format_html(
                '<a class="button" href="{}">Сделать суперадмин</a>',
                f'/admin/auth/user/{obj.id}/make-superuser/'
            )
    admin_actions.short_description = 'Действия'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:user_id>/make-superuser/',
                self.admin_site.admin_view(self.make_superuser),
                name='make-superuser',
            ),
            path(
                '<int:user_id>/remove-superuser/',
                self.admin_site.admin_view(self.remove_superuser),
                name='remove-superuser',
            ),
        ]
        return custom_urls + urls

    def make_superuser(self, request, user_id):
        user = User.objects.get(id=user_id)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        messages.success(request, f'Пользователь {user.username} теперь суперадминистратор')
        return redirect('admin:auth_user_changelist')

    def remove_superuser(self, request, user_id):
        user = User.objects.get(id=user_id)
        user.is_superuser = False
        user.save()
        messages.success(request, f'У пользователя {user.username} отозваны права суперадминистратора')
        return redirect('admin:auth_user_changelist')

    def make_admin(self, request, queryset):
        queryset.update(is_staff=True)
        messages.success(request, f'Выбранные пользователи теперь администраторы')
    make_admin.short_description = "Сделать администраторами"

    def make_superuser_action(self, request, queryset):
        queryset.update(is_staff=True, is_superuser=True)
        messages.success(request, f'Выбранные пользователи теперь суперадминистраторы')
    make_superuser_action.short_description = "Сделать суперадминистраторами"

    def remove_admin(self, request, queryset):
        queryset.update(is_staff=False)
        messages.success(request, f'У выбранных пользователей отозваны права администратора')
    remove_admin.short_description = "Отозвать права администратора"

    def remove_superuser_action(self, request, queryset):
        queryset.update(is_superuser=False)
        messages.success(request, f'У выбранных пользователей отозваны права суперадминистратора')
    remove_superuser_action.short_description = "Отозвать права суперадминистратора"

# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
