from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import traceback

from utils import *

try:
    from py_tarif.tarif import data
except:
    from tarif import data

try:
    from main_pdf.pdf import create_pdf
except:
    from pdf import create_pdf

# готовое кп

try:
    from main_pdf.user_tar_list import us_l, us_order
except:
    from user_tar_list import us_l, us_order

##### при формировании кп проверить на дважды занесенные в строку с кп кнопки {[..._sms-pack_sms-pack_...]}

# configuration
bot = Bot(token='5201645810:AAEMoBx3WSt5qgnX5pjNhYLvcATOGI5aKV4')
dp = Dispatcher(bot, storage=MemoryStorage())

### butons

kp_to_name = {
    'wifi': 'Wi-Fi',
    'wats': 'ВАТС',
    'vn': 'Видеонаблюдение',
    'iptv': 'IP TV',
    'iptv/hot': 'IP TV для гостиниц',
    'internet': 'Интернет'
}

dep_to_name = {
    'prim': 'ПФ',
    'khab': 'ХФ',
    'sakh': 'СФ',
    'kamch': 'КФ',
    'amur': 'АФ',
    'maga': 'МФ',
    'sakhtel': 'СТК'
}

show_used_to_name = {
    'wifi/control': 'Управляемый Wi-Fi',
    'wifi/guest': 'Wi-Fi для гостей',
    'vn': 'Видеонаблюдение',
    'iptv/hot': 'Телевидение для гостиниц',
    'iptv': 'Телевидение',
    'wats/busy': 'Виртаульная АТС: бизнес/вирт. номер',
    'wats/packmin': 'Виртаульная АТС: пакет минут',
    'internet': 'Интернет'
}


### internet

internet_tariffs_names = {
    'delovoj': 'Деловой',
    "uskorenie": "Ускорение",
    "ozhn": "ОЖН",
    "skorost": "Скорость",
    "m2mkontrol": "М2М Контроль"
}

internet_mats = {
    'opt': 'Оптика',
    'med': 'Медь'
}

internet_techs = {
    'yesm2m': 'M2M',
    'nom2m': 'Не M2M'
}

### wifi buttons


wifi_service_names = {
    'control-3600': 'костыль для проверки наличия флага',
    'control': 'Управляемый Wi-Fi',
    '3600': '⬆(Организация - 3 600 ₽ за 1 устройство)',
    'guest': 'Wi-Fi для гостей'
}

wifi_guest_tp_names = {
    'start-0/700': 'костыль для проверки наличия флага',
    'improve-3600/1450': 'костыль для проверки наличия флага',
    'extended-3600/1100': 'костыль для проверки наличия флага',
    'start': 'ТП Начальный',
    'improve': 'ТП Улушенный',
    'extended': 'ТП Расширенный',
    '0/700': '⬆0 ₽/устройство, 700 ₽/точка (в месяц)',
    '3600/1450': '⬆3600 ₽/устройство, 1450 ₽/точка (в месяц)',
    '3600/1100': '⬆3600 ₽/устройство, 1100 ₽/точка (в месяц)'
}

wifi_guest_speed_names = {
    '10': '10 Мбит/с, ',
    '20': '20 Мбит/с, ',
    '30': '30 Мбит/с, ',
    '50': '50 Мбит/с, ',
    '80': '80 Мбит/с, ',
    '100': '100 Мбит/с, '
}

wifi_control_sms_names = {
    'sms-1100': 'костыль для проверки наличия флага',
    'nosms-800': 'костыль для проверки наличия флага',
    'sms': 'с СМС',
    'nosms': 'без СМС',
    '1100': '⬆(1100 ₽ - ежемесячно за 1 устройство)',
    '800': '⬆(800 ₽ - ежемесячно за 1 устройство)'
}

wifi_dop_names = {
    'filter-600': 'костыль для проверки наличия флага',
    'block-50': 'костыль для проверки наличия флага',
    'filter': 'Расширенная фильтрация и анализ трафика',
    '600': '⬆(600 ₽ ежемесячно за 1 точку)',
    'block': 'Добровольная блокировка',
    '50': '⬆(50 ₽ ежемесячно за 1 услугу)',
    'radar': 'Wi-Fi Радар',
    'adv': 'Рекламная платформа',
    'wifi/pass': 'Пропустить'
}

check_dop_control = [
    'filter',
    'block',
    'radar'
]

check_dop_guest = [
    'filter',
    'block',
    'radar',
    'adv'
]

wifi_radar_adv_names = {
    'once/3600': 'Единовременно (3600 ₽ за 1 устройство)',
    '6m/2400': '6 месяцев (2400 ₽ за 1 устройство)',
    '12m/1': '12 месяцев (1 ₽ за 1 устройство)',

    'access': 'Соглашение (2400 ₽ ежемесячно за 1 точку)',
    '12m': 'Соглашение на 12 мес. (1800 ₽ ежемесячно за 1 точку)',
    'extended': 'ТП Расширенный (1050 ₽ ежемесячно за 1 точку)'
}

wifi_radar_adv_lic_names = {
    '1': '1 лиц. (ежемесячно за 1 лиц.)',
    '3': 'От 3 лиц. (ежемесячно за 1 лиц.)',
    '5': 'От 5 лиц. (ежемесячно за 1 лиц.)',
    '10': 'От 10 лиц. (ежемесячно за 1 лиц.)',

    'adv-access': '',
    'adv-12m': '',
    'adv-extended': ''
}


### iptv/hot buttons


iptv_hot_main = {
    '1mainChNoInt': 'ОПТ без интеграции',
    '2mainChPMS': 'ОПТ при интеграции (PMS)',
    '3mainChDVB': 'ОПТ при подключении DVB-C',
    '4mainChSmart': 'ОПТ при подключении на SmartTV',
    '5mainChSmartPMS': 'ОПТ на SmartTV при интеграции (PMS)'
}

iptv_hot_main_ch = {
    '1st': 'Стандарт',
    '1lux': 'Люкс',
    '1prestige': 'Престиж',
    '1st/daily': 'Стандарт (сут.)',
    '1lux/daily': 'Люкс (сут.)',
    '1prestige/daily': 'Престиж (сут.)',

    '2st/int': 'Стандарт (с инт.)',
    '2lux/int': 'Люкс (с инт.)',
    '2prestige/int': 'Престиж (с инт.)',
    '2st/daily/int': 'Стандарт (сут., с инт.)',
    '2lux/daily/int': 'Люкс (сут., с инт.)',
    '2prestige/daily/int': 'Престиж (сут., с инт.)',

    '3st/dvb': 'Стандарт DVB-C',
    '3lux/dvb': 'Люкс DVB-C',
    '3prestige/dvb': 'Престиж DVB-C',
    '3st/light/dvb': 'Стандарт Лайт DVB-C',

    '4st/smart': 'Стандарт SmartTV',
    '4lux/smart': 'Люкс SmartTV',
    '4prestige/smart': 'Престиж SmartTV',
    '4st/daily/smart': 'Стандарт SmartTV (сут.)',
    '4lux/daily/smart': 'Люкс SmartTV (сут.)',
    '4prestige/daily/smart': 'Престиж SmartTV (сут.)',

    '5st/smart/int': 'Стандарт SmartTV (с инт.)',
    '5lux/smart/int': 'Люкс SmartTV (с инт.)',
    '5prestige/smart/int': 'Престиж SmartTV (с инт.)',
    '5st/daily/smart/int': 'Стандарт SmartTV (сут., с инт.)',
    '5lux/daily/smart/int': 'Люкс SmartTV (сут., с инт.)',
    '5prestige/daily/smart/int': 'Престиж SmartTV (сут., с инт.)',
    '5partner': 'Пакет "Партнерский стандарт"',
    '5partner/int': 'Пакет "Партнерский стандарт" (с инт.)'
}

iptv_hot_main_ch_dop = ['1st', '1lux', '1prestige',
                       '3st/dvb', '3lux/dvb', '3prestige/dvb', '3st/light/dvb',
                       '4st/smart', '4lux/smart', '4prestige/smart'
]

iptv_hot_choices = {
    '1/10': '1-10 пакетов: ',
    '11/20': '11-20 пакетов: ',
    '21/30': '21-30 пакетов: ',
    '30+': 'свыше 30 пакетов: ',

    '1': '1 канал: 0 ₽ ежемес.',
    '2': '2 канала: 60 ₽ ежемес.',
    '3': '3 канала: 75 ₽ ежемес.',
    '4': '4 канала: 95 ₽ ежемес.',
    '5': '5 каналов: 120 ₽ ежемес.',
    'pass/infochannel': 'Пропустить'

}

iptv_hot_dop_ch_names = {
    'ihkhlprime': 'Телеканал KHL Prime (149 ₽)',
    'ihmatch': 'Матч! (100 ₽)',
    'ihsupermatch': 'Суперматч! (450 ₽)',
    'ihadult': 'Пакет для взрослых (500 ₽)',
    'ihadult+': 'Пакет для взрослых + (1200 ₽)',
    'ihadultSut': 'Пакет для взрослых (сут.) (120 ₽)',
    'ihadult+Sut': 'Пакет для взрослых + (сут.) (360 ₽)',
    'ihchina': 'Пакет Китай (150 ₽)',
    'ihchinaSut': 'Пакет Китай (сут.) (13 ₽)',
    'ihpass/dopchannel': 'Пропустить!'
}


### vn_buttons


vn_service_to_name = {
    'vnStan': '"Видеонаблюдение" Стандартный',
    'vnBase': '"Видеонаблюдение" Базовый 2.0'
}

vn_tp_to_name = {
    'stan0': 'Стандартный',
    'stan10': 'Стандартный-10',
    'stan20': 'Стандартный-20',
    'base20': 'Базовый 2.0',
    'base20mlm': 'Базовый 2.0 mlm',
    'base20dig': 'Базовый 2.0_Digital',
    'base2010': 'Базовый 2.0 - 10',
    'base2010mlm': 'Базовый 2.0 - 10 mlm',
    'base2010dig': 'Базовый 2.0_Digital - 10',
    'base2020': 'Базовый 2.0 - 20',
    'base2020mlm': 'Базовый 2.0 - 20 mlm',
    'base2020dig': 'Базовый 2.0_Digital - 20',
    'base2030': 'Базовый 2.0 -30',
    'base2030mlm': 'Базовый 2.0 - 30 mlm',
    'base2030dig': 'Базовый 2.0_Digital - 30',
}

vn_sutki_to_name = {
    '0': 'Без хранения',
    '3': '3 суток',
    '5': '5 суток',
    '7': '7 суток',
    '10': '10 суток',
    '14': '14 суток',
    '30': '30 суток',
    '45': '45 суток',
    '60': '60 суток',
    '90': '90 суток',
    '180': '180 суток'
}

vn_save_to_name = {
    'reg': 'Регистратор',
    'complete': 'Полная запись',
    'actions': 'Запись только событий',
    'econom': 'Режим экономии трафика'
}

vn_traffic_to_name = {
    '256': '256 Кбит/с',
    '512': '512 Кбит/с',
    '1': '1 Мбит/с',
    '1.5': '1.5 Мбит/с',
    '2': '2 Мбит/с',
    '3': '3 Мбит/с'
}

vn_big_dop_to_name = {
    'smsPack': 'Пакеты SMS-уведомлений',
    'vidAnal': 'Видеоаналитика',
    'pass': 'Пропустить'
}

vn_dops_to_name = {
    '100/30': '100 шт./ 30 суток',
    '500/90': '500 шт./ 90 суток',
    '1000/180': '1 000 шт./180 суток',
    '5000/365': '5 000 шт./365 суток',
    'visCount-1080': 'Подсчет посетителей',
    'lenQ-1320': 'Определение длины очереди',
    'faceRec-1800': 'Распознавание лиц',
    'controlEmp-1080': 'Контроль сотрудников на рабочем месте',
    'heatMap-960': 'Построение тепловых карт',
    'autoNom-3600': 'Распознавание а/м номеров',
    'leftS-1080': 'Оставленные предметы',
    'visCount-1080+disc': '(цена: 1080 руб., скидка до 30%)',
    'lenQ-1320+disc': '(цена: 1320 руб., скидка до 30%)',
    'faceRec-1800+disc': '(цена: 1800 руб., скидка до 30%)',
    'controlEmp-1080+disc': '(цена: 1080 руб., скидка до 30%)',
    'heatMap-960+disc': '(цена: 960 руб., скидка до 30%)',
    'autoNom-3600+disc': '(цена: 3600 руб., скидка до 30%)',
    'leftS-1080+disc': '(цена: 1080 руб., скидка до 30%)',
    'visCount': 'проверка',
    'lenQ': 'проверка',
    'faceRec': 'проверка',
    'controlEmp': 'проверка',
    'heatMap': 'проверка',
    'autoNom': 'проверка',
    'leftS': 'проверка',
    'pass/dv': 'Пропустить'
}

vn_dops_sms = {
    '100/30': '100 шт./ 30 суток',
    '500/90': '500 шт./ 90 суток',
    '1000/180': '1 000 шт./180 суток',
    '5000/365': '5 000 шт./365 суток'
}

vn_disc_val_to_name = {
    '0': 'Базовая стоимость: ',
    '10': 'Скидка 10%: ',
    '20': 'Скидка 20%: ',
    '30': 'Скидка 30%: '
}


### wats buttons

wats_big_tp_to_name = {
    'busyness/virt': 'ТП: бизнес/вирт. номер',
    'pack/min': 'ТП: пакеты минут',
}

wats_tp_to_name = {
    'bus/st': 'Бизнес. Стандарт',
    'bus/unlim': 'Бизнес. Безлимит',
    'virt/st': 'Виртуальный номер. Стандарт',
    'virt/unlim': 'Виртуальный номер. Безлимит',
    'bus/korp20': 'Бизнес. Корпорация 20',
    'bus/korp40': 'Бизнес. Корпорация 40',

    '3r/0m-500': '3 раб. места, 0 минут',
    '5r/600m-1100': '5 раб. мест, 600 минут',
    '10r/1200m-1900': '10 раб. мест, 1200 минут',
    '15r/3000m-4900': '15 раб. мест, 3000 минут',
    '30r/5000m-7900': '30 раб. мест, 5000 минут'

    # '100m-400': 'Пакет минут 100',
    # '500m-900': 'Пакет минут 500',
    # '1000m-1600': 'Пакет минут 1000',
    # '1500m-2350': 'Пакет минут 1500',
    # '2000m-3000': 'Пакет минут 2000',
    # '3000m-4400': 'Пакет минут 3000',
    # '5000m-7100': 'Пакет минут 5000'
}

wats_tp_bus = [
    'bus/st',
    'bus/unlim',
    'virt/st',
    'virt/unlim',
    'bus/korp20',
    'bus/korp40'
]

