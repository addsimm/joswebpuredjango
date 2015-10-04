from django.apps import AppConfig


class PythonSocialAuthConfig(AppConfig):
    name = 'lib.social.apps.django_app.default'
    verbose_name = 'Python Social Auth'

    def ready(self):
        from lib.social.strategies.utils import set_current_strategy_getter
        from lib.social.apps.django_app import load_strategy
        # Set strategy loader method to workaround current strategy getter
        # needed on get_user() method on authentication backends when working
        # with Django
        set_current_strategy_getter(load_strategy)
