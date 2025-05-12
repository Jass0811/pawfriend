from django.core.management.base import BaseCommand
from pets.models import Pet

class Command(BaseCommand):
    help = 'Adds sample cats to the database'

    def handle(self, *args, **kwargs):
        cats = [
            {
                'name': 'Whiskers',
                'species': 'Cat',
                'description': 'A playful and affectionate tabby who loves cuddles',
                'age': 2,
                'image': 'images/cats/whiskers.jpg'
            },
            {
                'name': 'Luna',
                'species': 'Cat',
                'description': 'A graceful Siamese with striking blue eyes',
                'age': 3,
                'image': 'images/cats/luna.jpg'
            },
            {
                'name': 'Oliver',
                'species': 'Cat',
                'description': 'A friendly orange tabby who loves to play',
                'age': 1,
                'image': 'images/cats/oliver.jpg'
            },
            {
                'name': 'Misty',
                'species': 'Cat',
                'description': 'A gentle Persian with a luxurious coat',
                'age': 4,
                'image': 'images/cats/misty.jpg'
            }
        ]

        for cat_data in cats:
            Pet.objects.create(**cat_data)
            self.stdout.write(self.style.SUCCESS(f'Successfully added {cat_data["name"]}')) 