wats_tp_min = [
    '3r/0m-500',
    '5r/600m-1100',
    '10r/1200m-1900',
    '15r/3000m-4900',
    '30r/5000m-7900'
]

wats_num_cat_to_name = {
    'platinum-100000': 'Платиновый номер (100.000 ₽)',
    'gold-40000': 'Золотой номер (40.000 ₽)',
    'silver-15000': 'Серебряный номер (15.000 ₽)',
    'bronze-5000': 'Бронзовый номер (5.000 ₽)',
    'nocat': 'Без категории'
}

wats_num_abon_to_name = {
    'do5': 'до 5 пользователей:',
    'more5user': 'более 5 пользователей:',
    '1user': '1 пользователь:',
    '23user': '2 и 3 пользователи:',
    '20user': 'до 20 пользователей:',
    'more20User': 'более 20 пользователей:',
    '40user': 'до 40 пользователей:',
    'more40User': 'более 40 пользователей:'
}

wats_dop_to_name = {
    'vid/back-500': 'Виджет обратного звонка (500 ₽)',
    'virt/contact/2-600': 'Вирт. контактный центр, два места (600 ₽)',
    'virt/contact/2-508': 'Вирт. контактный центр, два места (508 ₽)',
    'virt/contact/dop-120': 'Вирт. контактный центр, доп. место (120 ₽)',
    'virt/contact/dop-102': 'Вирт. контактный центр, доп. место (102 ₽)',
    'other/crm-508': 'Интеграционный API с другими CRM (508 ₽)',
    'pass/wats': 'Пропустить',

    'more/workp': 'Дополнительное рабочее место',
    'mobile/workp-100': 'Мобильное рабочее место (100 ₽)',
    'anal-1': 'Аналитика (1 ₽)',
    'virt/contact/2-500': 'Вирт. контактный центр, два места (500 ₽)',
    'virt/contact/dop-100': 'Вирт. контактный центр, доп. место (100 ₽)',
    'amocrm-500': 'Интеграции с AmoCRM (500 ₽)',
    'other/crm-500': 'Интеграционный API с другими CRM (500 ₽)',

    'more/workp-80': 'мусор!',
    'more/workp-60': 'мусор!',
    'more/workp-40': 'мусор!',
    'more/workp-35': 'мусор!',
    'more/workp-30': 'мусор!',
    'more/workp-25': 'мусор!'
}


### iptv buttons


ip_service_names = {
    'public': 'Публичный показ',
    'private': 'Непубличный показ'
}

ip_main_ch_cut_names = {
    'sokr/office': 'Основные пакеты для офиса',
    'sokr/stb': 'Основные пакеты STB',
    'sokr/dvb': 'Основной пакет DVB-C',
    'sokr/ott': 'Основной пакет ОТТ',
    'sokr/sm': 'Основные  пакеты SMART TV'
}

ip_main_ch_names = {
    'sfera/other': 'Для сф. услуг, др. провайдер (400 ₽)',
    'sfera+/other': 'Для сф. услуг+, др. провайдер (750 ₽)',
    'dvb/sfera/nodop': 'Для сф. услуг DVB-C (без доп.) (300 ₽)',
    'sfera': 'Для сферы услуг (600 ₽)',
    'sfera+': 'Для сферы услуг + (600 ₽)',
    'kids': 'Для детей (400 ₽)',
    'kids+': 'Для детей + (800 ₽)',
    'dvb/lite': 'DVB-C - Публичный лайт (300 ₽)',
    'dvb/sfera': 'Для сферы услуг DVB-C (600 ₽)',
    'dvb/sfera+': 'Для сферы услуг+ DVB-C (1200 ₽)',
    'dvb/kids': 'Для детей DVB-C (400 ₽)',
    'dvb/kids+': 'Для детей + DVB-C (800 ₽)',

    'office': 'ТВ для офиса – 600 ₽/мес.',
    'office+': 'ТВ для офиса + - 1000 ₽/мес.',
    'office/sm': 'ТВ для офиса SMART TV - 600 ₽/мес.',
    'office+/sm': 'ТВ для офиса + SMART TV - 1000 ₽/мес.',
    'office/other/sm': 'ТВ для офиса др.провайдер SMART – 400 ₽/мес.',
    'office+/other/sm': 'ТВ для офиса + др.провайдер SMART – 750 ₽/мес.',
    'office/other': 'ТВ для офиса на интернете др.провайдера – 400 ₽/мес.',
    'office+/other': 'ТВ для офиса + на интернете др.провайдера – 750 ₽/мес.',
    'dvb/office/nodop': 'ТВ для офиса DVB-C – 250 ₽/мес.'
}



ip_dop_ch_names = {
    'khlprime': 'Телеканал KHL Prime (149 ₽)',
    'match': 'Матч! (100 ₽)',
    'supermatch': 'Суперматч! (450 ₽)',
    'china': 'Пакет Китай (360 ₽)',
    'smart': 'SMART TV публичный показ',
    'adult+': 'Пакет телеканалов «Пакет для взрослых +»',
    'pass/dopchannel': 'Пропустить'
}

ip_dop_names = {
    'videomuz': 'Видеопрокат и Музыкальный прокат',
    'content/contr': 'Управление контентом',
    'adv/konst': 'Конструктор рекламы (220 ₽ ежемес.)',
    'iptv/block': 'Добровольная блокировка IPTV (20 ₽ ежемес.)',
    'pass': 'Пропустить!'
}

ip_smart_names = {
    'sm.kids': 'Для детей (400 ₽)',
    'sm.kids+': 'Для детей + (800 ₽)',
    'sm.sfera': 'Для сферы услуг (600 ₽)',
    'sm.sfera+': 'Для сферы услуг + (1200 ₽)',
    'sm.sfera/other': 'Для сф. услуг; др. провайдер (400 ₽)',
    'sm.sfera+/other': 'Для сф. услуг +; др. провайдер (750 ₽)'
    # 'sferaSM3': 'Для сферы услуг 350 (350 ₽)',
    # 'sferaSM6': 'Базовый для детских учреждений (450 ₽)',
    # 'sferaSM12': 'Базовый для детских учреждений ВИП SMART TV (708.33 ₽)',
    # 'basekids': 'Для сферы услуг 650 (650 ₽)',
    # 'basekids+': 'Для сферы услуг 1250 (1250 ₽)'
}

ip_prokat_names = {
    1: 'Категория 1 (100 ₽ единовременно)',
    2: 'Категория 2 (150 ₽ единовременно)',
    3: 'Категория 3 (200 ₽ единовременно)',
    4: 'Категория 4 (250 ₽ единовременно)',
    5: 'Категория 5 (300 ₽ единовременно)',
    6: 'Категория 6 (350 ₽ единовременно)',
    7: 'Категория 7 (400 ₽ единовременно)',
    8: 'Категория 8 (450 ₽ единовременно)',
    9: 'Категория 9 (500 ₽ единовременно)',
    10: 'Категория 10 (750 ₽ единовременно)',
    11: 'Категория 11 (1000 ₽ единовременно)'
}


### keyboards


def kp_keyboard(user_used_service=None):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    for tar in data.keys():
        if user_used_service != None:
            if tar not in user_used_service:
                if tar == 'wifi' and 'wifi/control' in user_used_service and 'wifi/guest' in user_used_service:
                    pass
                elif tar == 'wats' and 'wats/busy' in user_used_service and 'wats/packmin' in user_used_service:
                    pass
                else:
                    keyboard_markup.insert(types.InlineKeyboardButton(text=kp_to_name[tar], callback_data=f'{tar}'))
        else:
            keyboard_markup.insert(types.InlineKeyboardButton(text=kp_to_name[tar], callback_data=f'{tar}'))

    if user_used_service != None:
        keyboard_markup.row(types.InlineKeyboardButton(text='Добавленные услуги', callback_data='watch-kp'))
        keyboard_markup.row(types.InlineKeyboardButton(text='Перейти к созданию КП', callback_data='create-kp'))
        keyboard_markup.row(types.InlineKeyboardButton(text='Все данные пользователя о тарифах', callback_data='watch-all'))
    else:
        keyboard_markup.insert(types.InlineKeyboardButton(text='Помогите! 🙏', callback_data=f'helpme'))
        # keyboard_markup.insert(types.InlineKeyboardButton(text='Тест КП', callback_data=f'1-kptest'))
    return keyboard_markup

def dep_keyboard(kp):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    deps = data[kp].keys()
    for dep in deps:
        keyboard_markup.insert(types.InlineKeyboardButton(text=dep_to_name[dep], callback_data=f'{kp}_{dep}'))
    return keyboard_markup

