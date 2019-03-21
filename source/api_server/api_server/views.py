import json
from pyramid.view import view_config


@view_config(route_name='test/echo_val.json', renderer='json')
def get_echo(request):
    """
    This method will just return whatever is thrown at it
    :param request: web request
    :return dict:
    """
    data = json.loads(request.GET.get('data'))
    val = data['val']
    return {'val': val}


def make_response(request, result):
    """
    This method make response from result
    :param request: web request
    :param result: dict
    :return response: web response
    """
    response = request.response
    response.text = json.dumps(result)
    return response


def sample_api_response():
    """
    This generate sample response for request
    :return dict:
    """
    return {'status': True, 'messages': [], 'response': {}}


@view_config(route_name='signin.json', renderer='json')
def signin(request):
    """
    http://localhost:6543/signin.json?data=
    {
      "username": "something",
      "password": "something",
    }

    This method handled signin requests
    """
    result = sample_api_response()
    data = json.loads(request.GET.get('data'))
    if "username" not in data:
        result['status'] = False
        result['messages'].append('username is a required argument')
        return make_response(request, result)
    user_credentials = {
                        "first_name": "First",
                        "last_name": "Name",
                        "email": "something.com",
                        "city": "something"
                        }
    result['response'] = user_credentials
    return make_response(request, result)


@view_config(route_name='signup.json', renderer='json')
def signup(request):
    """
    http://localhost:6543/signup.json?data=
    {
        "first_name": "First",
        "last_name": "Name",
        "email": "something.com",
        "city": "something",
        "create_password": "something",
        "confirm_password": "something"

    }

    """
    result = sample_api_response()
    data = request.GET.get('data')
    try:
        data = json.loads(data)
    except Exception as e:
        result['status'] = False
        result['messages'].append('Request payload is not a valid json: %s' % e)
        return make_response(request, result)
    required_keys = ['first_name', 'last_name', 'user_name', 'confirm_password',
                     'email', 'create_password', 'city']

    # Check that all the keys exist.
    for key in required_keys:
        if key not in data:
            result['status'] = False
            result['messages'].append('%s is a required argument' % key)

    # Check that the create and confirm password are same
    if data['confirm_password'] != data['create_password']:
        result['status'] = False
        result['messages'].append('Create and Confirm password do not match')

    return make_response(request, result)


@view_config(route_name='meals_page/get_available_location_values.json', renderer='json')
def get_available_location_values(request):
    """
    http://localhost:6543/meals_page/get_available_location_values.json?data=
    {}
    This methods returns available locations to show on drop down list for filter.
    """
    result = sample_api_response()
    data = json.loads(request.GET.get('data'))
    return_data = {
                    "location": [
                        "location1",
                        "location2",
                        "location3"
                    ]
                }
    result['response'] = return_data
    return make_response(request, result)


@view_config(route_name='meals_page/get_available_cuisine_values.json', renderer='json')
def get_available_cuisine_values(request):
    """
    http://localhost:6543/meals_page/get_available_cuisine_values.json?data=
    {}
    This methods returns available cuisines to show on drop down list for filter.
    """
    result = sample_api_response()
    data = json.loads(request.GET.get('data'))
    return_data = {
                    "location": [
                        "cuisine1",
                        "cuisine2",
                        "cuisine3"
                    ]
                }
    result['response'] = return_data
    return make_response(request, result)


@view_config(route_name='meals_page/get_available_culinary_preference_values.json', renderer='json')
def get_available_culinary_preference_values(request):
    """
    http://localhost:6543/meals_page/get_available_culinary_preference_values.json?data=
    {}
    This methods returns available culinary_preference to show on drop down list for filter.
    """
    result = sample_api_response()
    data = json.loads(request.GET.get('data'))
    return_data = {
                    "location": [
                        "vegetarian",
                        "kosher",
                        "halal"
                    ]
                }
    result['response'] = return_data
    return make_response(request, result)


