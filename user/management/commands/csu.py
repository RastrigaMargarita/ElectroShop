import os
import django
from django.core.management.base import BaseCommand
from user.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


class Command(BaseCommand):
    """Вспомогательная процедура, чтобы создать суперпользователя,
    Можно удалить после использования"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            first_name='admin',
            last_name='admin',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password('123')
        user.save()
        print("Суперпользователь создан")

        user = User.objects.create(
            email='isActive@mail.ru',
            first_name='isActive',
            last_name='isActive',
            is_superuser=False,
            is_staff=False,
            is_active=True
        )
        user.set_password('123')
        user.save()
        print("Активный пользователь создан")

        user = User.objects.create(
            email='isNotActive@mail.ru',
            first_name='isNotActive',
            last_name='isNotActive',
            is_superuser=False,
            is_staff=False,
            is_active=False
        )
        user.set_password('123')
        user.save()
        print("Не активный пользователь создан")
