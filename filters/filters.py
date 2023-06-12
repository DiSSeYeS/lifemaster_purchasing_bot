from states import ADMINLIST, USERS, ALL_MODELS


__all__ = ['admin_filter', 'start_command_filter', 'help_command_filter',
           'select_vehicles_filter', 'select_details_filter', 'add_to_cart_filter',
            'question_for_add_filter', 'definition_filter', 'buying_filter',
            'show_cart_filter', 'clear_cart_filter', 'cleaning_cart_filter',
            'deleting_item_filter']

# Фильтер для распознавания хэндлерами админов
admin_filter = lambda msg: msg.from_user.id in ADMINLIST

# Фильтер для распознавания хэндлерами сообщений 'машины' от людей в состоянии None
select_vehicles_filter = lambda msg: USERS[msg.from_user.id]['condition'] == None and msg.text.lower() == 'машины'

# Фильтер для распознавания хэндлерами сообщений 'детали' от людей в состоянии None
select_details_filter = lambda msg: USERS[msg.from_user.id]['condition'] == None and msg.text.lower() == 'детали'

# Фильтер для распознавания хэндлерами команды "/start"
start_command_filter = lambda msg: msg.text == '/start'

# Фильтер для распознавания хэндлерами команды "/help"
help_command_filter = lambda msg: msg.text == '/help'

# Фильтр для распознавания хэндлерами команды "/купить"
buying_filter = lambda msg: msg.text == '/купить'

# Фильтр для распознавания хэндлерами команды "/корзина"
show_cart_filter = lambda msg: msg.text == '/корзина'

# Фильтр для распознавания хэндлерами команды "/очистка"
clear_cart_filter = lambda msg: msg.text == '/очистка' or USERS[msg.from_user.id]['condition'] == 'another_deleting_definition'

# Фильтер для распознавания хэндлерами команды добавления в корзину
question_for_add_filter = lambda msg: USERS[msg.from_user.id]['condition'] == 'choosing' and msg.text in ALL_MODELS

# Фильтр для распознавания хэндлера, пополняющего корзину
add_to_cart_filter = lambda msg: USERS[msg.from_user.id]['condition'] == 'adding_to_cart'\
      and msg.text.lower() in ('да', 'нет', 'добавить')

# Фильтр для распознавания хэндлером состояние человека 'undefined'
definition_filter = lambda msg: USERS[msg.from_user.id]['condition'] == 'undefined'

# Фильтр для распознавания хэндлером состояние пользователя 'cleaning_cart'
cleaning_cart_filter = lambda msg: USERS[msg.from_user.id]['condition'] == 'cleaning_cart'

# Фильтр для распознавания хэндлером состояния пользователя 'deleting_item'
deleting_item_filter = lambda msg: USERS[msg.from_user.id]['condition'] == 'deleting_item'
