from pyramid.config import Configurator
from pyramid.request import Request
from pyramid.response import Response


def request_factory(environ):
    """
    This functions
    :param environ:
    :return request:
    """
    request = Request(environ)
    request.response = Response()
    request.response.headerlist = []
    request.response.headerlist.extend(
        (
            ('Access-Control-Allow-Origin', '*'),
            ('Content-Type', '*')
        )
    )
    return request


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    :param global_config:
    :param settings:
    :return wsgi_app:
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.set_request_factory(request_factory)
    config.include('pyramid_chameleon')
    config.add_route('test/echo_val.json', '/test/echo_val.json')
    config.add_route('signin.json', '/signin.json')
    config.add_route('signup.json', '/signup.json')
    config.add_route('meals_page/get_available_location_values.json', '/meals_page/get_available_location_values.json')
    config.add_route('meals_page/get_available_cuisine_values.json', '/meals_page/get_available_cuisine_values.json')
    config.add_route('meals_page/get_available_culinary_preference_values.json',
                     '/meals_page/get_available_culinary_preference_values.json')
    config.add_route('meals_page/get_available_meals.json', '/meals_page/get_available_meals.json')
    config.add_route('meal_details_page/get_meal_details.json', '/meal_details_page/get_meal_details.json')
    config.add_route('meal_details_page/get_reviews_of_meal.json', '/meal_details_page/get_reviews_of_meal.json')
    config.add_route('meal_details_page/book_meal.json', '/meal_details_page/book_meal.json')
    config.add_route('meal_details_page/post_meal.json', '/meal_details_page/post_meal.json')
    config.add_route('meal_details_page/delete_meal.json', '/meal_details_page/delete_meal.json')
    config.add_route('host_page/host_meta_data.json', '/host_page/host_meta_data.json')
    config.add_route('guest_page/my_past_meals.json', '/guest_page/my_past_meals.json')
    config.add_route('guest_page/my_past_reviews.json', '/guest_page/my_past_reviews.json')
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
