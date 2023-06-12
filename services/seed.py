from django_seed import Seed
from .models import Services, Services


def Servicesrun():
    seeder = Seed.seeder()
    datas = [
        {
            'logo': 'bi-briefcase',
            'titre': 'exemple',
            'contenu': 'mounir est incroyablement nul',
        },
        {
            'logo': 'bi-briefcase',
            'titre': 'exemple',
            'contenu': 'idriss est incroyablement nul',
        },
        {
            'logo': 'bi-briefcase',
            'titre': 'exemple',
            'contenu': 'marouane est incroyablement fort',
        }
    ]
    for data in datas:
        seeder.add_entity(Services, 1, data)
    print(seeder.execute())
