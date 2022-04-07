import os
from aenum import Enum
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from pathlib import Path
from PyPDF2 import PdfFileMerger


curdir = os.getcwd()

pdf_dir = Path.cwd() / 'main_pdf/pdf_temp'

user_data = {}

used_service = {}

used_user_data = {}

def flatten(seq):
    l = []
    for elt in seq:
        t = type(elt)
        if t is tuple or t is list:
            for elt2 in flatten(elt):
                l.append(elt2)
        else:
            l.append(elt)
    return l

def get_current_state(udata, uid):
    try:
        return len(udata[uid][-1])
    except:
        print('message not accepted')
        return 6

def only_skip(uid):
    keyboard_markup = types.InlineKeyboardMarkup(resize=True)
    keyboard_markup.insert(types.InlineKeyboardButton(text='Пропустить!', callback_data=f'Пропустить!_{uid}'))
    return keyboard_markup

class States(Enum):
    cl_addr = 1
    cl_name = 2
    manager_name = 3
    phn_num = 4
    install_proc = 5
    install_hard = 6

# for wats formula price input
class Mydialog(StatesGroup):
    otvet = State()

async def rm_pdf_doc(uid, fs):
    for i in fs:
        Path.unlink(i)
    os.remove(f'{uid}_kp_new.pdf')
    print('remove pdfs')

def tostr_(lis):
    P = -3
    C = ' '
    lis.insert(P, C)
    ret = ''
    for i in lis:
        ret += i
    return ret