from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages
from django.utils import timezone
from .models import Game, Build, AdminInvite
from .forms import UserRegistrationForm
import random
from django.contrib.auth import logout
from django.views.decorators.http import require_http_methods
from .games.dota2 import generate_dota2_build
from .games.dead_by_daylight import generate_dead_by_daylight_build
from .games.world_of_tanks import generate_world_of_tanks_build
from .games.league_of_legends import generate_league_of_legends_build

def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_builds/game_list.html', {'games': games})

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    name = game.name.lower().strip()
    print("Game name:", name)  # для отладки
    if name == "dota 2":
        template = "game_builds/game_detail_dota2.html"
    elif name == "dead by daylight":
        template = "game_builds/game_detail_dead_by_daylight.html"
    elif name == "мир танков":
        template = "game_builds/game_detail_worldoftanks.html"
    elif name == "league of legends":
        template = "game_builds/game_detail_league_of_legends.html"
    else:
        template = "game_builds/game_detail.html"
    return render(request, template, {'game': game})

def generate_random_build(request, slug):
    game = get_object_or_404(Game, slug=slug)

    if game.name.lower() == "dota 2":
        build = generate_dota2_build()
    elif game.name.lower() == "dead by daylight":
        build = generate_dead_by_daylight_build()
    elif game.name.lower() == "мир танков":
        build = generate_world_of_tanks_build()
    elif game.name.lower() == "league of legends":
        build = generate_league_of_legends_build()
    else:
        build = {"error": "Build generation not implemented for this game"}

    return JsonResponse(build)

def is_github_user(user):
    return user.is_authenticated and hasattr(user, 'social_auth') and \
           user.social_auth.filter(provider='github').exists()

@user_passes_test(is_github_user)
def register_admin(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.is_superuser = True
            user.save()
            messages.success(request, 'Администратор успешно создан!')
            return redirect('admin:index')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'game_builds/register_admin.html', {'form': form})

def activate_admin_invite(request, code):
    if not request.user.is_authenticated:
        return redirect('social:begin', 'github')
    
    try:
        invite = AdminInvite.objects.get(code=code, is_used=False)
        github_account = request.user.social_auth.get(provider='github')
        github_username = github_account.extra_data.get('login')  # Получаем username из GitHub
        
        if invite.github_username == github_username:
            invite.is_used = True
            invite.used_at = timezone.now()
            invite.save()
            
            user = request.user
            user.is_staff = True
            user.is_superuser = True
            user.save()
            
            messages.success(request, 'Вы успешно активировали админ права!')
            return redirect('admin:index')
        else:
            messages.error(request, 'Это приглашение предназначено для другого пользователя GitHub.')
    except AdminInvite.DoesNotExist:
        messages.error(request, 'Неверный или уже использованный код приглашения.')
    except Exception as e:
        messages.error(request, f'Произошла ошибка при активации: {str(e)}')
    
    return redirect('game_builds:game_list')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация успешна! Теперь вы можете войти.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'game_builds/register.html', {'form': form})

@require_http_methods(["GET", "POST"])
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('logout_success')
    return render(request, 'registration/logged_out.html')
