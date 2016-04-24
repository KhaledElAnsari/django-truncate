from django.core.management.base import BaseCommand, CommandError

from django.apps import apps

class Command(BaseCommand):
    appsList = []  # this list will have all wanted apps
    modelsList = []  # this list will have all wanted models

    def add_arguments(self, parser):
        parser.add_argument('--models',
                        nargs='*',
                        type=str,
                        dest='models',
                        default=None,
                        help="This will take the names of the wanted models")
        parser.add_argument('--apps',
                        nargs='*',
                        type=str,
                        dest='apps',
                        default=None,
                        help='Collect wanted apps to get there models, default will be getting all models of the project')

    def handle(self, *args, **options):

        if options['apps'] == None or options['apps'] == [] or options['apps'] == ['']:
            print('No apps was entered')
        else:
            print('Fetching apps...')
            for someApp in options['apps']:
                try:
                    self.appsList.append(apps.get_app_config(someApp))
                except LookupError:
                    print("The app " + someApp + " does not exist")
            print('Finished apps fetching')

        if options['models'] == None or options['models'] == [] or options['models'] == ['']:
            print("No models were called")
        elif self.appsList:
            print("Fetching models...")
            for appConf in self.appsList:
                for someModel in options['models']:
                    try:
                        self.modelsList.append(appConf.get_model(someModel))
                    except LookupError:
                        print("The model " + someModel + " does not exist in this app")

            if not self.modelsList:
                self.appsList = []
            print('Finished models fetching')

        if not self.modelsList and not self.appsList:
            print('Nothing was called')
        elif self.appsList and not self.modelsList:
            print('Starting apps truncate..')
            for _app in self.appsList:
                app_models = _app.get_models()
                for _model in app_models:
                    _model.objects.all().delete()
                print("The " + _app.name + " app is now empty")
            print('Finished apps truncate!')

        else:
            for _model in self.modelsList:
                _model.objects.all().delete()

            print('Finished models truncate!')
