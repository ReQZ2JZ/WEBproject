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

def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_builds/game_list.html', {'games': games})

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'game_builds/game_detail.html', {'game': game})

def generate_random_build(request, slug):
    game = get_object_or_404(Game, slug=slug)
    
    if game.name.lower() == "dota 2":
        heroes = ["Anti-Mage", "Crystal Maiden", "Lina", "Shadow Fiend", "Pudge"]
        items = ["Black King Bar", "Desolator", "Blink Dagger", "Aghanim's Scepter"]
        build = {
            "hero": random.choice(heroes),
            "core_items": random.sample(items, 3)
        }
    elif game.name.lower() == "dead by daylight":
        perks = ["Borrowed Time", "Dead Hard", "Iron Will", "Sprint Burst"]
        items = ["Medkit", "Flashlight", "Toolbox", "Map"]
        build = {
            "perks": random.sample(perks, 4),
            "item": random.choice(items)
        }
    elif game.name.lower() == "мир танков":
        tank_types = ["Тяжёлый танк", "Средний танк", "Лёгкий танк", "ПТ-САУ"]
        nations = ["СССР", "Германия", "США", "Великобритания", "Франция", "Япония", "Китай"]
        tiers = ["VIII", "IX", "X"]
        
        tanks = {
            "СССР": {
                "Тяжёлый танк": ["ИС-7", "Объект 277", "ИС-4", "Объект 705А", "СТ-II"],
                "Средний танк": ["Объект 140", "Т-62А", "К-91", "Объект 430У"],
                "Лёгкий танк": ["Т-100 ЛТ", "ЛТГ"],
                "ПТ-САУ": ["Объект 268", "Объект 268/4", "Объект 263"]
            },
            "Германия": {
                "Тяжёлый танк": ["E 100", "Maus", "Pz.Kpfw. VII", "VK 72.01 K"],
                "Средний танк": ["Leopard 1", "E 50 M"],
                "Лёгкий танк": ["Rheinmetall Panzerwagen"],
                "ПТ-САУ": ["Grille 15", "Jagdpanzer E 100", "Waffenträger auf E 100"]
            },
            "США": {
                "Тяжёлый танк": ["T110E5", "T57 Heavy Tank"],
                "Средний танк": ["M48 Patton", "T95E6"],
                "Лёгкий танк": ["T100E4", "Sheridan"],
                "ПТ-САУ": ["T110E3", "T110E4"]
            },
            "Великобритания": {
                "Тяжёлый танк": ["Super Conqueror", "T95/FV4201 Chieftain"],
                "Средний танк": ["Centurion Action X", "FV4202"],
                "Лёгкий танк": ["Manticore"],
                "ПТ-САУ": ["FV4005 Stage II", "FV217 Badger"]
            },
            "Франция": {
                "Тяжёлый танк": ["AMX M4 54", "AMX 50 B"],
                "Средний танк": ["B-C 25 t", "AMX 30 B"],
                "Лёгкий танк": ["AMX 13 105", "EBR 105"],
                "ПТ-САУ": ["Foch B", "Foch 155"]
            },
            "Япония": {
                "Тяжёлый танк": ["Type 5 Heavy"],
                "Средний танк": ["STB-1"],
                "Лёгкий танк": [],
                "ПТ-САУ": []
            },
            "Китай": {
                "Тяжёлый танк": ["WZ-111 model 5A", "113"],
                "Средний танк": ["121", "121B"],
                "Лёгкий танк": ["WZ-132-1"],
                "ПТ-САУ": []
            }
        }

        equipment = {
            "Тяжёлый танк": ["Усиленные приводы наводки", "Улучшенная вентиляция", "Усиленные торсионы", "Досылатель", "Стабилизатор вертикальной наводки"],
            "Средний танк": ["Усиленные приводы наводки", "Улучшенная вентиляция", "Стабилизатор вертикальной наводки", "Досылатель", "Оптика"],
            "Лёгкий танк": ["Усиленные приводы наводки", "Улучшенная вентиляция", "Оптика", "Биинокль", "Стабилизатор вертикальной наводки"],
            "ПТ-САУ": ["Усиленные приводы наводки", "Улучшенная вентиляция", "Маскировочная сеть", "Биинокль", "Досылатель"]
        }
        consumables = ["Ремкомплект", "Аптечка", "Огнетушитель", "Доппаёк", "Кола", "Шоколад", "Кофе с молоком"]
        
        tank_type = random.choice(tank_types)
        nation = random.choice(nations)
        
        while not tanks[nation][tank_type]:
            nation = random.choice(nations)
        
        build = {
            "тип_танка": tank_type,
            "нация": nation,
            "танк": random.choice(tanks[nation][tank_type]),
            "уровень": random.choice(tiers),
            "оборудование": random.sample(equipment[tank_type], 3),
            "расходники": random.sample(consumables, 3)
        }
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