def after_kp():
    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.row(types.InlineKeyboardButton(text='К началу!', callback_data='to_begin'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Вернуться в B2Бот', url='http://t.me/b2b_teacher_bot'))
    return keyboard_markup

### internet keyboards

def int_mat_keyboard(kp, department):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
    for mat in internet_mats.keys():
        keyboard_markup.insert(types.InlineKeyboardButton(text=internet_mats[mat], callback_data=f'mat_{kp}_{department}_{mat}'))
    return keyboard_markup

def int_tech_keyboard(kp, dep, mat):
    department_techs = data[kp][dep][mat]
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
    for tech in department_techs.keys():
        keyboard_markup.insert(types.InlineKeyboardButton(text=internet_techs[tech], callback_data=f'tech_{kp}_{dep}_{mat}_{tech}'))
    return keyboard_markup

def int_speed_keyboard(kp, dep, mat, tech):
    tariffs = data[kp][dep][mat][tech]
    speeds = []
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
    for tariff in tariffs:
        for specs in tariffs[tariff]:
            if specs['speed'] not in speeds:
                speeds.append(specs['speed'])
    for speed in speeds:
        keyboard_markup.insert(types.InlineKeyboardButton(text=f"{speed}бит/с", callback_data=f'speed_{kp}_{dep}_{mat}_{tech}_{speed}'))
    return keyboard_markup

def int_tariff_keyboard(kp, dep, mat, tech, speed):
    tariffs = data[kp][dep][mat][tech]
    chosen_tariffs = []
    name_chosen_tariffs = []
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    for tariff in tariffs:
        for specs in tariffs[tariff]:
            if specs['speed'] == speed:
                discount = f', скидка до -{specs["discount"]}' if specs["discount"] else ''
                chosen_tariffs.append('ТАРИФ: "' + f'{internet_tariffs_names[tariff]}"')
                chosen_tariffs.append('(цена: ' + f'{tostr_(list(str(specs["price"])))}' + f' ₽{discount})')
                name_chosen_tariffs.append(tariff)
                name_chosen_tariffs.append(tariff)


    for t, name in zip(chosen_tariffs, name_chosen_tariffs):
        for i in data[kp][dep][mat][tech][name]:
            if speed in i['speed']:
                sale = i['discount']
        sale = str(sale)
        if '%' not in sale:
            sale+='%'

        keyboard_markup.insert(types.InlineKeyboardButton(text=t, callback_data=f'0t_{kp}_{dep}_{mat}_{tech}_{speed}_{name}_{sale}'))
    return keyboard_markup

def int_sale_keyboard(kp, dep, mat, tech, speed, name, sale):
    for specs in data[kp][dep][mat][tech][name]:
        if specs['speed'] == speed:
            price = int(specs['price'])
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    keyboard_markup.insert(types.InlineKeyboardButton(text=f'Цена: {price} ₽, скидка: 0%', callback_data=f'00t_{kp}_{dep}_{mat}_{tech}_{speed}_{name}_0%'))
    for i in range(int(int(sale[:-1]) / 10)):
        keyboard_markup.insert(types.InlineKeyboardButton(text=f'Цена: {int(price - (price * (((i+1)*10) / 100)))} ₽, скидка: {i+1}0%', callback_data=f'00t_{kp}_{dep}_{mat}_{tech}_{speed}_{name}_{i+1}0%'))
    return keyboard_markup


def int_fin_keyboard_more(dep):
    keyboard_markup = types.InlineKeyboardMarkup(resize=True)
    keyboard_markup.row(types.InlineKeyboardButton(text='Перейти к созданию КП', callback_data='create-kp'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить тарифы', callback_data=f'internet_{dep}'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить услуги / Главное Меню', callback_data=f'add-service'))
    keyboard_markup.row(types.InlineKeyboardButton(text='К началу!', callback_data='to_begin'))
    return keyboard_markup

def int_fin_keyboard_3():
    keyboard_markup = types.InlineKeyboardMarkup(resize=True)
    keyboard_markup.row(types.InlineKeyboardButton(text='Перейти к созданию КП', callback_data='create-kp'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить услуги / Главное Меню', callback_data=f'add-service'))
    keyboard_markup.row(types.InlineKeyboardButton(text='К началу!', callback_data='to_begin'))
    return keyboard_markup



### wifi keyboards



def wifi_service_keyboard(kp, dep, uid):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for service in data[kp][dep].keys():
        try:
            if service == 'guest' and 'wifi/guest' in used_service[uid]:
                pass
            elif service == 'control-3600' and 'wifi/control' in used_service[uid]:
                pass
            else:
                service_split = service.split('-')
                for text in service_split:
                    keyboard_markup.insert(types.InlineKeyboardButton(text=wifi_service_names[text],
                                                                      callback_data=f'{kp}_{dep}_{service}'))
        except:
            service_split = service.split('-')
            for text in service_split:
                keyboard_markup.insert(
                    types.InlineKeyboardButton(text=wifi_service_names[text], callback_data=f'{kp}_{dep}_{service}'))

    return keyboard_markup

def wifi_tp_keyboard(kp, dep, serv):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for tp in data[kp][dep][serv].keys():
        tp_split = tp.split('-')
        for text in tp_split:
            if serv == 'control-3600':
                keyboard_markup.insert(types.InlineKeyboardButton(text=wifi_control_sms_names[text],
                                                                  callback_data=f'{kp}_{dep}_{serv}_{tp}'))
            else:
                keyboard_markup.insert(
                    types.InlineKeyboardButton(text=wifi_guest_tp_names[text], callback_data=f'{kp}_{dep}_{serv}_{tp}'))
    return keyboard_markup

def wg_speed_keyboard(kp, dep, serv, tp):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for speed in data[kp][dep][serv][tp]['speed'][dep].keys():
        speed_price = data[kp][dep][serv][tp]['speed'][dep][speed]
        speed_split = speed.split('-')
        for text in speed_split:
            keyboard_markup.insert(
                types.InlineKeyboardButton(text=f'{wifi_guest_speed_names[text]}{speed_price} ₽',
                                           callback_data=f'{kp}_{dep}_{serv}_{tp}_speed-{speed_price}_wfdop'))
    return keyboard_markup

def wifi_dop_keyboard(kp, dep, serv, tp_or_sms):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for dop in data[kp][dep][serv][tp_or_sms]['dop'].keys():
        dop_split = dop.split('-')
        for text in dop_split:
            keyboard_markup.insert(types.InlineKeyboardButton(text=wifi_dop_names[text],
                                                              callback_data=f'{kp}_{dep}_{serv}_{tp_or_sms}_{dop}'))
    return keyboard_markup

def wifi_dop_more_keyboard(kp, dep, serv, tp_or_sms, used_dops=None):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for dop in data[kp][dep][serv][tp_or_sms]['dop'].keys():
        if dop in flatten(used_dops):
            pass
        else:
            dop_split = dop.split('-')
            for text in dop_split:
                keyboard_markup.insert(types.InlineKeyboardButton(text=wifi_dop_names[text],
                                                                  callback_data=f'{kp}_{dep}_{serv}_{tp_or_sms}_{dop}'))
    return keyboard_markup

def wifi_radar_keyboard(kp, dep, serv, sms, radar):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    radars = data[kp][dep][serv][sms]['dop'][radar].keys()
    for rad in radars:
        keyboard_markup.insert(types.InlineKeyboardButton(text=wifi_radar_adv_names[rad],
                                                          callback_data=f'{kp}_{dep}_{serv}_{sms}_{radar}-{rad}'))
    return keyboard_markup

def wifi_radar_lic_keyboard(kp, dep, serv, sms, radar, rad):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    radars_lics = data[kp][dep][serv][sms]['dop'][radar][rad].keys()
    for rad_lic in radars_lics:
        price = data[kp][dep][serv][sms]['dop'][radar][rad][rad_lic]
        keyboard_markup.insert(
            types.InlineKeyboardButton(text=wifi_radar_adv_lic_names[rad_lic].replace('(', f'({price} ₽'),
                                       callback_data=f'{kp}_{dep}_{serv}_{sms}_{radar}-{rad}-{rad_lic}'))
    return keyboard_markup

def wg_fin_keyboard(kp, dep, serv):
    keyboard_markup = types.InlineKeyboardMarkup(resize=True)
    keyboard_markup.row(types.InlineKeyboardButton(text='Перейти к созданию КП', callback_data='create-kp'))
    keyboard_markup.row(
        types.InlineKeyboardButton(text='Добавить тарифы', callback_data=f'{kp}_{dep}_{serv}_add-tar-wf'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить услуги / Главное Меню', callback_data=f'add-service'))
    keyboard_markup.row(types.InlineKeyboardButton(text='К началу!', callback_data='to_begin'))
    return keyboard_markup

def wg_fin_keyboard_3():
    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.row(types.InlineKeyboardButton(text='Перейти к созданию КП', callback_data='create-kp'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить услуги / Главное Меню', callback_data=f'add-service'))
    keyboard_markup.row(types.InlineKeyboardButton(text='К началу!', callback_data='to_begin'))
    return keyboard_markup


### iptv/hot keyboard


def iptv_hot_main_serv_keyboard(kp, dep):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for m_ch in data[kp][dep].keys():
        keyboard_markup.insert(types.InlineKeyboardButton(text=iptv_hot_main[m_ch], callback_data=f'{kp}_{dep}_{m_ch}'))
    return keyboard_markup

def iptv_hot_main_dop_ch_keyboard(kp, dep, ch, dop, uid=None):
    print(dop)
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    if dop in iptv_hot_main_ch_dop:
        m_ch_d_keys = data[kp][dep][ch]['main'][dop].keys()
        for m_ch_d in m_ch_d_keys:
            try:
                price = '-' + str(int(data[kp][dep][ch]['main'][dop][m_ch_d]))
                tx_dop = iptv_hot_choices[m_ch_d] + str(price).replace('-', '') + ' ₽' + '/1 пакет'
            except:
                price = ''
                tx_dop = iptv_hot_choices[m_ch_d]
            print('ifCBD')
            print(f'{kp}_{dep}_{ch}_{m_ch_d}{price}')
            keyboard_markup.insert(types.InlineKeyboardButton(text=tx_dop, callback_data=f'{kp}_{dep}_{ch}_{m_ch_d}{price}'))
    else:
        m_ch_d_keys = data[kp][dep][ch][dop].keys()
        for m_ch_d in m_ch_d_keys:
            try:
                price = '-'+str(int(data[kp][dep][ch][dop][m_ch_d]))
                tx_dop = iptv_hot_main_ch[m_ch_d] + str(price).replace('-', '') + ' ₽' + '/1 пакет'
            except:
                price = ''
                tx_dop = iptv_hot_main_ch[m_ch_d]
            print('elseCBD')
            print(f'{kp}_{dep}_{ch}_{m_ch_d}{price}')
            keyboard_markup.insert(types.InlineKeyboardButton(text=tx_dop, callback_data=f'{kp}_{dep}_{ch}_{m_ch_d}{price}'))
    return keyboard_markup

def iptv_hot_dop_keyboard(kp, dep, ch, dop, used_d=['nomatter']):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    dop_keys = data[kp][dep][ch][dop].keys()
    for dop_k in dop_keys:
        if dop_k in used_d:
            pass
        else:
            tx_dop = iptv_hot_dop_ch_names[dop_k]
            price = data[kp][dep][ch][dop][dop_k]
            keyboard_markup.insert(types.InlineKeyboardButton(text=tx_dop, callback_data=f'{dop_k}-{price}'))
    return keyboard_markup

def iptv_hot_info_keyboard(kp, dep, ch, dop):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    dop_keys = data[kp][dep][ch][dop].keys()
    for dop_k in dop_keys:
        tx_dop = iptv_hot_choices[dop_k]
        price = data[kp][dep][ch][dop][dop_k]
        keyboard_markup.insert(types.InlineKeyboardButton(text=tx_dop, callback_data=f'iptvlast_{dop_k}-{price}'))
    return keyboard_markup

def iptv_hot_fin_keyboard(kp, dep):
    keyboard_markup = types.InlineKeyboardMarkup(resize=True)
    keyboard_markup.row(types.InlineKeyboardButton(text='Перейти к созданию КП', callback_data='create-kp'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить тарифы', callback_data=f'{kp}_{dep}_add-tar'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить услуги / Главное Меню', callback_data=f'add-service'))
    keyboard_markup.row(types.InlineKeyboardButton(text='К началу!', callback_data='to_begin'))
    return keyboard_markup

def iptv_hot_fin_keyboard_3():
    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.row(types.InlineKeyboardButton(text='Перейти к созданию КП', callback_data='create-kp'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить услуги / Главное Меню', callback_data=f'add-service'))
    keyboard_markup.row(types.InlineKeyboardButton(text='К началу!', callback_data='to_begin'))
    return keyboard_markup


### vn_keyboards


def vn_service_keyboard(kp, dep):
    # организовать сохранение
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for serv in data[kp][dep].keys():
        keyboard_markup.insert(types.InlineKeyboardButton(text=vn_service_to_name[serv], callback_data=f'{kp}_{dep}_{serv}'))
    return keyboard_markup

def vn_tp_keyboard(kp, dep, serv):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for tp in data[kp][dep][serv].keys():
        keyboard_markup.insert(types.InlineKeyboardButton(text=vn_tp_to_name[tp], callback_data=f'{kp}_{dep}_{serv}_{tp}'))
    return keyboard_markup

def vn_sutki_keyboard(kp, dep, serv, tp):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for sutki in data[kp][dep][serv][tp]['saveDays'].keys():
        keyboard_markup.insert(types.InlineKeyboardButton(text=vn_sutki_to_name[sutki], callback_data=f'{kp}_{dep}_{serv}_{tp}_{sutki}'))
    return keyboard_markup

def vn_save_keyboard(kp, dep, serv, tp, sutki):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for save in data[kp][dep][serv][tp]['saveDays'][sutki]['saveType'].keys():
        if save == 'econom':
            price = int(data[kp][dep][serv][tp]['saveDays'][sutki]['saveType'][save][save])
            keyboard_markup.insert(types.InlineKeyboardButton(text=vn_save_to_name[save] + ': ' + str(price)+ '₽', callback_data=f'vn/dop_{save}-{price}'))
        elif save == 'reg':
            price = int(data[kp][dep][serv][tp]['saveDays'][sutki]['saveType'][save])
            keyboard_markup.insert(types.InlineKeyboardButton(text=vn_save_to_name[save] + ': ' + str(price)+ '₽', callback_data=f'vn/dop_{save}-{price}'))
        else:
            keyboard_markup.insert(types.InlineKeyboardButton(text=vn_save_to_name[save], callback_data=f'{kp}_{dep}_{serv}_{tp}_{sutki}_{save}'))
    return keyboard_markup

def vn_speed_keyboard(kp, dep, serv, tp, sutki, save):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for speed in data[kp][dep][serv][tp]['saveDays'][sutki]['saveType'][save].keys():
        price = int(data[kp][dep][serv][tp]['saveDays'][sutki]['saveType'][save][speed])
        keyboard_markup.insert(types.InlineKeyboardButton(text=vn_traffic_to_name[speed] + ' : ' + str(price) + '₽', callback_data=f'vn/dop_{speed}-{price}'))
    return keyboard_markup

def vn_dop_keyboard(kp, dep, serv, tp, used_dops = ['nomatter']):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for dop in data[kp][dep][serv][tp]['dop'].keys():
        if dop in used_dops:
            pass
        elif dop == 'pass':
            # в обработчике если доп = pass не добавлять в user_data
            keyboard_markup.insert(types.InlineKeyboardButton(text=vn_big_dop_to_name[dop], callback_data=f'vn/fin_{dop}'))
        else:
            keyboard_markup.insert(types.InlineKeyboardButton(text=vn_big_dop_to_name[dop], callback_data=f'vn/dop/more_{dop}'))
    return keyboard_markup

def vn_dop_more_keyboard(kp, dep, serv, tp, dop, used_dops, used_dops_vid):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    print('used_dops_vid', used_dops_vid)
    if dop not in data[kp][dep][serv][tp]['dop'].keys():
        dop = 'vidAnal'
    for dop_more in data[kp][dep][serv][tp]['dop'][dop].keys():
        if dop == 'vidAnal':
            if any(i in dop_more for i in used_dops_vid):
                pass
            else:
                if dop_more == 'pass/dv':
                    if len(used_dops_vid) != 0:
                        if len(used_dops) != 2:
                            keyboard_markup.insert(types.InlineKeyboardButton(text=vn_dops_to_name[dop_more], callback_data=f'vn/dop_{dop_more}'))
                        else:
                            keyboard_markup.insert(types.InlineKeyboardButton(text=vn_dops_to_name[dop_more], callback_data=f'vn/fin_{dop_more}'))
                    else:
                        pass
                else:
                    # в обработчике команды не добавлять dop_more в user_data!
                    keyboard_markup.insert(types.InlineKeyboardButton(text=vn_dops_to_name[dop_more], callback_data=f'vn/dop/disc_{dop_more}'))
                    keyboard_markup.insert(types.InlineKeyboardButton(text=vn_dops_to_name[f'{dop_more}+disc'], callback_data=f'vn/dop/disc_{dop_more}'))
        else:
            if len(used_dops) in [0,1]:
                price = int(data[kp][dep][serv][tp]['dop'][dop][dop_more])
                keyboard_markup.insert(types.InlineKeyboardButton(text=vn_dops_to_name[dop_more] + ' : ' + str(price) + '₽', callback_data=f'vn/dop_{dop_more}-{price}'))
            else:
                price = int(data[kp][dep][serv][tp]['dop'][dop][dop_more])
                keyboard_markup.insert(types.InlineKeyboardButton(text=vn_dops_to_name[dop_more] + ' : ' + str(price) + '₽', callback_data=f'vn/fin_{dop_more}-{price}'))
    return keyboard_markup

def vn_dop_disc_keyboard(kp, dep, serv, tp, dop, dop_more, used_dops, used_dops_vid):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    if dop not in data[kp][dep][serv][tp]['dop'].keys():
        dop = 'vidAnal'
    if dop_more not in data[kp][dep][serv][tp]['dop'][dop].keys():
        dop_more = [i for i in vn_dops_to_name if i.startswith(dop_more)][0]
    for discount in sorted(data[kp][dep][serv][tp]['dop'][dop][dop_more]):
        if len(used_dops) != 2:
            if len(used_dops_vid) == 6:
                price = int(int(dop_more.split('-')[1]) * float(1-(int(discount)*0.01)))
                # print(f'vn/fin_{dop_more.replace(dop_more[dop_more.find("-")+1:], "")}{price}')
                keyboard_markup.insert(types.InlineKeyboardButton(text=vn_disc_val_to_name[discount] + str(price) + '₽', callback_data=f'vn/dop_{dop_more.replace(dop_more[dop_more.find("-")+1:], "")}{price}'))
            else:
                price = int(int(dop_more.split('-')[1]) * float(1-(int(discount)*0.01)))
                # print(f'vn/fin_{dop_more.replace(dop_more[dop_more.find("-")+1:], "")}{price}')
                keyboard_markup.insert(types.InlineKeyboardButton(text=vn_disc_val_to_name[discount] + str(price) + '₽', callback_data=f'vn/dop/more_{dop_more.replace(dop_more[dop_more.find("-")+1:], "")}{price}'))
        else:
            if len(used_dops_vid) == 6:
                price = int(int(dop_more.split('-')[1]) * float(1-(int(discount)*0.01)))
                # print(f'vn/fin_{dop_more.replace(dop_more[dop_more.find("-")+1:], "")}{price}')
                keyboard_markup.insert(types.InlineKeyboardButton(text=vn_disc_val_to_name[discount] + str(price) + '₽', callback_data=f'vn/fin_{dop_more.replace(dop_more[dop_more.find("-")+1:], "")}{price}'))
            else:
                price = int(int(dop_more.split('-')[1]) * float(1-(int(discount)*0.01)))
                # print(f'vn/fin_{dop_more.replace(dop_more[dop_more.find("-")+1:], "")}{price}')
                keyboard_markup.insert(types.InlineKeyboardButton(text=vn_disc_val_to_name[discount] + str(price) + '₽', callback_data=f'vn/dop/more_{dop_more.replace(dop_more[dop_more.find("-")+1:], "")}{price}'))
    return keyboard_markup

def vn_fin_keyboard(kp, dep):
    keyboard_markup = types.InlineKeyboardMarkup(resize=True)
    keyboard_markup.row(types.InlineKeyboardButton(text='Перейти к созданию КП', callback_data='create-kp'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить тарифы', callback_data=f'{kp}_{dep}_add-tar-vn'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить услуги / Главное Меню', callback_data=f'add-service'))
    keyboard_markup.row(types.InlineKeyboardButton(text='К началу!', callback_data='to_begin'))
    return keyboard_markup

def vn_fin_keyboard_3():
    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.row(types.InlineKeyboardButton(text='Перейти к созданию КП', callback_data='create-kp'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить услуги / Главное Меню', callback_data=f'add-service'))
    keyboard_markup.row(types.InlineKeyboardButton(text='К началу!', callback_data='to_begin'))
    return keyboard_markup


### wats keyboard

def wats_big_tp_keyboard(kp, dep, uid):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for big_tp in data[kp][dep].keys():
        if big_tp == 'busyness/virt' and 'wats/busy' in used_service[uid]:
            pass
        elif big_tp == 'pack/min' and 'wats/packmin' in used_service[uid]:
            pass
        else:
            keyboard_markup.insert(types.InlineKeyboardButton(text=wats_big_tp_to_name[big_tp], callback_data=f'{kp}_{dep}_{big_tp}'))
    return keyboard_markup

def wats_num_cat_keyboard(kp, dep, big_tp, tp, dop):
    print(dop)
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    if dop == 'numbCat':
        for cat in data[kp][dep][big_tp][tp][dop].keys():
            keyboard_markup.insert(types.InlineKeyboardButton(text=wats_num_cat_to_name[cat], callback_data=f'{cat}'))
    return keyboard_markup

def wats_num_users_keyboard(kp, dep, big_tp, tp, dop):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for us_count in data[kp][dep][big_tp][tp][dop][dep].keys():
        price = data[kp][dep][big_tp][tp][dop][dep][us_count]
        print('here')
        print(price)
        try:
            price = int(price)
            keyboard_markup.insert(types.InlineKeyboardButton(text=wats_num_abon_to_name[us_count] + ' ' + str(price) + '₽', callback_data=f'{us_count}-{price}'))
        except:
            print(f'{us_count}_{price}')
            keyboard_markup.insert(types.InlineKeyboardButton(text=wats_num_abon_to_name[us_count][:-1], callback_data=f'{us_count}_{price}'))
    return keyboard_markup

def wats_in_tp_keyboard(kp, dep, big_tp):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    if big_tp == 'busyness/virt':
        for tp in data[kp][dep][big_tp].keys():
            keyboard_markup.insert(types.InlineKeyboardButton(text=wats_tp_to_name[tp], callback_data=f'{kp}_{dep}_{big_tp}_{tp}'))
    else:
        for tp in data[kp][dep][big_tp]['speed'].keys():
            price = str(data[kp][dep][big_tp]['speed'][tp])
            keyboard_markup.insert(types.InlineKeyboardButton(text=wats_tp_to_name[tp] + ': ' + str(price) + '₽', callback_data=f'{kp}_{dep}_{big_tp}_{tp}'))
    return keyboard_markup

def wats_dop_keyboard(kp, dep, big_tp, tp, dop, used_d=['nomatter']):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    print(kp, dep, big_tp, tp, dop)
    if big_tp == 'busyness/virt':
        for dop_k in data[kp][dep][big_tp][tp][dop].keys():
            if dop_k in used_d:
                pass
            else:
                keyboard_markup.insert(types.InlineKeyboardButton(text=wats_dop_to_name[dop_k], callback_data=f'{dop_k}'))
    elif big_tp == 'pack/min':
        for dop_k in data[kp][dep][big_tp][dop].keys():
            if dop_k in used_d or any(i.split('-')[0] == dop_k for i in used_d):
                pass
            else:
                if dop_k == 'more/workp':
                    price = int(data[kp][dep][big_tp][dop][dop_k][tp])
                    keyboard_markup.insert(types.InlineKeyboardButton(text=wats_dop_to_name[dop_k] + ' (' + str(price) + '₽)', callback_data=f'{dop_k}-{price}'))
                else:
                    keyboard_markup.insert(types.InlineKeyboardButton(text=wats_dop_to_name[dop_k], callback_data=f'{dop_k}'))
    return keyboard_markup

def wats_fin_keyboard(kp, dep, big_tp):
    keyboard_markup = types.InlineKeyboardMarkup(resize=True)
    keyboard_markup.row(types.InlineKeyboardButton(text='Перейти к созданию КП', callback_data='create-kp'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить тарифы', callback_data=f'{kp}_{dep}_{big_tp}_add-tar-wa'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить услуги / Главное Меню', callback_data=f'add-service'))
    keyboard_markup.row(types.InlineKeyboardButton(text='К началу!', callback_data='to_begin'))
    return keyboard_markup

def wats_fin_keyboard_3():
    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.row(types.InlineKeyboardButton(text='Перейти к созданию КП', callback_data='create-kp'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить услуги / Главное Меню', callback_data=f'add-service'))
    keyboard_markup.row(types.InlineKeyboardButton(text='К началу!', callback_data='to_begin'))
    return keyboard_markup


### iptv keyboards


def ip_service_keyboard(kp, dep):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for service in data[kp][dep].keys():
            keyboard_markup.insert(types.InlineKeyboardButton(text=ip_service_names[service], callback_data=f'{kp}_{dep}_{service}'))
    return keyboard_markup

def ip_main_ch_cut_keyboard(kp, dep, serv):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    main_ch_keys = data[kp][dep][serv]['main'].keys()
    for main_ch in main_ch_keys:
        keyboard_markup.insert(types.InlineKeyboardButton(text=ip_main_ch_cut_names[main_ch], callback_data=f'{kp}_{dep}_{serv}_{main_ch}'))
    return keyboard_markup

def ip_main_ch_keyboard(kp, dep, serv, cut):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    main_ch_keys = data[kp][dep][serv]['main'][cut].keys()
    for main_ch in main_ch_keys:
        keyboard_markup.insert(types.InlineKeyboardButton(text=ip_main_ch_names[main_ch], callback_data=f'{kp}_{dep}_{serv}_{main_ch}_dopchannel'))
    return keyboard_markup

def ip_dop_ch_keyboard(kp, dep, serv, channel=None, user_data=None):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    dop_ch_keys = data[kp][dep][serv]['dopchannel'].keys()
    if channel == None:
        for dop_ch in dop_ch_keys:
            keyboard_markup.insert(
                types.InlineKeyboardButton(text=ip_dop_ch_names[dop_ch], callback_data=f'{kp}_{dep}_{serv}_{dop_ch}_dopchannel'))
            print(f'{kp}_{dep}_{serv}_{dop_ch}_dopchannel')
        return keyboard_markup
    else:
        used_dops = []
        splitted = [i.split('-')[0] for i in user_data.split('_')]
        print(splitted)
        for elem in splitted:
            if elem in dop_ch_keys or 'radar' in elem or 'adv' in elem:
                for j in elem.split('-'):
                    used_dops.append(j)
        dop_keys = data[kp][dep][serv]['dopchannel'].keys()

        for dop in dop_keys:
            try:
                if not any(x in used_dops for x in dop.split('-')):
                    print(f'user_dataaaaaaaa check len{len(user_data)}')
                    print(user_data)
                    print(f'serv {serv}')
                    if len(user_data.split('_')) != [8 if serv == 'public' else 7][0]:
                    # if not all(x in [j.split('-')[0] for j in user_data.split('_')[-5:]] for x in list(data[kp][dep][serv]['dopchannel'].keys())[:-1]):
                        keyboard_markup.insert(types.InlineKeyboardButton(text=ip_dop_ch_names[dop], callback_data=f'{kp}_{dep}_{serv}_{dop}_dopchannel'))
                        print()
                        print('button!')
                        print(f'{kp}_{dep}_{serv}_{dop}_dopchannel')
                    else:
                        print('else in else (FINAL)')
                        keyboard_markup.insert(types.InlineKeyboardButton(text=ip_dop_ch_names[dop], callback_data=f'{kp}_{dep}_{serv}_{dop}_dopchannel-fin'))
                        print('button!')
                        print(f'{kp}_{dep}_{serv}_{dop}_dopchannel-fin')
            except:
                print('зашел в except v ip_dop_keyboard')
                keyboard_markup.insert(types.InlineKeyboardButton(text=ip_dop_ch_names[dop], callback_data=f'{kp}_{dep}_{serv}_{dop}_dopchannel'))

        return keyboard_markup


def ip_dop_keyboard(kp, dep, serv, dop_type, dop_clicked=None, user_data=None):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    if dop_clicked == None:
        dop_keys = data[kp][dep][serv][dop_type].keys()
        print(dop_keys)
        for dop in dop_keys:
            try:
                dop_split = dop.split('-')
                for text in dop_split:
                    keyboard_markup.insert(
                        types.InlineKeyboardButton(text=ip_dop_names[text], callback_data=f'{kp}_{dep}_{serv}_{dop_type}_{dop}'))
            except:
                keyboard_markup.insert(types.InlineKeyboardButton(text=ip_dop_names[dop], callback_data=f'{kp}_{dep}_{serv}_{dop_type}_{dop}'))

        return keyboard_markup
    else:
        used_dops = []
        splitted = user_data.split('_')
        for elem in splitted:
            if elem in ip_dop_names.keys() or 'videomuz' in elem:
                for j in elem.split('-'):
                    used_dops.append(j)
        print('used_dops')
        print(used_dops)
        dop_keys = data[kp][dep][serv][dop_type].keys()
        for dop in dop_keys:
            try:
                if not any(x in used_dops for x in dop.split('-')):
                    dop_split = dop.split('-')
                    for text in dop_split:
                        print('user_dataaaaaaaaaaaaaaa')
                        print(user_data)
                        print(f'serv {serv}')
                        if len(user_data.split('_')) != [8 if serv == 'public' else 7][0] or any(x in ip_dop_names for x in used_dops):
                            keyboard_markup.insert(types.InlineKeyboardButton(text=ip_dop_names[text], callback_data=f'{kp}_{dep}_{serv}_{dop_type}_{dop}'))
                        else:
                            print('else in else')
                            keyboard_markup.insert(types.InlineKeyboardButton(text=ip_dop_names[text], callback_data=f'{kp}_{dep}_{serv}_{dop_type}_{dop}_pass'))
                            print(f'{kp}_{dep}_{serv}_{dop_type}_{dop}_pass')
            except:
                print('зашел в except v ip_dop_keyboard')
                keyboard_markup.insert(types.InlineKeyboardButton(text=ip_dop_names[dop], callback_data=f'{kp}_{dep}_{serv}_{dop_type}_{dop}'))

        return keyboard_markup

def ip_smart_keyboard(kp, dep, serv, user_data):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    smart_keys = data[kp][dep][serv]['dopchannel']['smart'].keys()
    print(smart_keys)
    for i in smart_keys:
        print(ip_smart_names[i])
        price = str(data[kp][dep][serv]['dopchannel']['smart'][i])
        print(f'{kp}_{dep}_{serv}_smart-{i}-{price}_dopchannel')
        if len(user_data.split('_')) != 8:
            keyboard_markup.insert(types.InlineKeyboardButton(text=ip_smart_names[i],
                                                          callback_data=f'{kp}_{dep}_{serv}_smart-{i}-{price}_dopchannel'))
        else:
            keyboard_markup.insert(types.InlineKeyboardButton(text=ip_smart_names[i],
                                                              callback_data=f'{kp}_{dep}_{serv}_smart-{i}-{price}_dopchannel-fin'))
    return keyboard_markup

def ip_prokat_keyboard(kp, dep, serv):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    prokat_keys = data[kp][dep][serv]['dop']['videomuz'].keys()
    for i in prokat_keys:
        price = str(data[kp][dep][serv]['dop']['videomuz'][i])
        print(f'{kp}_{dep}_{serv}_dop_videomuz-{i}-{price}')
        keyboard_markup.insert(types.InlineKeyboardButton(text=ip_prokat_names[i],
                                                          callback_data=f'{kp}_{dep}_{serv}_dop_videomuz-{i}-{price}'))
    return keyboard_markup

def ip_fin_keyboard(kp, dep):
    keyboard_markup = types.InlineKeyboardMarkup(resize=True)
    keyboard_markup.row(types.InlineKeyboardButton(text='Перейти к созданию КП', callback_data='create-kp'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить тарифы', callback_data=f'{kp}_{dep}_add-tar-ip'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить услуги / Главное Меню', callback_data=f'add-service'))
    keyboard_markup.row(types.InlineKeyboardButton(text='К началу!', callback_data='to_begin'))
    return keyboard_markup

def ip_fin_keyboard_3():
    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.row(types.InlineKeyboardButton(text='Перейти к созданию КП', callback_data='create-kp'))
    keyboard_markup.row(types.InlineKeyboardButton(text='Добавить услуги / Главное Меню', callback_data=f'add-service'))
    keyboard_markup.row(types.InlineKeyboardButton(text='К началу!', callback_data='to_begin'))
    return keyboard_markup


# bot_functions


@dp.message_handler(commands=['start'], state='*')
async def start_kp(message: types.Message, state):
    await state.finish()
    print(f'msg chat id: {message.chat.id}')
    try:
        await bot.send_message(message.chat.id, 'Здравствуйте! Выберите услугу:',
                               parse_mode='Markdown',
                               reply_markup=kp_keyboard())
        user_data[message.chat.id] = {'main': []}
        used_service[message.chat.id] = []
        used_user_data[message.chat.id] = []
    except Exception:
        print(traceback.format_exc())


@dp.callback_query_handler(lambda cb: cb.data == 'add-service')
async def more_start_kp(callback_query: types.callback_query, state):
    cb = callback_query
    try:
        try:
            if 'wifi' in user_data[cb.from_user.id]['main'][0]:
                used_service[cb.from_user.id].append(
                    'wifi/guest' if 'guest' in user_data[cb.from_user.id]['main'][0] else 'wifi/control')
                used_user_data[cb.from_user.id].append(user_data[cb.from_user.id]['main'])
            elif 'wats' in user_data[cb.from_user.id]['main'][0]:
                used_service[cb.from_user.id].append('wats/busy' if 'busyness/virt' in user_data[cb.from_user.id]['main'][0] else 'wats/packmin')
                used_user_data[cb.from_user.id].append(user_data[cb.from_user.id]['main'])
            else:
                used_service[cb.from_user.id].append(user_data[cb.from_user.id]['main'][0].split('_')[0])
                used_user_data[cb.from_user.id].append(user_data[cb.from_user.id]['main'])

        except:
            if 'wifi' in user_data[cb.from_user.id]['main'][0]:
                used_service[cb.from_user.id] = [
                    'wifi/guest' if 'guest' in user_data[cb.from_user.id]['main'][0] else 'wifi/control']
                used_user_data[cb.from_user.id] = [user_data[cb.from_user.id]['main']]
            elif 'wats' in user_data[cb.from_user.id]['main'][0]:
                used_service[cb.from_user.id] = ['wats/busy' if 'busyness/virt' in user_data[cb.from_user.id]['main'][0] else 'wats/packmin']
                used_user_data[cb.from_user.id] = [user_data[cb.from_user.id]['main']]
            else:
                used_service[cb.from_user.id] = [user_data[cb.from_user.id]['main'][0].split('_')[0]]
                used_user_data[cb.from_user.id] = [user_data[cb.from_user.id]['main']]
        print(used_service)
        print(used_user_data)
        user_data[cb.from_user.id] = {'main': []}
        more_start_text = 'Вы добавили максимальное количество услуг. Можете сформировать коммерческое предложение!' if len(used_service[cb.from_user.id]) == 8 else 'Вы можете выбрать ещё услугу, посмотреть услуги, добавленные в КП, или сформировать КП'
        await bot.send_message(cb.from_user.id, text=more_start_text,
                               parse_mode='Markdown',
                               reply_markup=kp_keyboard(user_used_service=used_service[cb.from_user.id]))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())


@dp.callback_query_handler(lambda cb: cb.data in kp_to_name.keys())
async def department(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data
    try:
        await bot.send_message(cb.from_user.id, 'Пожалуйста, выберите филиал:',
                               reply_markup=dep_keyboard(cb_data))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())


### internet



@dp.callback_query_handler(lambda cb: (cb.data.split('_')[0] == 'internet') and (cb.data.split('_')[1] in dep_to_name))
async def int_main_keyboard_messages(callback_query: types.CallbackQuery, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    print(cb_data)
    kp = cb_data[0]
    dep = cb_data[1]
    try:
        await bot.send_message(cb.from_user.id, 'Выберите технологию подключения:',
                               reply_markup=int_mat_keyboard(kp, dep))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())


@dp.callback_query_handler(lambda cb: cb.data.split('_')[0] == 'mat')
async def int_material_handler(callback_query: types.CallbackQuery, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    print(cb_data)
    kp = cb_data[1]
    dep = cb_data[2]
    mat = cb_data[3]
    try:
        await bot.send_message(cb.from_user.id, text='Выберите!                ', reply_markup=int_tech_keyboard(kp, dep, mat))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        print(traceback.format_exc())
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        await state.finish()
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())


@dp.callback_query_handler(lambda cb: cb.data.split('_')[0] == 'tech')
async def int_technology_handler(callback_query: types.CallbackQuery, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    print(cb_data)
    kp = cb_data[1]
    dep = cb_data[2]
    mat = cb_data[3]
    tech = cb_data[4]
    try:
        await bot.send_message(cb.from_user.id, 'Выберите скорость:', reply_markup=int_speed_keyboard(kp, dep, mat, tech))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await state.finish()
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())


@dp.callback_query_handler(lambda cb: cb.data.split('_')[0] == 'speed')
async def int_tariff_handler(callback_query: types.CallbackQuery, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    print(cb_data)
    kp = cb_data[1]
    dep = cb_data[2]
    mat = cb_data[3]
    tech = cb_data[4]
    speed = cb_data[5]
    try:
        await bot.send_message(cb.from_user.id, 'Выберите тариф:', reply_markup=int_tariff_keyboard(kp, dep, mat, tech, speed))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await state.finish()
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())


@dp.callback_query_handler(lambda cb: cb.data.split('_')[0] == '0t')
async def int_final_handler(callback_query: types.CallbackQuery, state):
    cb = callback_query
    print(cb.data)
    if cb.data.split('_')[-1] == '0%':
        try:
            print('Fin!!!!!!!!!')
            data = cb.data.split('_')
            print('datasale0')
            print(data)
            kp = data[1]
            dep = data[2]
            mat = data[3]
            tech = data[4]
            speed = data[5]
            name_tariff = data[6]
            try:
                user_data[cb.from_user.id]['main'].append(cb.data[3:])
            except:
                user_data[cb.from_user.id] = {'main': []}
                user_data[cb.from_user.id]['main'].append(cb.data[3:])
            print(user_data)
            if len(user_data[cb.from_user.id]['main']) <= 2:
                len_for_grammar = len(user_data[cb.from_user.id]['main'])
                letter = '' if len_for_grammar == 2 else 'а'
                await bot.send_message(cb.from_user.id,
                                       'Вы можете сформировать коммерческое предложение или добавить еще {} тариф{} для сравнения!'.format(3-len_for_grammar, letter),
                                       reply_markup=int_fin_keyboard_more(dep))
                print('МЕНЬШЕ 3 ИДЕТ ДАЛЬШЕ')
                print(user_data[cb.from_user.id]['main'])
            else:
                await bot.send_message(cb.from_user.id,
                                       'Вы добавили 3 тарифа для сравнения!',
                                       reply_markup=int_fin_keyboard_3())
                print('ЕСТЬ 3 ТАРИФА')
                print(user_data[cb.from_user.id]['main'])

        except Exception:
            user_data[cb.from_user.id] = {'main': []}
            used_service[cb.from_user.id] = []
            used_user_data[cb.from_user.id] = []
            print(traceback.format_exc())
            await state.finish()
            await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                                   reply_markup=kp_keyboard())

    else:
        try:
            data = cb.data.split('_')
            print('data so skidkoi!!!')
            print(data)

            kp = data[1]
            dep = data[2]
            mat = data[3]
            tech = data[4]
            speed = data[5]
            name_tariff = data[6]
            sale_amount = data[7]
            await bot.send_message(cb.from_user.id,'Выберите допустимый объем скидки:',
                                   reply_markup=int_sale_keyboard(kp, dep, mat, tech, speed, name_tariff, sale_amount))
        except Exception:
            user_data[cb.from_user.id] = {'main': []}
            used_service[cb.from_user.id] = []
            used_user_data[cb.from_user.id] = []
            print(traceback.format_exc())
            await state.finish()
            await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                                   reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: cb.data.split('_')[0] == '00t')
async def int_final_handler_2(callback_query: types.CallbackQuery, state):
    cb = callback_query
    print(cb.data)
    try:
        print('Fin')
        data = cb.data.split('_')
        kp = data[1]
        dep = data[2]
        mat = data[3]
        tech = data[4]
        speed = data[5]
        name_tariff = data[6]
        try:
            user_data[cb.from_user.id]['main'].append(cb.data[4:])
        except:
            user_data[cb.from_user.id] = {'main': []}
            user_data[cb.from_user.id]['main'].append(cb.data[4:])
        print(user_data)
        if len(user_data[cb.from_user.id]['main']) <= 2:
            len_for_grammar = len(user_data[cb.from_user.id]['main'])
            letter = '' if len_for_grammar == 2 else 'а'
            await bot.send_message(cb.from_user.id,
                                   'Вы можете сформировать коммерческое предложение или добавить еще {} тариф{} для сравнения!'.format(3-len_for_grammar, letter),
                                   reply_markup=int_fin_keyboard_more(dep))
            print('МЕНЬШЕ 3 ИДЕТ ДАЛЬШЕ')
            print(user_data[cb.from_user.id]['main'])
        else:
            await bot.send_message(cb.from_user.id,
                                   'Вы добавили 3 тарифа для сравнения!',
                                   reply_markup=int_fin_keyboard_3())
            print('ЕСТЬ 3 ТАРИФА')
            print(user_data[cb.from_user.id]['main'])

    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await state.finish()
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())



### wifi


@dp.callback_query_handler(lambda cb: cb.data.split('_')[-1] in dep_to_name and 'wifi' in cb.data.split('_')[0])
async def wifi_main_serv(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    print(cb.data)
    try:
        await bot.send_message(cb.from_user.id, 'Выберите услугу:',
                               reply_markup=wifi_service_keyboard(kp, dep, cb.from_user.id))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: cb.data.split('_')[-1] in wifi_service_names or cb.data.split('_')[-1] == 'add-tar-wf')
async def wifi_tp(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    text_ = 'Выберите тарифный план:' if serv == 'guest' else 'Выберите вариант предоставления услуги "Авторизация пользователей:'
    try:
        user_data[cb.from_user.id]['main'].append(cb.data.replace('_add-tar-wf', ''))
        print(user_data)
        await bot.send_message(cb.from_user.id,
                               text=text_,
                               reply_markup=wifi_tp_keyboard(kp, dep, serv))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: cb.data.split('_')[-1] in wifi_guest_tp_names or cb.data.split('_')[-1] in wifi_control_sms_names)
async def wg_speed_and_wc_dop(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    tp_or_sms = cb_data[3]
    print(cb.data)
    try:
        user_data[cb.from_user.id]['main'][-1] += '_' + cb_data[-1]
        print(user_data)
        if serv == 'guest':
            await bot.send_message(cb.from_user.id, 'Выберите скорость передачи данных:',
                                   reply_markup=wg_speed_keyboard(kp, dep, serv, tp_or_sms))
        else:
            await bot.send_message(cb.from_user.id, 'Выберите дополнительные услуги или нажмите пропустить:',
                                   reply_markup=wifi_dop_keyboard(kp, dep, serv, tp_or_sms))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: cb.data.split('_')[-1] == 'wfdop')
async def wifi_dop(callback_query: types.callback_query, state):
    cb = callback_query
    print(cb.data)
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    tp_or_sms = cb_data[3]
    speed = cb_data[4]
    print(speed)
    try:
        if serv == 'guest':
            user_data[cb.from_user.id]['main'][-1] += '_' + speed
        elif tp_or_sms not in user_data[cb.from_user.id]['main'][-1]:
            user_data[cb.from_user.id]['main'][-1] += '_' + tp_or_sms
        else:
            print('polnaya pizda')
        print(user_data)
        await bot.send_message(cb.from_user.id, 'Выберите дополнительные услуги или нажмите пропустить:',
                               reply_markup=wifi_dop_keyboard(kp, dep, serv, tp_or_sms))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[0] == 'wifi') and
                                      ((cb.data.split('_')[-1] in wifi_dop_names and cb.data.split('_')[-1] not in ['radar', 'adv', 'wifi/pass']) or (
                                              cb.data.split('_')[-1].split('-')[-1] in wifi_radar_adv_lic_names or
                                              cb.data.split('_')[-1] in wifi_radar_adv_lic_names)))
async def wifi_dop_more(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    tp_or_sms = cb_data[3]
    dop = cb_data[4]
    try:
        user_data[cb.from_user.id]['main'][-1] += '_' + dop
        print(user_data)
        used_dops = [[i, i.split('-')[0]] for i in user_data[cb.from_user.id]['main'][-1].split('_') if
                     (i in wifi_dop_names) or (i.split('-')[0] in wifi_dop_names)]
        print(used_dops)
        if serv == 'guest':
            if all(i in flatten(used_dops) for i in check_dop_guest):
                print('fin')
                print(user_data)
                if len(user_data[cb.from_user.id]['main']) <= 2:
                    len_for_grammar = len(user_data[cb.from_user.id]['main'])
                    letter = '' if len_for_grammar == 2 else 'а'
                    await bot.send_message(cb.from_user.id,
                                           'Вы можете сформировать коммерческое предложение или добавить еще {} тариф{} для сравнения!'.format(
                                               3 - len_for_grammar, letter),
                                           reply_markup=wg_fin_keyboard(kp, dep, serv))
                else:
                    await bot.send_message(cb.from_user.id,
                                           f'Вы добавили 3 тарифа для сравнения!',
                                           reply_markup=wg_fin_keyboard_3())
            else:
                await bot.send_message(cb.from_user.id, 'Выберите ещё дополнительные услуги или нажмите пропустить:',
                                       reply_markup=wifi_dop_more_keyboard(kp, dep, serv, tp_or_sms, used_dops))
        else:
            if all(i in flatten(used_dops) for i in check_dop_control):
                print('fin')
                print(user_data)
                if len(user_data[cb.from_user.id]['main']) <= 2:
                    len_for_grammar = len(user_data[cb.from_user.id]['main'])
                    letter = '' if len_for_grammar == 2 else 'а'
                    await bot.send_message(cb.from_user.id,
                                           'Вы можете сформировать коммерческое предложение или добавить еще {} тариф{} для сравнения!'.format(
                                               3 - len_for_grammar, letter),
                                           reply_markup=wg_fin_keyboard(kp, dep, serv))
                else:
                    await bot.send_message(cb.from_user.id,
                                           f'Вы добавили 3 тарифа для сравнения!',
                                           reply_markup=wg_fin_keyboard_3())
            else:
                await bot.send_message(cb.from_user.id, 'Выберите ещё дополнительные услуги или нажмите пропустить:',
                                       reply_markup=wifi_dop_more_keyboard(kp, dep, serv, tp_or_sms, used_dops))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[-1] in ['radar', 'adv']) or (
        cb.data.split('_')[-1] == 'pass' and cb.data.split('_')[-2] in ['radar', 'adv']))
async def wifi_radar_adv(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    tp_or_sms = cb_data[3]
    radar = cb_data[-1]
    if radar == 'pass':
        radar = cb_data[-2]
    try:
        await bot.send_message(cb.from_user.id,
                               'Организация услуги "WiFi радар":' if radar == 'radar' else 'Предоставление доступа к услугам рекламной платформы:',
                               reply_markup=wifi_radar_keyboard(kp, dep, serv, tp_or_sms, radar))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(
    lambda cb: cb.data.split('_')[-1].split('-')[-1] in wifi_radar_adv_names and cb.data.split('_')[-1].split('-')[
        -1] not in ['access', '12m', 'extended'])
async def wifi_radar_adv_lic(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    sms = cb_data[3]
    radar = cb_data[-1].split('-')[0]
    rad_dop = cb_data[-1].split('-')[1]
    try:
        await bot.send_message(cb.from_user.id, 'Выберите количество лицензий:',
                               reply_markup=wifi_radar_lic_keyboard(kp, dep, serv, sms, radar, rad_dop))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: cb.data.split('_')[-1] == 'wifi/pass')
async def wifi_dop_pass(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    try:
        print('pass')
        print(user_data)
        if len(user_data[cb.from_user.id]['main']) <= 2:
            len_for_grammar = len(user_data[cb.from_user.id]['main'])
            letter = '' if len_for_grammar == 2 else 'а'
            await bot.send_message(cb.from_user.id,
                                   'Вы можете сформировать коммерческое предложение или добавить еще {} тариф{} для сравнения!'.format(
                                       3 - len_for_grammar, letter),
                                   reply_markup=wg_fin_keyboard(kp, dep, serv))
        else:
            await bot.send_message(cb.from_user.id,
                                   f'Вы добавили 3 тарифа для сравнения!',
                                   reply_markup=wg_fin_keyboard_3())
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())


### iptv/hot


@dp.callback_query_handler(lambda cb: ((cb.data.split('_')[-1] in dep_to_name) and (cb.data.split('_')[0] == 'iptv/hot')) or (cb.data.split('_')[-1] == 'add-tar'))
async def ih_main_serv(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    try:
        await bot.send_message(cb.from_user.id, 'Выберите услугу \n(ОПТ - Основные Пакеты Телеканалов ):',
                                   reply_markup=iptv_hot_main_serv_keyboard(kp, dep))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[-1] in iptv_hot_main) or (cb.data.split('_')[-1] in iptv_hot_main_ch))
async def ih_main_ch(callback_query: types.callback_query, state):
    cb = callback_query
    print()
    print('cbdata:' + cb.data)
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    ch = cb_data[2]
    dop = cb_data[-1]
    if dop in iptv_hot_main:
        dop = 'main'
    elif dop in iptv_hot_main_ch_dop:
        print('in elif')
        user_data[cb.from_user.id]['main'].append(cb.data)
    else:
        print('BIG MISTAKE')

    try:
        await bot.send_message(cb.from_user.id,
                               'Основные пакеты телеканалов',
                               reply_markup=iptv_hot_main_dop_ch_keyboard(kp, dep, ch, dop, cb.from_user.id))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[0] == 'iptv/hot') and (len(cb.data.split('-')) == 2) and (cb.data.split('-')[0] not in iptv_hot_dop_ch_names) and (cb.data.split('_')[0] != 'iptvlast') and (cb.data.split('_')[-1] != 'add-tar') and (cb.data != 'watch-kp'))
async def in_dop_channel(callback_query: types.callback_query, state):
    cb = callback_query
    print(cb.data)
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    ch = cb_data[2]
    if cb_data[-1].split('-')[0] in iptv_hot_choices:
        user_data[cb.from_user.id]['main'][-1] += '_' + cb_data[-1]
    elif cb_data[-1].split('-')[0] in iptv_hot_main_ch:
        user_data[cb.from_user.id]['main'].append(cb.data)
    print('fin_d ', user_data)
    try:
        await bot.send_message(cb.from_user.id, 'Выберите дополнительные пакеты телеканалов или нажмите "Пропустить":',
                               reply_markup=iptv_hot_dop_keyboard(kp, dep, ch, 'dopchannel'))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('-')[0] in iptv_hot_dop_ch_names) and (cb.data.split('-')[0] != 'ihpass/dopchannel'))
async def ih_in_more_dop_channel(callback_query: types.callback_query, state):
    cb = callback_query
    user_data[cb.from_user.id]['main'][-1] += '_' + cb.data
    u_data = user_data[cb.from_user.id]['main'][-1]
    cb_data = u_data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    ch = cb_data[2]
    used_dops = [i.split('-')[0] for i in cb_data if i.split('-')[0] in iptv_hot_dop_ch_names]
    print('fin_d ', user_data)
    try:
        if len(used_dops) == 9:
            await bot.send_message(cb.from_user.id, 'Выберите количество информационных каналов или нажмите "Пропустить":',
                               reply_markup=iptv_hot_info_keyboard(kp, dep, ch, 'infochannel'))
        else:
            await bot.send_message(cb.from_user.id, 'Выберите еще пакеты телеканалов или нажмите "Пропустить":',
                               reply_markup=iptv_hot_dop_keyboard(kp, dep, ch, 'dopchannel', used_dops))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: cb.data.split('-')[0] == 'ihpass/dopchannel')
async def ih_in_infoch(callback_query: types.callback_query, state):
    cb = callback_query
    u_data = user_data[cb.from_user.id]['main'][-1]
    cb_data = u_data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    ch = cb_data[2]
    try:
        await bot.send_message(cb.from_user.id, 'Выберите количество информационных каналов или нажмите "Пропустить":',
                               reply_markup=iptv_hot_info_keyboard(kp, dep, ch, 'infochannel'))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: cb.data.split('_')[0] == 'iptvlast')
async def ih_last(callback_query: types.callback_query, state):
    cb = callback_query
    if cb.data.split('_')[1] != 'pass/infochannel-infochannel-fin':
        user_data[cb.from_user.id]['main'][-1] += '_' + cb.data.split('_')[1]
    else:
        pass
    u_data = user_data[cb.from_user.id]['main'][-1]
    cb_data = u_data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    print('finallll ', user_data)
    try:
        if len(user_data[cb.from_user.id]['main']) <= 2:
            len_for_grammar = len(user_data[cb.from_user.id]['main'])
            letter = '' if len_for_grammar == 2 else 'а'
            await bot.send_message(cb.from_user.id,
                                   'Вы можете сформировать коммерческое предложение или добавить еще {} тариф{} для сравнения!'.format(3-len_for_grammar, letter),
                                   reply_markup=iptv_hot_fin_keyboard(kp, dep))
        else:
            await bot.send_message(cb.from_user.id, f'Вы добавили 3 тарифа для сравнения!',
                                   reply_markup=iptv_hot_fin_keyboard_3())
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())


