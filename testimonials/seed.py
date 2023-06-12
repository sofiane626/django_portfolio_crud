from django_seed import Seed
from .models import Testimonials


def Testimonialsrun():
    seeder = Seed.seeder()
    datas = [
        {
            'citation': 'Contenu du paragraphe 1',
            'nom': 'Sofiane',
            'job': 'web DEV',
        },
        {
            'citation': 'Contenu du paragraphe 1',
            'nom': 'mounir',
            'job': 'web DEV',
        },
        {
            'citation': 'Contenu du paragraphe 1',
            'nom': 'Marouane',
            'job': 'web DEV',
        },
    ]
    for data in datas:
        seeder.add_entity(Testimonials, 1, data)
    print(seeder.execute())
