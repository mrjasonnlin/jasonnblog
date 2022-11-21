from populate import base
from django.contrib.auth.models import User
from account.models import UserProfile


def populate():
    print('Creating admin account ... ', 'end=')
    User.objects.all().delete()
    admin = User.objects.create_superuser(username='admin', password='admin', email=None)
    UserProfile.objects.create(user=admin, fullName='admin')
    print('done')


if __name__ == '__main__':
    populate()
