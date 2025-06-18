from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user=User.objects.create(
            username="adminka",
            last_name="Алиева",
            first_name="Элвида",
            middle_name="Шахларовна",
            email="admin@mail.ru",
            phone="+79293086100",
            is_staff=True,
            is_superuser=True,
        )


        user.set_password('password')
        user.save()