### vn


@dp.callback_query_handler(lambda cb: ((cb.data.split('_')[-1] in dep_to_name) and (cb.data.split('_')[0] == 'vn')) or (cb.data.split('_')[-1] == 'add-tar-vn'))
async def vn_service(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    try:
        await bot.send_message(cb.from_user.id, 'Выберите услугу:',
                                   reply_markup=vn_service_keyboard(kp, dep))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[-1] in vn_service_to_name) or (cb.data.split('_')[-1] == 'add-tar-vn'))
async def vn_tp(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    user_data[cb.from_user.id]['main'].append(cb.data)
    print('vn_tp', user_data)
    try:
        await bot.send_message(cb.from_user.id, 'Выберите тарифный план:',
                                   reply_markup=vn_tp_keyboard(kp, dep, serv))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[-1] in vn_tp_to_name))
async def vn_sutki(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    tp = cb_data[3]
    user_data[cb.from_user.id]['main'][-1] += '_' + cb_data[-1]
    print('vn_sutki', user_data)
    try:
        await bot.send_message(cb.from_user.id, 'Выберите количество суток хранения архива:',
                                   reply_markup=vn_sutki_keyboard(kp, dep, serv, tp))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[-1] in vn_sutki_to_name))
async def vn_save(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    tp = cb_data[3]
    sutki = cb_data[4]
    user_data[cb.from_user.id]['main'][-1] += '_' + cb_data[-1]
    print('vn_save', user_data)
    try:
        await bot.send_message(cb.from_user.id, 'Выберите вид записи:',
                                   reply_markup=vn_save_keyboard(kp, dep, serv, tp, sutki))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[-1] in vn_save_to_name))
