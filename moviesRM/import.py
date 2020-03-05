import csv
from movies.models import Movie

with open('tmdb_5000_movies.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        try:
            d, p = Movie.objects.get_or_create(
                title=row[17],
                genre=row[1],
                homepage=row[2],
                overview=row[7],
                release_date=row[11],
                production_companies=row[9],
                length=row[13],
                tagline=row[16]
                )
            d.save()
        except: break