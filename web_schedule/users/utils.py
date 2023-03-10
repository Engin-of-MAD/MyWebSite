menu = [{'title': "Главная", 'url_name': 'home'},]


class DataMixin:
    @staticmethod
    def get_user_context(**kwargs):
        context = kwargs
        user_menu = menu.copy()
        context['menu'] = user_menu
        return context
