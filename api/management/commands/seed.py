import csv
from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from api.models import Consumer


class Command(BaseCommand):
    help = "seed database with consumer data"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="path to csv file")

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]
        chunk_size = 1000

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            while True:
                consumers = []
                try:
                    for _ in range(chunk_size):
                        row = next(reader)
                        consumers.append(row)
                except StopIteration:
                    break
                # seed data
                self.seed_data(consumers)
        
        self.stdout.write(self.style.SUCCESS('Consumers seeded successfully'))
    

    def seed_data(self, consumer_data):
        try:
            objects = []
            for row in consumer_data:
                point = Point(float(row[6]), float(row[5]))
                object = Consumer(
                    consumer_id=row[0],
                    street=row[1],
                    status=row[2],
                    previous_jobs_count=int(row[3]),
                    amount_due=int(row[4]),
                    geometry=point
                )
                objects.append(object)
            Consumer.objects.bulk_create(objects)
        except IntegrityError:
            self.stdout.write(self.style.ERROR('Consumers seeding FAILED'))

        return
