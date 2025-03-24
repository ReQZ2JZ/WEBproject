from django.db import models
import uuid

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='game_images/', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='item_images/')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='items')
    category = models.CharField(max_length=50)  # Starting Items, Early Game, Mid Game, Late Game
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.game.name} - {self.name}"

class Build(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='builds')
    name = models.CharField(max_length=200)
    description = models.TextField()
    components = models.JSONField()  # Будет хранить компоненты билда в JSON формате
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.game.name} - {self.name}"

class AdminInvite(models.Model):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True)
    github_username = models.CharField(max_length=100)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    used_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Invite for {self.github_username} ({self.email})"