@view_config(route_name='meals_page/get_available_meals.json', renderer='json')
def get_available_meals(request):
    """
    http://localhost:6543/meals_page/get_available_meals.json?data=
    {
        "location": ["location1", "location1"],
        "cuisine": ["cuisine1", "cuisine2"],
        "price_range": [10, 200],
        "culinary_preference": ["vegetarian", "pescatarian"],
        "rating": [4, 5],
        "date_range": ["MMDDYYYY", "MMDDYYYY"],
        "meal_types": ["breakfast", "lunch", "snacks", "dinner"],
    }

    This methods returns available meals based on provided filter.
    """
    # TODO: Add appropriate URLs.
    result = sample_api_response()
    data = json.loads(request.GET.get('data'))
    return_data = {
                    "meal_id1": {
                        "meal_id": "meal_id1",
                        "name": "Name",
                        "rating": 5,
                        "price": 5,
                        "date": "02012019",
                        "start_time": "0700",
                        "end_time": "0900",
                        "location": "location1",
                        "top_image_url": "meal_image_url"
                    },
                    "meal_id2": {
                        "name": "meal_id2",
                        "rating": 5,
                        "price": 5,
                        "date": "02102019",
                        "start_time": "0530",
                        "end_time": "0730",
                        "location" : "location2",
                        "top_image_url" : "meal_image_url"
                    },
                    "meal_id3": {
                        "name": "meal_id3",
                        "rating": 5,
                        "price": 5,
                        "date": "03012019",
                        "start_time": "1000",
                        "end_time": "1300",
                        "location": "location3",
                        "top_image_url": "meal_image_url"
                    }
                }

    result['response'] = return_data
    return make_response(request, result)


@view_config(route_name='meal_details_page/get_meal_details.json', renderer='json')
def get_meal_details(request):
    """
    http://ec2-3-16-149-55.us-east-2.compute.amazonaws.com:6543/meal_details_page/get_meal_details.json?data=
    {
        "meal_id" : "meal_id1"
    }

    This methods returns available meal detail based on provided id.
    """
    # TODO: Add appropriate URLs.
    result = sample_api_response()
    data = json.loads(request.GET.get('data'))
    if data.get('meal_id') != 'meal_id1':
        result['status'] = False
        result['messages'].append('meal_id is a required argument and accepted value is meal_id1')
        return make_response(request, result)

    return_data = {
                    "meal_id1": {
                        "meal_id": "meal_id1",
                        "name": "Name",
                        "rating": 3,
                        "price": 4,
                        "dates": ["02102019", "02112019", "02122019", "02132019"],
                        "start_time": "1900",
                        "end_time": "2100",
                        "location": "location1",
                        "image_urls": ["meal_image_url1", "meal_image_url2", "meal_image_url3"],
                        "menu": {
                            "item1": "description-1",
                            "item2": "description-2",
                            "item3": "description-3"
                        }
                    }
                }
    result['response'] = return_data
    return make_response(request, result)


@view_config(route_name='meal_details_page/get_reviews_of_meal.json', renderer='json')
def get_reviews_of_meal(request):
    """
    http://ec2-3-16-149-55.us-east-2.compute.amazonaws.com:6543/meal_details_page/get_reviews_of_meal.json?data=
    {
        "meal_id" : "meal_id1"
    }
    This methods returns reviews of a meal provided an id.
    """
    # TODO: Add appropriate URLs.
    result = sample_api_response()
    data = json.loads(request.GET.get('data'))
    if data.get('meal_id') != 'meal_id1':
        result['status'] = False
        result['messages'].append('meal_id is a required argument and accepted value is meal_id1')
        return make_response(request, result)

    return_data = {
                    "review_id1": {
                        "review_id": "review_id1",
                        "review_title": "This is review title",
                        "review": "This is a review",
                        "rating": 4,
                        "user_name": "Name",
                        "user_url": "user_pic_url"
                    },
                    "review_id2": {
                        "review_id": "review_id2",
                        "review_title": "This is review title",
                        "review": "This is a review",
                        "rating": 5,
                        "user_name": "Name",
                        "user_url": "user_pic_url"
                    },
                    "review_id3": {
                        "review_id": "review_id3",
                        "review_title": "This is review title",
                        "review": "This is a review",
                        "rating": 4,
                        "user_name": "Name",
                        "user_url": "user_pic_url"
                    }
                }
    result['response'] = return_data
    return make_response(request, result)


@view_config(route_name='meal_details_page/book_meal.json', renderer='json')
def book_meal(request):
    """
    http://ec2-3-16-149-55.us-east-2.compute.amazonaws.com:6543/meal_details_page/book_meal.json?data=
    {
        "name": "Name",
        "user_id": "UserID",
        "number_of_people" : 2,
        "date": "02102019",
        "meal_id": "meal_id1"
    }
    This methods is called when people submit a meal booking form.
    """
    # TODO: Add appropriate URLs.
    result = sample_api_response()
    _ = json.loads(request.GET.get('data'))
    return make_response(request, result)


