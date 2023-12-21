from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Creates users and assigns them to groups'

    def handle(self, *args, **kwargs):
        user_superuser = User.objects.create_user('Mr.Arafat', password='super@simplisolve')
        user_admin = User.objects.create_user('admin', password='admin@simplisolve')
        user_hr = User.objects.create_user('hr', password='hr@simplisolve')
        user_recruiter = User.objects.create_user('recruiter', password='recruiter@simplisolve')

        superuser_group, _ = Group.objects.get_or_create(name='superuser')
        admin_group, _ = Group.objects.get_or_create(name='admin')
        hr_group, _ = Group.objects.get_or_create(name='hr')
        recruiter_group, _ = Group.objects.get_or_create(name='recruitment')

        user_superuser.groups.add(superuser_group)
        user_admin.groups.add(admin_group)
        user_hr.groups.add(hr_group)
        user_recruiter.groups.add(recruiter_group)

        self.stdout.write(self.style.SUCCESS('Users created successfully!'))

