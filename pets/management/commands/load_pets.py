from django.core.management.base import BaseCommand
from pets.models import Pet

class Command(BaseCommand):
    help = 'Loads sample pets data into the database'

    def handle(self, *args, **options):
        # Sample dogs
        dogs = [
            {
                'name': 'Max',
                'species': 'Dog',
                'description': 'Intelligent and loyal companion, great with families and children.',
                'age': 2
            },
            {
                'name': 'Bella',
                'species': 'Dog',
                'description': 'Playful and affectionate, loves cuddles and attention.',
                'age': 1
            },
            {
                'name': 'Charlie',
                'species': 'Dog',
                'description': 'Friendly and gentle, perfect family dog with lots of energy.',
                'age': 3
            }
        ]

        # Sample cats
        cats = [
            {
                'name': 'Luna',
                'species': 'Cat',
                'description': 'Elegant and vocal, loves attention and playtime.',
                'age': 2
            },
            {
                'name': 'Oliver',
                'species': 'Cat',
                'description': 'Gentle and calm, enjoys quiet time and cuddles.',
                'age': 3
            },
            {
                'name': 'Leo',
                'species': 'Cat',
                'description': 'Friendly giant, loves water and being around people.',
                'age': 1
            }
        ]

        # Add dogs
        for dog_data in dogs:
            Pet.objects.get_or_create(**dog_data)
            self.stdout.write(self.style.SUCCESS(f'Added dog: {dog_data["name"]}'))

        # Add cats
        for cat_data in cats:
            Pet.objects.get_or_create(**cat_data)
            self.stdout.write(self.style.SUCCESS(f'Added cat: {cat_data["name"]}'))

        self.stdout.write(self.style.SUCCESS('Successfully loaded all pets!')) 