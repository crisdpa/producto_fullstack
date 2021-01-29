"""Location Module."""
from django.core.management.base import BaseCommand
from opianalytics.apps.location.models.location import Location


class Command(BaseCommand):
    """Django Command Class."""

    help = "Add locations from a csv file"

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        """Handle a command process."""
        csv_file = options['csv_file']

        locations_added = Location.objects.add_from_csv(csv_file)
        self.stdout.write('Process finished, {0} locations added'.format(locations_added))
