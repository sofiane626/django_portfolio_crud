from django_seed import Seed
from .models import Contact


def Contactrun():
    seeder = Seed.seeder()
    datas = [
        {
            'location': 'Bruxelles',
            'mail': 'azerty@gmail.com',
            'call': '+32 485687425',
        }
    ]
    for data in datas:
        seeder.add_entity(Contact, 1, data)
    print(seeder.execute())