async def vn_speed(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    tp = cb_data[3]
    sutki = cb_data[4]
    save = cb_data[5]
    user_data[cb.from_user.id]['main'][-1] += '_' + cb_data[-1]
    print('vn_speed', user_data)
    try:
        await bot.send_message(cb.from_user.id, 'Выберите трафик:',
                                   reply_markup=vn_speed_keyboard(kp, dep, serv, tp, sutki, save))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[0] == 'vn/dop'))
async def vn_dop(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    if cb_data[-1] != 'pass/dv':
        user_data[cb.from_user.id]['main'][-1] += '_' + cb_data[-1]
    u_data = user_data[cb.from_user.id]['main'][-1]
    cb_data = u_data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    tp = cb_data[3]
    used_dops = [i for i in cb_data if i in vn_big_dop_to_name]
    print('vn_dop', user_data)
    try:
        if used_dops == []:
            await bot.send_message(cb.from_user.id, 'Выберите дополнительные опции или нажмите "Пропустить":',
                                       reply_markup=vn_dop_keyboard(kp, dep, serv, tp))
        elif used_dops != []:
            await bot.send_message(cb.from_user.id, 'Выберите еще дополнительные опции или нажмите "Пропустить":',
                                       reply_markup=vn_dop_keyboard(kp, dep, serv, tp, used_dops))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[0] == 'vn/dop/more'))
