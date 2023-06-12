from django_seed import Seed
from .models import Skills, Skills_bar


def Skillsrun():
    seeder = Seed.seeder()
    datas = [
        {
            'paragraphe3': 'Contenu du paragraphe 1',
        }
    ]
    for data in datas:
        seeder.add_entity(Skills, 1, data)

    datas1 = [
        {
            'texte_progression': 'html', 'progression': '50'
        },
        {
            'texte_progression': 'css', 'progression': '50'
        },
        {
            'texte_progression': 'js', 'progression': '50'
        }
    ]
    for data in datas1:
        seeder.add_entity(Skills_bar, 1, data)
    print(seeder.execute())