@view_config(route_name='meal_details_page/post_meal.json', renderer='json')
def post_meal(request):
    """
    http://ec2-3-16-149-55.us-east-2.compute.amazonaws.com:6543/meal_details_page/post_meal.json?data=
    {
        "meal_id" : "meal_id1",
        "name" : "Name",
        "price": 15,
        "dates": ["02102019", "02112019", "02122019", "02132019"],
        "start_time": "1900",
        "end_time": "2100",
        "location" : "location1",
        "image_urls" : ["meal_image_url1", "meal_image_url2"],
        "menu": {
            "item1": "description-1",
            "item2": "description-2",
            "item3": "description-3"
        }
    }
    This methods is called when people submit a meal booking form.
    """
    result = sample_api_response()
    data = json.loads(request.GET.get('data'))
    if "meal_id" not in data:
        result['status'] = False
        result['messages'].append('meal_id is a required argument')
        return make_response(request, result)
    return_data = {'meal_id': 'meal_id1'}
    result['response'] = return_data
    return make_response(request, result)


@view_config(route_name='meal_details_page/delete_meal.json', renderer='json')
def delete_meal(request):
    """
    http://ec2-3-16-149-55.us-east-2.compute.amazonaws.com:6543/meal_details_page/delete_meal.json?data=
    {
        "meal_id" : "meal_id1"
    }
    This methods is called when people want to delete a posted meal.
    """
    result = sample_api_response()
    data = json.loads(request.GET.get('data'))
    if "meal_id" not in data:
        result['status'] = False
        result['messages'].append('meal_id is a required argument')
        return make_response(request, result)
    return make_response(request, result)


@view_config(route_name='host_page/host_meta_data.json', renderer='json')
def host_meta_data(request):
    """
    http://ec2-3-16-149-55.us-east-2.compute.amazonaws.com:6543/host_page/host_meta_data.json?data=
    {
        "user_name" : "xyz",
        "details": {
            "<key>": "<value>"
        }
    }
    This methods is called when people fill in details to be a host.
    """
    result = sample_api_response()
    data = json.loads(request.GET.get('data'))
    if "user_name" not in data:
        result['status'] = False
        result['messages'].append('user_name is a required argument')
        return make_response(request, result)
    return make_response(request, result)


@view_config(route_name='guest_page/my_past_meals.json', renderer='json')
def guest_past_meals(request):
    """
    http://ec2-3-16-149-55.us-east-2.compute.amazonaws.com:6543/guest_page/my_past_meals.json?data=
    {
        "user_name" : "xyz"
    }
    This methods is used to retrieve past meals of a guest.
    """
    result = sample_api_response()
    data = json.loads(request.GET.get('data'))
    if "user_name" not in data:
        result['status'] = False
        result['messages'].append('user_name is a required argument')
        return make_response(request, result)

    return_data = {
        "meal_id1": {
            "meal_id": "meal_id1",
            "name": "Name",
            "rating": 5,
            "price": 5,
            "date": "02012019",
            "start_time": "0700",
            "end_time": "0900",
            "location": "location1",
            "top_image_url": "meal_image_url"
        },
        "meal_id2": {
            "name": "meal_id2",
            "rating": 5,
            "price": 5,
            "date": "02102019",
            "start_time": "0530",
            "end_time": "0730",
            "location": "location2",
            "top_image_url": "meal_image_url"
        },
        "meal_id3": {
            "name": "meal_id3",
            "rating": 5,
            "price": 5,
            "date": "03012019",
            "start_time": "1000",
            "end_time": "1300",
            "location": "location3",
            "top_image_url": "meal_image_url"
        }
    }

    result['response'] = return_data
    return make_response(request, result)


@view_config(route_name='guest_page/my_past_reviews.json', renderer='json')
def guest_past_reviews(request):
    """
    http://ec2-3-16-149-55.us-east-2.compute.amazonaws.com:6543/guest_page/my_past_reviews.json?data=
    {
        "user_name" : "xyz"
    }
    This methods is used to retrieve past reviews of a guest.
    """
    result = sample_api_response()
    data = json.loads(request.GET.get('data'))
    if "user_name" not in data:
        result['status'] = False
        result['messages'].append('user_name is a required argument')
        return make_response(request, result)

    return_data = {
        "review_id1": {
            "review_id": "review_id1",
            "review_title": "This is review title",
            "review": "This is a review",
            "rating": 4,
            "user_name": "Name",
            "user_url": "user_pic_url"
        },
        "review_id2": {
            "review_id": "review_id2",
            "review_title": "This is review title",
            "review": "This is a review",
            "rating": 5,
            "user_name": "Name",
            "user_url": "user_pic_url"
        },
        "review_id3": {
            "review_id": "review_id3",
            "review_title": "This is review title",
            "review": "This is a review",
            "rating": 4,
            "user_name": "Name",
            "user_url": "user_pic_url"
        }
    }
    result['response'] = return_data
    return make_response(request, result)
