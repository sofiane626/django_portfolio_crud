import django
django.setup()

from about.seed import Aboutrun
from skills.seed import Skillsrun
from services.seed import Servicesrun
from testimonials.seed import Testimonialsrun
from contact.seed import Contactrun
from portfolio.seed import Portfoliorun

if __name__ == '__main__':
    Aboutrun()
    Skillsrun()
    Servicesrun()
    Testimonialsrun()
    Contactrun()
    Portfoliorun()
