#!/usr/bin/env python
import sys

from django.conf import settings


settings.configure(
    DATABASES={
        'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory;'}
    },
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'podcast',
    ],
    ROOT_URLCONF='podcast.urls',
    TEST_RUNNER='django_coverage.coverage_runner.CoverageRunner',
    USE_TZ=True,
)


def runtests(*test_args):
    import django.test.utils

    runner_class = django.test.utils.get_runner(settings)
    test_runner = runner_class(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['podcast'])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
