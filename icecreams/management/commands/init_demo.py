from django.core.management.base import BaseCommand
from icecreams.models import IceCreamBucket, IceCream


class Command(BaseCommand):
    help = "Initialize the database to run demo"

    def handle(self, *args, **options):
        perfumes = ('Cherry', 'Chocolat Orange', 'Pistachio', 'Raspberry', 'Vanilla')

        for perfume in perfumes:
            ice_cream, created = IceCream.objects.get_or_create(
                name=perfume,
                static_image_path=f"{ perfume.lower().replace(' ', '-') }.jpg"
            )
            if created:
                ice_cream.save()

                bucket = IceCreamBucket(ice_cream=ice_cream)
                bucket.save()