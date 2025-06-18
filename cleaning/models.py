from django.db import models
from users.models import User

class Order(models.Model):
    SERVICE_CHOICES = [
        ('deep_cleaning', 'Общий клининг'),
        ('general_cleaning', 'Генеральная уборка'),
        ('construction_cleaning', 'Послестроительная уборка'),
        ('carpet_cleaning', 'Химчистка ковров и мебели'),
    ]
    PAYMENT_CHOICES = [
        ('cash', 'Наличные'),
        ('card', 'Банковская карта'),
    ]
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('ip_progress', 'В работе'),
        ('done', 'Выполнено'),
        ('cancelled', 'Отменено'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    address = models.CharField(max_length=50, verbose_name="Адрес")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    email = models.EmailField(max_length=50, verbose_name="Адрес электронной почты")
    service = models.CharField(blank=True, max_length=50, choices=SERVICE_CHOICES, verbose_name="Вид услуги")
    is_custom_service = models.BooleanField(default=False, verbose_name="Иная услуга")
    custom_service = models.TextField( blank=True, null=True, verbose_name="Описание иной услуги")
    date_and_time = models.DateTimeField(verbose_name="Дата и время")
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES, verbose_name="Тип оплаты")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name="Статус", default='new')
    cancellation_reason = models.TextField(blank=True, null=True, verbose_name="Причина отмены")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
