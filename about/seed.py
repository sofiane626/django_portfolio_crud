from django_seed import Seed
from .models import About

def Aboutrun():
    seeder = Seed.seeder()
    datas = [
        {
            'paragraphe1': 'Contenu du paragraphe 1',
            'birthday': 'Date de naissance',
            'website': 'www.example.com',
            'phone': '0123456789',
            'city': 'Ville',
            'age': 'Âge',
            'degree': 'Diplôme',
            'phEmailone': 'exemple@example.com',
            'freelance': 'Statut freelance',
            'paragraphe2': 'Contenu du paragraphe 2',
        }
    ]
    for data in datas:
        seeder.add_entity(About, 1, data)
    print(seeder.execute())