async def vn_dop_more(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    user_data[cb.from_user.id]['main'][-1] += '_' + cb_data[-1]
    u_data = user_data[cb.from_user.id]['main'][-1]
    cb_data = u_data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    tp = cb_data[3]
    dop = cb.data.split('_')[-1]
    used_dops = [i for i in cb_data if i in vn_big_dop_to_name]
    print('vn_dop_more', user_data)
    try:
        if dop == 'smsPack':
            used_dops_vid = [i.split('-')[0] for i in cb_data if (i.split('-')[0] in vn_dops_to_name) and ('/' not in i)]
            await bot.send_message(cb.from_user.id, 'Выберите пакет SMS-уведомлений:',
                                       reply_markup=vn_dop_more_keyboard(kp, dep, serv, tp, dop, used_dops, used_dops_vid))
        else:
            used_dops_vid = [i.split('-')[0] for i in cb_data if (i.split('-')[0] in vn_dops_to_name) and ('/' not in i)]
            if len(used_dops_vid) == 0:
                await bot.send_message(cb.from_user.id, 'Выберите опцию Видеоаналитики:',
                                           reply_markup=vn_dop_more_keyboard(kp, dep, serv, tp, dop, used_dops, used_dops_vid))
            else:
                await bot.send_message(cb.from_user.id, 'Выберите еще опцию Видеоаналитики или нажмите "Пропустить":',
                                       reply_markup=vn_dop_more_keyboard(kp, dep, serv, tp, dop, used_dops,
                                                                         used_dops_vid))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[0] == 'vn/dop/disc'))
async def vn_dop_disc(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    # user_data[cb.from_user.id]['main'][-1] += '_' + cb_data[-1]
    u_data = user_data[cb.from_user.id]['main'][-1]
    cb_data = u_data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    tp = cb_data[3]
    dop = cb_data[-1]
    dop_more = cb.data.split('_')[-1]
    used_dops = [i for i in cb_data if i in vn_big_dop_to_name]
    used_dops_vid = [i.split('-')[0] for i in cb_data if (i.split('-')[0] in vn_dops_to_name) and ('/' not in i)]
    print('vn_dop_disc', user_data)
    print(dop, dop_more)
    try:
        await bot.send_message(cb.from_user.id, 'Выберите допустимый объём скидки:',
                                   reply_markup=vn_dop_disc_keyboard(kp, dep, serv, tp, dop, dop_more, used_dops, used_dops_vid))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[0] == 'vn/fin'))
async def vn_fin(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    if cb_data[-1] != 'pass' and cb_data[-1] != 'pass/dv':
        user_data[cb.from_user.id]['main'][-1] += '_' + cb_data[-1]
    u_data = user_data[cb.from_user.id]['main'][-1]
    cb_data = u_data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    print('finallll ', user_data)
    try:
        if len(user_data[cb.from_user.id]['main']) <= 2:
            len_for_grammar = len(user_data[cb.from_user.id]['main'])
            letter = '' if len_for_grammar == 2 else 'а'
            await bot.send_message(cb.from_user.id,
                                   'Вы можете сформировать коммерческое предложение или добавить еще {} тариф{} для сравнения!'.format(3-len_for_grammar, letter),
                                   reply_markup=vn_fin_keyboard(kp, dep))
        else:
            await bot.send_message(cb.from_user.id, f'Вы добавили 3 тарифа для сравнения!',
                                   reply_markup=vn_fin_keyboard_3())
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())


### wats functions


@dp.callback_query_handler(lambda cb: (cb.data.split('_')[-1] in dep_to_name) and (cb.data.split('_')[0] == 'wats'))
async def wats_big_tp(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    try:
        await bot.send_message(cb.from_user.id, 'Группа тарифных планов:',
                                   reply_markup=wats_big_tp_keyboard(kp, dep, cb.from_user.id))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[-1] in wats_big_tp_to_name) or (cb.data.split('_')[-1] == 'add-tar-wa'))
async def wats_in_tp(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    big_tp = cb_data[2]
    try:
        user_data[cb.from_user.id]['main'].append(cb.data.replace('_add-tar-wa', ''))
        text = 'из группы \n"' + wats_big_tp_to_name[big_tp] + '"'
        await bot.send_message(cb.from_user.id, f'Выберите тарифный план {text}:',
                                   reply_markup=wats_in_tp_keyboard(kp, dep, big_tp))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[-1] in wats_tp_to_name))
async def wats_in_number_or_dop(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    big_tp = cb_data[2]
    tp = cb_data[3]
    if tp in wats_tp_bus:
        dop = 'numbCat'
        try:
            user_data[cb.from_user.id]['main'][-1] += '_' + cb_data[-1]
            print(user_data)
            await bot.send_message(cb.from_user.id, 'Выберите категорию номера:',
                                   reply_markup=wats_num_cat_keyboard(kp, dep, big_tp, tp, dop))
        except Exception:
            user_data[cb.from_user.id] = {'main': []}
            used_service[cb.from_user.id] = []
            used_user_data[cb.from_user.id] = []
            print(traceback.format_exc())
            await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                                   reply_markup=kp_keyboard())
    else:
        dop = 'dop'
        try:
            user_data[cb.from_user.id]['main'][-1] += '_' + cb_data[-1]
            print(dop)
            print(user_data)
            await bot.send_message(cb.from_user.id, 'Выберите дополнительные услуги или нажмите Пропустить',
                                   reply_markup=wats_dop_keyboard(kp, dep, big_tp, tp, dop))
        except Exception:
            user_data[cb.from_user.id] = {'main': []}
            used_service[cb.from_user.id] = []
            used_user_data[cb.from_user.id] = []
            print(traceback.format_exc())
            await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                                   reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[-1] in wats_num_cat_to_name))
async def wats_in_speed(callback_query: types.callback_query, state):
    cb = callback_query
    user_data[cb.from_user.id]['main'][-1] += '_' + cb.data
    u_data = user_data[cb.from_user.id]['main'][-1]
    cb_data = u_data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    big_tp = cb_data[2]
    tp = cb_data[3]
    dop = 'speed'
    try:
        print(user_data)
        print('in колво польз')
        await bot.send_message(cb.from_user.id, 'Выберите количество пользователей:',
                               reply_markup=wats_num_users_keyboard(kp, dep, big_tp, tp, dop))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('-')[0] in wats_num_abon_to_name) or (cb.data.split('_')[0] in wats_num_abon_to_name))
