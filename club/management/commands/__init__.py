from django.core.management.base import BaseCommand, CommandError
from club.models import Member
import faker
from faker.factory import Factory

fake = faker.Faker('ko_KR')

class Command(BaseCommand):
    help = 'Make fake members'

    def add_arguments(self, parser):
        parser.add_argument('numbers', nargs='+', type=int)

    def handle(self, *args, **options):
        for _ in range(options['numbers']):
            Member.objects.create(
                generation=fake.random_digit(),
                birth_date=fake.date(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                introduction=fake.paragraph(nb_sentences=3),
                
            )

            self.stdout.write(self.style.SUCCESS('Succesfully made members of"%s"' % options['numbers']))