class BaseCommand(object):

    help = ''

    def execute(self, namespace):
        raise NotImplemented

    def add_arguments(self, parser):
        pass