async def wats_in_formula_or_dop(callback_query: types.callback_query, state):
    cb = callback_query
    try:
        if cb.data.split('-')[0] in wats_num_abon_to_name:
            user_data[cb.from_user.id]['main'][-1] += '_' + cb.data
            u_data = user_data[cb.from_user.id]['main'][-1]
            cb_data = u_data.split('_')
            kp = cb_data[0]
            dep = cb_data[1]
            big_tp = cb_data[2]
            tp = cb_data[3]
            dop = 'dop'
            await bot.send_message(cb.from_user.id, 'Выберите дополнительные услуги или нажмите Пропустить',
                    reply_markup=wats_dop_keyboard(kp, dep, big_tp, tp, dop))
        elif cb.data.split('_')[0] in wats_num_abon_to_name:
            user_data[cb.from_user.id]['main'][-1] += '_' + cb.data.split('_')[0]
            await Mydialog.otvet.set()
            await bot.send_message(cb.from_user.id, f'Введите стоимость АП (без пробелов), посчитав по формуле, где n-кол-во пользователей \n{cb.data.split("_")[1]}')
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.message_handler(state=Mydialog.otvet)
async def wats_price_input(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['text'] = message.text
            user_message = data['text']
            user_data[message.from_user.id]['main'][-1] += '-' + user_message
            u_data = user_data[message.from_user.id]['main'][-1]
            cb_data = u_data.split('_')
            kp = cb_data[0]
            dep = cb_data[1]
            big_tp = cb_data[2]
            tp = cb_data[3]
            dop = 'dop'
            await bot.send_message(message.from_user.id, 'Выберите дополнительные услуги или нажмите Пропустить',
                                   reply_markup=wats_dop_keyboard(kp, dep, big_tp, tp, dop))
        await state.finish()
    except Exception:
        user_data[message.from_user.id] = {'main': []}
        print(traceback.format_exc())
        await bot.send_message(message.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: cb.data in wats_dop_to_name or cb.data.split('-')[0] in wats_dop_to_name or cb.data == 'pass/wats')
async def wats_after_dop(callback_query: types.callback_query, state):
    cb = callback_query
    print(cb.data)
    if cb.data != 'pass/wats':
        user_data[cb.from_user.id]['main'][-1] += '_' + cb.data
    else:
        pass
    u_data = user_data[cb.from_user.id]['main'][-1]
    cb_data = u_data.split('_')
    used_dops = [i for i in cb_data if i in wats_dop_to_name]
    kp = cb_data[0]
    dep = cb_data[1]
    big_tp = cb_data[2]
    tp = cb_data[3]
    dop = 'dop'
    print('fin')
    print(user_data)
    try:
        if len(used_dops) == 4 and big_tp == 'busyness/virt' and cb.data != 'pass/wats':
            if len(user_data[cb.from_user.id]['main']) <= 2:
                len_for_grammar = len(user_data[cb.from_user.id]['main'])
                letter = '' if len_for_grammar == 2 else 'а'
                await bot.send_message(cb.from_user.id,
                                       'Вы можете сформировать коммерческое предложение или добавить еще {} тариф{} для сравнения!'.format(3-len_for_grammar, letter),
                                       reply_markup=wats_fin_keyboard(kp, dep, big_tp))
            else:
                await bot.send_message(cb.from_user.id, f'Вы добавили 3 тарифа для сравнения!',
                                       reply_markup=wats_fin_keyboard_3())
        elif len(used_dops) == 8 and big_tp == 'pack/min' and cb.data != 'pass/wats':
            if len(user_data[cb.from_user.id]['main']) <= 2:
                len_for_grammar = len(user_data[cb.from_user.id]['main'])
                letter = '' if len_for_grammar == 2 else 'а'
                await bot.send_message(cb.from_user.id,
                                       'Вы можете сформировать коммерческое предложение или добавить еще {} тариф{} для сравнения!'.format(3-len_for_grammar, letter),
                                       reply_markup=wats_fin_keyboard(kp, dep, big_tp))
            else:
                await bot.send_message(cb.from_user.id, f'Вы добавили 3 тарифа для сравнения!',
                                       reply_markup=wats_fin_keyboard_3())
        elif cb.data == 'pass/wats':
            if len(user_data[cb.from_user.id]['main']) <= 2:
                len_for_grammar = len(user_data[cb.from_user.id]['main'])
                letter = '' if len_for_grammar == 2 else 'а'
                await bot.send_message(cb.from_user.id,
                                       'Вы можете сформировать коммерческое предложение или добавить еще {} тариф{} для сравнения!'.format(3-len_for_grammar, letter),
                                       reply_markup=wats_fin_keyboard(kp, dep, big_tp))
            else:
                await bot.send_message(cb.from_user.id, f'Вы добавили 3 тарифа для сравнения!',
                                       reply_markup=wats_fin_keyboard_3())
        else:
            await bot.send_message(cb.from_user.id, 'Выберите еще дополнительные услуги или нажмите Пропустить:',
                               reply_markup=wats_dop_keyboard(kp, dep, big_tp, tp, dop, used_dops))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

### IPTV functions

@dp.callback_query_handler(lambda cb: ((cb.data.split('_')[-1] in dep_to_name) and (cb.data.split('_')[0] == 'iptv')) or (cb.data.split('_')[-1] == 'add-tar-ip'))
async def ip_service(callback_query: types.callback_query, state):
    cb = callback_query
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    try:
        await bot.send_message(cb.from_user.id, 'Выберите опцию:',
                                   reply_markup=ip_service_keyboard(kp, dep))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: cb.data.split('_')[-1] in ip_service_names)
async def ip_main_cut_ch(callback_query: types.callback_query, state):
    cb = callback_query
    print(cb.data)
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    try:
        iptxt = 'публичного показа:' if serv == 'public' else 'непубличного показа:'
        await bot.send_message(cb.from_user.id,
                               f'Выберите группу пакетов для {iptxt}',
                               reply_markup=ip_main_ch_cut_keyboard(kp, dep, serv))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: cb.data.split('_')[-1] in ip_main_ch_cut_names)
async def ip_main_ch(callback_query: types.callback_query, state):
    cb = callback_query
    print(cb.data)
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    cut = cb_data[3]
    try:
        iptxt = 'публичного показа:' if serv == 'public' else 'непубличного показа:'
        await bot.send_message(cb.from_user.id,
                               f'Выберите пакет основных телеканалов для {iptxt}',
                               reply_markup=ip_main_ch_keyboard(kp, dep, serv, cut))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[0] == 'iptv') and (cb.data.split('_')[-1] in ['dopchannel', 'dopchannel-fin']) and (cb.data.split('_')[-2] != 'smart') and (cb.data.split('_')[-2] != 'pass/dopchannel'))
async def ip_dop_ch(callback_query: types.callback_query, state):
    cb = callback_query
    print(cb.data)
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    channel = cb_data[3]
    if channel in ip_main_ch_names:
        price = str(data[kp][dep][serv]['kostyl'][channel]) # из-за логики формирования тарифа в iptv сделал костыль
        try:
            print('add_tar udata')
            print(user_data)
            print(len(user_data[cb.from_user.id]['main']))
            user_data[cb.from_user.id]['main'].append(str(cb.data+'-'+price).replace('_dopchannel', ''))
        except:
            user_data[cb.from_user.id] = {'main': [str(cb.data+'-'+price).replace('_dopchannel', '')]}
    else:
        try:
            price = '-' + str(data[kp][dep][serv]['dopchannel'][channel])
        except:
            price=''
        if cb.data.split('_')[-2] != 'pass/dopchannel':
            user_data[cb.from_user.id]['main'][-1] = user_data[cb.from_user.id]['main'][-1] + '_' + channel + price
    print(user_data)
    try:
        if cb.data.split('_')[-1] == 'dopchannel-fin':
            print('aa финал в допе')
            print('dop_CH_348!')
            await bot.send_message(cb.from_user.id,
                                   'Выберите дополнительные услуги или нажмите пропустить:',
                                   reply_markup=ip_dop_keyboard(kp, dep, serv, 'dop'))
        elif channel in ip_main_ch_names and cb.data.split('_')[-1] != 'dopchannel_fin':
            iptxt = 'публичного показа:' if serv == 'public' else 'непубличного показа:'
            await bot.send_message(cb.from_user.id,
                                   f'Выберите пакет дополнительных телеканалов для {iptxt}',
                                   reply_markup=ip_dop_ch_keyboard(kp, dep, serv))
        else:
            await bot.send_message(cb.from_user.id,
                                   'Вы можете добавить следующие пакеты дополнительных телеканалов:',
                                   reply_markup=ip_dop_ch_keyboard(kp, dep, serv, channel, user_data[cb.from_user.id]['main'][-1]))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[0] == 'iptv') and (cb.data.split('_')[-2] == 'smart'))
async def ip_smart(callback_query: types.callback_query, state):
    cb = callback_query
    print(cb.data)
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    try:
        await bot.send_message(cb.from_user.id, 'Выберите пакет SMART TV:', reply_markup=ip_smart_keyboard(kp, dep, serv, user_data[cb.from_user.id]['main'][-1]))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[0] == 'iptv') and (cb.data.split('_')[-2] == 'pass/dopchannel' or (cb.data.split('_')[-1] == 'dopchannel_fin' and cb.data.split('_')[-2] != 'smart')))
async def ip_dop(callback_query: types.callback_query, state):
    print('ЗАШЕЛВ  ДОМП!')
    print('ПЕРВЫЙ ДОП КИБОРГ')
    print(user_data)
    cb = callback_query
    cb_data = cb.data.split('_')
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print(cb.data)
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    dop_type = 'dop'
    print(f'in dop {cb_data}')
    try:
        # user_data[cb.from_user.id] = {'main': [str(cb.data).replace('_dop', '')]}
        print('dop399!')
        await bot.send_message(cb.from_user.id, 'Выберите дополнительные услуги или нажмите "Пропустить"',
                               reply_markup=ip_dop_keyboard(kp, dep, serv, dop_type))
        print(user_data)
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: cb.data.split('_')[-1] == 'videomuz')
async def ip_videomuz(callback_query: types.callback_query, state):
    cb = callback_query
    print(cb.data)
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    print(user_data)
    try:
        await bot.send_message(cb.from_user.id, 'Выберите категорию:', reply_markup=ip_prokat_keyboard(kp, dep, serv))
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[0] == 'iptv') and ((cb.data.split('_')[-1] in ip_dop_names) and (cb.data.split('_')[-1] != 'pass') or (all(x in cb.data.split('_')[-1] for x in ['videomuz', '-']))))
async def ip_dop_more(callback_query: types.callback_query, state):
    cb = callback_query
    print('last radar')
    print(cb.data)
    cb_data = cb.data.split('_')
    kp = cb_data[0]
    dep = cb_data[1]
    serv = cb_data[2]
    sms = cb_data[3]
    dop = cb_data[4]
    print(f'in dop more{cb_data}')
    try:
        if len(user_data[cb.from_user.id]['main'][-1]) == 0:
            user_data[cb.from_user.id]['main'][-1] = user_data[cb.from_user.id]['main'][-1] + cb.data
        else:
            user_data[cb.from_user.id]['main'][-1] = user_data[cb.from_user.id]['main'][-1] + '_' + dop
        print(user_data)
        if not all(x in [j.split('-')[0] for j in user_data[cb.from_user.id]['main'][-1].split('_')[-4:]] for x in list(data[kp][dep][serv]['dop'].keys())[:-1]):
            print('user_data to ip_dop_keyboard!!!!!!!')
            print(user_data)
            await bot.send_message(cb.from_user.id, 'Выберите еще дополнительные услуги или нажмите "Пропустить"',
                                   reply_markup=ip_dop_keyboard(kp, dep, serv, sms, dop, user_data[cb.from_user.id]['main'][-1]))
        else:
            if len(user_data[cb.from_user.id]['main']) <= 2:
                print('LENNNNNNNNNNN')
                print(len(user_data[cb.from_user.id]['main']))
                print(user_data[cb.from_user.id]['main'])
                len_for_grammar = len(user_data[cb.from_user.id]['main'])
                letter = '' if len_for_grammar == 2 else 'а'
                await bot.send_message(cb.from_user.id,
                                       'Вы можете сформировать коммерческое предложение или добавить еще {} тариф{} для сравнения!'.format(
                                           3 - len_for_grammar, letter),
                                       reply_markup=ip_fin_keyboard(kp, dep))
                print('МЕНЬШЕ 3 ИДЕТ ДАЛЬШЕ')
                print(user_data)
            else:
                await bot.send_message(cb.from_user.id,
                                       f'Вы добавили 3 тарифа для сравнения!',
                                       reply_markup=ip_fin_keyboard_3())
                print('ЕСТЬ 3 ТАРИФА')
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: (cb.data.split('_')[0] == 'iptv') and ((cb.data.split('_')[-1] == 'pass' and cb.data.split('_')[-2] =='pass') or cb.data.split('_')[-1] == 'pass'))
async def iptv_fin_keyboard(callback_query: types.callback_query, state):
    cb = callback_query
    kp = cb.data.split('_')[0]
    dep = cb.data.split('_')[1]
    serv = cb.data.split('_')[2]
    print('fin_ud')
    print(user_data)
    try:
        try:
            if cb.data.split('_')[-2] not in user_data[cb.from_user.id]['main'][-1].split('_') and cb.data.split('_')[-2] in ip_dop_names and len(user_data[cb.from_user.id]['main'][-1].split('_')) == 6 and cb.data.split('_')[-2] != 'pass':
                user_data[cb.from_user.id]['main'][-1] = user_data[cb.from_user.id]['main'][-1] + '_' +cb.data.split('_')[-2]
            elif len(user_data[cb.from_user.id]['main'][-1]) == 0:
                user_data[cb.from_user.id]['main'][-1] = user_data[cb.from_user.id]['main'][-1] + cb.data
        except:
            pass

        if len(user_data[cb.from_user.id]['main']) <= 2:
            len_for_grammar = len(user_data[cb.from_user.id]['main'])
            letter = '' if len_for_grammar == 2 else 'а'
            await bot.send_message(cb.from_user.id,
                                   'Вы можете сформировать коммерческое предложение или добавить еще {} тариф{} для сравнения!'.format(3-len_for_grammar, letter),
                                   reply_markup=ip_fin_keyboard(kp, dep))
        else:
            await bot.send_message(cb.from_user.id, 'Вы добавили 3 тарифа для сравнения!',
                                   reply_markup=ip_fin_keyboard_3())

    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())



### create kp



