from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Назва"
    )

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Product(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name="Назва товару"
    )

    brand = models.CharField(
        max_length=100,
        verbose_name="Бренд"
    )

    description = models.TextField(
        verbose_name="Опис"
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Ціна"
    )

    quantity = models.PositiveIntegerField(
        verbose_name="Кількість"
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Власник"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
        blank=True,
        verbose_name="Категорія"
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        verbose_name="Фото товару"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"

    def __str__(self):
        return self.title


class Profile(models.Model):

    ROLE_CHOICES = [
        ("manager", "Менеджер"),
        ("customer", "Покупець"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Користувач"
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="customer",
        verbose_name="Роль"
    )

    class Meta:
        verbose_name = "Профіль"
        verbose_name_plural = "Профілі"

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Review(models.Model):

    username = models.CharField(
        max_length=100,
        verbose_name="Ім'я"
    )

    message = models.TextField(
        verbose_name="Відгук"
    )

    rating = models.PositiveIntegerField(
        verbose_name="Оцінка"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"

    def __str__(self):
        return f"{self.username} ({self.rating}/5)"