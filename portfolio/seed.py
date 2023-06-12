from django_seed import Seed
from .models import Portfolio, PortfolioFiltre


def Portfoliorun():
    seeder = Seed.seeder()
    datas = [
        {
            'filtre': 'filtre1',
        },
        {
            'filtre': 'filtre2',
        }
    ]
    for data in datas:
        seeder.add_entity(PortfolioFiltre, 1, data)

    datas1 = [
        {
            'img': 'portfolio-1.jpg', 
            'choixFiltre': 'filtre1'
        },
        {
            'img': 'portfolio-2.jpg',
            'choixFiltre': 'filtre1',
        },
        {
            'img': 'portfolio-1.jpg',
            'choixFiltre': 'filtre2',
        },
    ]
    for data in datas1:
        seeder.add_entity(Portfolio, 1, data)
    print(seeder.execute())
