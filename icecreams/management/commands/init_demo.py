from django.core.management.base import BaseCommand
from icecreams.models import IceCreamBucket, IceCream, IceCreamBall, Recipe


class Command(BaseCommand):
    help = "Initialize the database to run demo"

    def handle(self, *args, **options):
        perfumes = ('Cherry', 'Chocolate Orange', 'Pistachio', 'Raspberry', 'Vanilla')

        # Stocking perfumes for recipes
        ice_creams = {}
        for perfume in perfumes:
            ice_cream, created = IceCream.objects.get_or_create(
                name=perfume,
                static_image_path=f"icecreams/img/{ perfume.lower().replace(' ', '-') }.jpg"
            )
            ice_creams[perfume] = ice_cream
            if created:
                ice_cream.save()

                bucket = IceCreamBucket(ice_cream=ice_cream)
                bucket.save()

        italian_cup, created = Recipe.objects.get_or_create(name="Italian Cup")
        if created:
            pistachio_ball = IceCreamBall.objects.create(ice_cream=ice_creams['Pistachio'], quantity=1)
            vanilla_ball = IceCreamBall.objects.create(ice_cream=ice_creams['Vanilla'], quantity=1)
            cherry_ball = IceCreamBall.objects.create(ice_cream=ice_creams['Cherry'], quantity=1)

            italian_cup.ice_cream_balls.add(pistachio_ball, vanilla_ball, cherry_ball)

        rainbow_cup, created = Recipe.objects.get_or_create(name="Rainbow Cup")
        if created:
            balls = []
            for perfume in perfumes:
                ball = IceCreamBall.objects.create(ice_cream=ice_creams[perfume], quantity=1)
                balls.append(ball)

            rainbow_cup.ice_cream_balls.add(*balls)