from contextlib import contextmanager

from django.core.management import call_command


@contextmanager
def prepopulate_db(*data):
    for path in data:
        call_command('loaddata', path)
    yield
