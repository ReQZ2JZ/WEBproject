from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from game_builds import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('game_builds.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('logout/success/', TemplateView.as_view(template_name='registration/logout_success.html'), name='logout_success'),
    path('social-auth-error/', TemplateView.as_view(template_name='registration/social_auth_error.html'), name='social_auth_error'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
