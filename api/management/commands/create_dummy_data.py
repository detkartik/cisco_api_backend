import random
import datetime
from django.contrib.auth import get_user_model
from api.models import Cisco
from django.core.management import BaseCommand

User = get_user_model()

    
class Command(BaseCommand):

    first_names = ('John','Andy','Joe')
    last_names = ('Johnson','Smith','Williams')

    def create_random_user(self, count):
        data = {
            'username' : random.choice(self.first_names) + str(count),
            'password' : 'user' + str(count),
            'first_name' : random.choice(self.first_names),
            'last_name' : random.choice(self.last_names),
        }
        return User.objects.create_user(**data)

    def handle(self, *args, **kwargs):
        print('Creating dummy data')
        user = User.objects.get(username='kartikey')
        for count in range(1,251):
            data = {
                'user' : user,
            }
            Cisco.objects.create(**data)
            if count % 10 == 0:
                user = self.create_random_user(count)
        print('Creation of dummy data is completed')