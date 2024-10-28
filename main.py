import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.get_or_create(name=genre)
    actors = [("George", "Klooney"),
              ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"),
              ("Will", "Smith"),
              ("Jaden", "Smith"),
              ("Scarlett", "Johansson")]
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu", last_name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").all().order_by("first_name")


print(main())
# <QuerySet [<Actor: Jaden Smith>, <Actor: Will Smith>]>

print(Genre.objects.all())
# <QuerySet [<Genre: Western>, <Genre: Drama>]>

print(Actor.objects.all())
# <QuerySet [<Actor: George Clooney>, <Actor: Keanu Reeves>, <Actor: Will Smith>, <Actor: Jaden Smith>]>
