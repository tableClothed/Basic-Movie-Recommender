import csv
from movies.models import Movie

with open('film.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        if row[1] in (None, ""):
            row[1] = 0
        if row[7] in (None, ""):
            row[7] = 0
        d, p = Movie.objects.get_or_create(
            year=row[0],
            length=row[1],
            title=row[2],
            genre=row[3],
            actor=row[4],
            actress=row[5],
            director=row[6],
            popularity=row[7],
            awards=row[8])
        d.save()