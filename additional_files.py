from import_packages import *


def get_moscow_options():
    moscow_options = []

    for index in range(10 + 1):
        if index == 0:
            take_away_option = types.ShippingOption(f'moscow_mail', f'Почта Москвы')
            take_away_option.add_price(types.LabeledPrice(f'Почта Москвы', 10000))
            moscow_options.append(take_away_option)
        else:
            take_away_option = types.ShippingOption(f'takeaway_{index}', f'Пункт самовывоза Москва #{index}')
            take_away_option.add_price(types.LabeledPrice(f'Пункт самовывоза Москва #{index}', 0))
            moscow_options.append(take_away_option)

    return moscow_options


def get_regions_options():
    regions_options = []

    for index in range(11, 21 + 1):
        if index == 11:
            take_away_option = types.ShippingOption(f'regions_mail', f'Почта регионов')
            take_away_option.add_price(types.LabeledPrice(f'Почта регионов', 5000))
            regions_options.append(take_away_option)
        else:
            take_away_option = types.ShippingOption(f'takeaway_{index}', f'Пункт самовывоза Регионы #{index}')
            take_away_option.add_price(types.LabeledPrice(f'Пункт самовывоза Регионы #{index}', 0))
            regions_options.append(take_away_option)

    return regions_options


moscow_options = get_moscow_options()
regions_options = get_regions_options()

project_directory = os.path.dirname(os.path.realpath(__file__))


# Getting data from config file
def get_config() -> dict:
    global project_directory
    with open(rf'{project_directory}/data_files/default.json', 'r', encoding='utf-8') as config:
        data = json.load(config)

    return data


# # Getting data about catalog
# def get_catalog() -> dict:
#     global project_directory
#
#     # headers = {'Accept': 'application/json'}
#     # data_get_request = requests.get('', headers=headers)
#
#     with open(rf'{project_directory}/data_files/data.json', 'r', encoding='utf-8') as data:
#         catalog = json.load(data)['catalog']
#
#     return catalog


# Getting data about selections
def get_selections() -> dict:
    global project_directory

    # headers = {'Accept': 'application/json'}
    # data_get_request = requests.get('', headers=headers)

    with open(rf'{project_directory}/data_files/data.json', 'r', encoding='utf-8') as data:
        selections = json.load(data)['selections']

    return selections


# Getting data about current user's cart
def get_cart(user_id: str) -> dict:
    global project_directory

    # headers = {'Accept': 'application/json'}
    # data_get_request = requests.get('', headers=headers)

    with open(rf'{project_directory}/data_files/data.json', 'r', encoding='utf-8') as data:
        cart = json.load(data)['cart'][user_id]

    return cart


# Getting data about user's orders
def get_orders(user_id: str) -> dict:
    global project_directory

    # headers = {'Accept': 'application/json'}
    # data_get_request = requests.get('', headers=headers)

    with open(rf'{project_directory}/data_files/data.json', 'r', encoding='utf-8') as data:
        orders = json.load(data)['orders'][user_id]

    return orders


# Getting data about user's orders status
def get_orders_status(user_id: str) -> dict:
    global project_directory

    # headers = {'Accept': 'application/json'}
    # data_get_request = requests.get('', headers=headers)

    with open(rf'{project_directory}/data_files/data.json', 'r', encoding='utf-8') as data:
        orders = json.load(data)['ordersStatus'][user_id]

    return orders


# Getting data about user's favorite items
def get_favorites(user_id: str) -> dict:
    global project_directory

    # headers = {'Accept': 'application/json'}
    # data_get_request = requests.get('', headers=headers)

    with open(rf'{project_directory}/data_files/data.json', 'r', encoding='utf-8') as data:
        favorites = json.load(data)['favorites'][user_id]

    return favorites