@dp.callback_query_handler(lambda cb: (cb.data == 'create-kp'))
async def create_kp(callback_query: types.callback_query, state):
    cb = callback_query
    print(user_data)
    print('in   kp')

    if not any(i == user_data[cb.from_user.id]['main'] for i in used_user_data) and user_data[cb.from_user.id]['main'] != []:
        try:
            if 'wifi' in user_data[cb.from_user.id]['main'][0]:
                used_service[cb.from_user.id].append(
                    'wifi/guest' if 'guest' in user_data[cb.from_user.id]['main'][0] else 'wifi/control')
                used_user_data[cb.from_user.id].append(user_data[cb.from_user.id]['main'])
            elif 'wats' in user_data[cb.from_user.id]['main'][0]:
                used_service[cb.from_user.id].append(
                    'wats/busy' if 'busyness/virt' in user_data[cb.from_user.id]['main'][0] else 'wats/packmin')
                used_user_data[cb.from_user.id].append(user_data[cb.from_user.id]['main'])
            else:
                used_service[cb.from_user.id].append(user_data[cb.from_user.id]['main'][0].split('_')[0])
                used_user_data[cb.from_user.id].append(user_data[cb.from_user.id]['main'])

        except:
            if 'wifi' in user_data[cb.from_user.id]['main'][0]:
                used_service[cb.from_user.id] = [
                    'wifi/guest' if 'guest' in user_data[cb.from_user.id]['main'][0] else 'wifi/control']
                used_user_data[cb.from_user.id] = [user_data[cb.from_user.id]['main']]
            elif 'wats' in user_data[cb.from_user.id]['main'][0]:
                used_service[cb.from_user.id] = [
                    'wats/busy' if 'busyness/virt' in user_data[cb.from_user.id]['main'][0] else 'wats/packmin']
                used_user_data[cb.from_user.id] = [user_data[cb.from_user.id]['main']]
            else:
                used_service[cb.from_user.id] = [user_data[cb.from_user.id]['main'][0].split('_')[0]]
                used_user_data[cb.from_user.id] = [user_data[cb.from_user.id]['main']]

    print(used_user_data)
    print(used_service)
    try:
        used_service[cb.from_user.id].append('info')
        used_user_data[cb.from_user.id].append([])
                # a[353443196][-1].append('-10')
        await bot.send_message(cb.from_user.id, 'Введите адрес предоставления услуги!')
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.message_handler(lambda message: get_current_state(used_user_data, message.chat.id) + 1 == States.cl_addr.value)
async def name_input(message, state):
    try:
        await bot.send_message(message.chat.id, "Введите имя клиента!")
        used_user_data[message.chat.id][-1].append(message.text)
    except Exception:
        user_data[message.chat.id] = {'main': []}
        used_service[message.chat.id] = []
        used_user_data[message.chat.id] = []
        print(traceback.format_exc())
        await state.finish()
        await bot.send_message(message.chat.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.message_handler(lambda message: get_current_state(used_user_data, message.chat.id) + 1 == States.cl_name.value)
async def name_input(message, state):
    try:
        await bot.send_message(message.chat.id, "Введите Ваше имя!")
        used_user_data[message.chat.id][-1].append(message.text)
    except Exception:
        user_data[message.chat.id] = {'main': []}
        used_service[message.chat.id] = []
        used_user_data[message.chat.id] = []
        print(traceback.format_exc())
        await state.finish()
        await bot.send_message(message.chat.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.message_handler(lambda message: get_current_state(used_user_data, message.chat.id) + 1 == States.manager_name.value)
async def put_registration_number(message, state):
    try:
        await bot.send_message(message.chat.id, "Введите Ваш телефон!")
        used_user_data[message.chat.id][-1].append(message.text)
    except Exception:
        user_data[message.chat.id] = {'main': []}
        used_service[message.chat.id] = []
        used_user_data[message.chat.id] = []
        print(traceback.format_exc())
        await state.finish()
        await bot.send_message(message.chat.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.message_handler(lambda message: get_current_state(used_user_data, message.chat.id) + 1 == States.phn_num.value)
async def put_registration_number(message, state):
    try:
        used_user_data[message.chat.id][-1].append(message.text)
        await bot.send_message(message.chat.id, 'Введите стоимость инсталляционных услуг (вы можете отправить боту сообщение со стоимостью или нажать "Пропустить!")', reply_markup=only_skip(f'{message.chat.id}_fst'))
    except Exception:
        user_data[message.chat.id] = {'main': []}
        used_service[message.chat.id] = []
        used_user_data[message.chat.id] = []
        print(traceback.format_exc())
        await state.finish()
        await bot.send_message(message.chat.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.message_handler(lambda message: get_current_state(used_user_data, message.chat.id) + 1 == States.install_proc.value)
async def put_registration_number(message, state):
    try:
        used_user_data[message.chat.id][-1].append(message.text)
        await bot.send_message(message.chat.id, 'Введите стоимость оборудования (вы можете отправить боту сообщение со стоимостью или нажать "Пропустить!")', reply_markup=only_skip(f'{message.chat.id}_sec'))
    except Exception:
        user_data[message.chat.id] = {'main': []}
        used_service[message.chat.id] = []
        used_user_data[message.chat.id] = []
        print(traceback.format_exc())
        await state.finish()
        await bot.send_message(message.chat.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())


@dp.message_handler(lambda message: get_current_state(used_user_data, message.chat.id) + 1 == States.install_hard.value)
async def put_registration_number(message, state):
    used_user_data[message.chat.id][-1].append(message.text)
    try:
        uid = message.chat.id
        await bot.send_message(uid,
                               f'Все готово! Формируется КП! \nВы добавили {len(used_service[uid])-1} услуг. Примерное время создания файла {int(len(used_service[uid])-1) * 7 + 10} секунд. Пожалуйста, подождите...')
        print(f'pass to KP data= {used_user_data[uid]}')
        print(f'pass to KP order= {used_service[uid]}')
        await create_pdf(uid, used_user_data[uid], used_service[uid])

        all_files_user = list(Path(pdf_dir).rglob(f'{uid}*'))
        pdf_files = [str(i) for i in all_files_user if '.pdf' in str(i)]
        merger = PdfFileMerger()

        for pdf in pdf_files:
            merger.append(pdf)

        merger.write(f"{curdir}/{uid}_kp_new.pdf")
        merger.close()

        file = open(f"{curdir}/{uid}_kp_new.pdf", "rb")
        await bot.send_document(uid, document=file)
        await bot.send_message(uid, 'КП сформировано!', reply_markup=after_kp())
        user_data[uid] = {'main': []}
        used_service[uid] = []
        used_user_data[uid] = []
        await rm_pdf_doc(uid, all_files_user)

    except Exception:
        user_data[message.chat.id] = {'main': []}
        used_service[message.chat.id] = []
        used_user_data[message.chat.id] = []
        print(traceback.format_exc())
        await state.finish()
        await bot.send_message(message.chat.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: cb.data.split('_')[0] == 'Пропустить!')
async def withskipvalue(callback_query: types.callback_query, state):
    cb = callback_query
    uid = cb.from_user.id
    try:
        if cb.data.split('_')[2] == 'fst':
            used_user_data[uid][-1].append('Пропустить')
            await bot.send_message(uid, 'Введите стоимость оборудования (вы можете отправить боту сообщение со стоимостью или нажать "Пропустить!")', reply_markup=only_skip(f'{uid}_sec'))
        elif cb.data.split('_')[2] == 'sec':
            used_user_data[uid][-1].append('Пропустить')
            await bot.send_message(uid, f'Все готово! Формируется КП! \nВы добавили {len(used_service[uid])-1} услуг. Примерное время создания файла {int(len(used_service[uid])-1) * 7 + 10} секунд. Пожалуйста, подождите...')
            print(f'pass to KP data= {used_user_data[uid]}')
            print(f'pass to KP order= {used_service[uid]}')
            await create_pdf(uid, used_user_data[uid], used_service[uid])

            all_files_user = list(Path(pdf_dir).rglob(f'{uid}*'))
            pdf_files = [str(i) for i in all_files_user if '.pdf' in str(i)]
            merger = PdfFileMerger()

            for pdf in pdf_files:
                merger.append(pdf)

            merger.write(f"{curdir}/{uid}_kp_new.pdf")
            merger.close()

            file = open(f"{curdir}/{uid}_kp_new.pdf", "rb")
            await bot.send_document(uid, document=file)
            await bot.send_message(uid, 'КП сформировано!', reply_markup=after_kp())
            user_data[uid] = {'main': []}
            used_service[uid] = []
            used_user_data[uid] = []
            await rm_pdf_doc(uid, all_files_user)

    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: cb.data == '1-kptest')
async def kptest(callback_query: types.callback_query, state):
    cb = callback_query
    uid = cb.from_user.id
    try:
        await bot.send_message(uid, f'Все готово! Формируется КП! \nВы добавили {len(us_order[uid])-1} услуг. Примерное время создания файла {int(len(us_order[uid])-1) * 7 + 10} секунд. Пожалуйста, подождите...')
        print(f'pass to KP data= {us_l[uid]}')
        print(f'pass to KP order= {us_order[uid]}')
        await create_pdf(uid, us_l[uid], us_order[uid])

        all_files_user = list(Path(pdf_dir).rglob('353443196*'))
        pdf_files = [str(i) for i in all_files_user if '.pdf' in str(i)]
        print(pdf_files)
        merger = PdfFileMerger()

        for pdf in pdf_files:
            merger.append(pdf)

        merger.write(f"{curdir}/{uid}_kp_new.pdf")
        merger.close()

        file = open(f"{curdir}/{uid}_kp_new.pdf", "rb")
        await bot.send_document(uid, document=file)
        await bot.send_message(uid, 'КП сформировано!', reply_markup=after_kp())
        user_data[uid] = {'main': []}
        await rm_pdf_doc(uid, all_files_user)

    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())



### bot_functions


@dp.callback_query_handler(lambda cb: cb.data == 'watch-kp')
async def show(callback_query: types.CallbackQuery, state):
    cb = callback_query
    try:
        used_elements = '' if cb.from_user.id not in used_service.keys() else \
            ['*' + str(show_used_to_name[i]) + '*' for i in used_service[cb.from_user.id]]
        msg_txt = 'Вы пока не добавили услуг в коммерческое предложение' if used_elements == '' else 'Вы добавили следующие услуги:' + "\n" + "\n".join(
            used_elements) + '\n' + "(для продолжения воспользуйтесь клавиатурой сверху)"
        print(user_data)
        print(used_user_data)
        print(used_service)
        await bot.send_message(cb.from_user.id, text=msg_txt, parse_mode='Markdown')
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())


@dp.callback_query_handler(lambda cb: cb.data == 'to_begin')
async def beginning(callback_query: types.CallbackQuery, state):
    cb = callback_query
    try:
        await bot.send_message(cb.from_user.id, 'Начнем заново! Выберите филиал:',
                               reply_markup=kp_keyboard())
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())

@dp.callback_query_handler(lambda cb: cb.data == 'watch-all')
async def watch_all(callback_query: types.CallbackQuery, state):
    cb = callback_query
    try:
        await bot.send_message(cb.from_user.id, f'Двнные для формирования КП:\n\n{used_user_data[cb.from_user.id]}\n')
    except Exception:
        user_data[cb.from_user.id] = {'main': []}
        used_service[cb.from_user.id] = []
        used_user_data[cb.from_user.id] = []
        print(traceback.format_exc())
        await bot.send_message(cb.from_user.id, 'Что-то пошло не так, возврат в меню.',
                               reply_markup=kp_keyboard())



@dp.message_handler(commands=['help'], state='*')
async def help(message: types.Message, state):
    await state.finish()
    print(f'msg chat id: {message.chat.id}')
    try:
        txtxtxt = '*Как рабоатать с ботом?* \n \nПри *первом* нажатии */start* появится меню из 5 кнопок. Это услуги, с которыми возможно' \
                  ' создание коммерческого предложения. Выберите необходимую услугу и нажмите на нее. \n\n' \
                  'Появится меню с возможными филиалами для формирования услуги. Выбираете нужный, нажимаете кнопку, -' \
                  ' достаточно простой алгоритм.\n\n' \
                  'Так-же кнопка */start* может служить для перезапуска бота с удалением текущего прогресса формирования КП! \n\n' \
                  '*Важно*: \n' \
                  '  - всегда читайте текст над появляющимся меню!;\n' \
                  '  - старайтесь использовать только последнее появившееся меню!' \
                  ' использование более старых меню может привести к нарушению порядка работы алгоритма и к ошибкам;\n' \
                  '  - не спешите! если ответ на нажатие кнопки появляется не сразу - скорее всего, это из-за проблем с сетью;\n' \
                  '  - не нажимайте одну и ту-же кнопку несколько раз подряд! (см. пункт выше);\n' \
                  '  - если выбор сделан неверно, вы можете нажать */start* из кнопки *меню* слева от поля ввода. \n\n' \
                  '*Это всё!* \nРекомендую перед работой проверить бот в тестовом режиме!\nПри возникновении ошибок, пишите *@pnknw*'
        await bot.send_message(message.chat.id, txtxtxt,
                               parse_mode='Markdown')
        # user_data[message.chat.id] = {'main': []}
        # used_service[message.chat.id] = []
        # used_user_data[message.chat.id] = []
    except Exception:
        print(traceback.format_exc())

@dp.callback_query_handler(lambda cb: cb.data == 'helpme')
async def help(callback_query: types.CallbackQuery):
    cb = callback_query
    print(f'msg chat id: {cb.from_user.id}')
    try:
        txtxtxt = '*Как рабоатать с ботом?* \n \nПри *первом* нажатии /start появится меню из 5 кнопок. Это услуги, с которыми возможно' \
                  ' создание коммерческого предложения. Выберите необходимую услугу и нажмите на нее. \n\n' \
                  'Появится меню с возможными филиалами для формирования услуги. Выбираете нужный, нажимаете кнопку, -' \
                  ' достаточно простой алгоритм.\n\n' \
                  'Так-же кнопка */start* может служить для перезапуска бота с удалением текущего прогресса формирования КП! \n\n' \
                  '*Важно*: \n' \
                  '  - всегда читайте текст над появляющимся меню!;\n' \
                  '  - старайтесь использовать только последнее появившееся меню!' \
                  ' использование более старых меню может привести к нарушению порядка работы алгоритма и к ошибкам;\n' \
                  '  - не спешите! если ответ на нажатие кнопки появляется не сразу - скорее всего, это из-за проблем с сетью;\n' \
                  '  - не нажимайте одну и ту-же кнопку несколько раз подряд! (см. пункт выше);\n' \
                  '  - если выбор сделан неверно, вы можете нажать /start из кнопки "меню" слева от поля ввода. \n\n' \
                  '*Это всё!* \nРекомендую перед работой проверить бот в тестовом режиме!\nПри возникновении ошибок, пишите *@pnknw*\n' \
                  '/start'
        await bot.send_message(cb.from_user.id, txtxtxt,
                               parse_mode='Markdown')
        # user_data[message.chat.id] = {'main': []}
        # used_service[message.chat.id] = []
        # used_user_data[message.chat.id] = []
    except Exception:
        print(traceback.format_exc())

### run

if __name__ == '__main__':
    print('')
    print('БОТ РАБОТАЕТ!')
    print('')
    print('ЧТОБЫ ОСТАНОВИТЬ БОТ, НАЖМИТЕ КОМБИНАЦИЮ КЛАВИШ CTRL + C')
    print('')
    executor.start_polling(dp, skip_updates=False)
