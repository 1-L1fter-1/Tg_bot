#pip --version
#py --version
#pip install aiogram
#py -m pip install aiogram - если не работает pip
#pip install aiogram --force-reinstall
#(личная пометка для удоления для запуска проги) python "c:/Users/User/OneDrive/Рабочий стол/Tg_bot/Bot_MARVI_Base_Cod/Bot_.py"

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.client.default import DefaultBotProperties
import asyncio

# Токен бота 
API_TOKEN = '8014549050:AAGr5RLubBVqyvLlx5Nl6ZmnE9qcABm7dBc'

# Инициализируем бота
bot = Bot(token='8014549050:AAGr5RLubBVqyvLlx5Nl6ZmnE9qcABm7dBc', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Главное меню бота
def get_main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Лекции", callback_data="lectures")]
        ]
    )

# Меню лекций
def get_lectures_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Выбрать лекцию", callback_data="select_lecture")],
            [InlineKeyboardButton(text="Все лекции", callback_data="all_lectures")],
            [InlineKeyboardButton(text="Назад", callback_data="back_to_main")]
        ]
    )

# Обработчик команды /start
@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Я бот Marvi, созданный помогать компании Глобус в обучении стажеров. "
        "Чтобы начать, нажмите /menu",
        reply_markup=get_main_menu() 
    )

# Обработчик команды /menu
@dp.message(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer(
        "Главное меню: Пожалуйста, выберите что вы хотели бы сделать?",
        reply_markup=get_main_menu()
    )

# Обработчик кнопки Лекции
@dp.callback_query(lambda c: c.data == 'lectures')
async def handle_lectures(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Меню лекций: что вы желаете сделать?",
        reply_markup=get_lectures_menu()
    )
    await callback.answer()

# Обработчик кнопки Назад
@dp.callback_query(lambda c: c.data == 'back_to_main')
async def handle_back(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Главное меню:",
        reply_markup=get_main_menu()
    )
    await callback.answer()

#  (заглушки)
@dp.callback_query(lambda c: c.data == 'select_lecture')
async def handle_select_lecture(callback: types.CallbackQuery):
    await callback.answer("Функция выбора лекции в разработке", show_alert=True)

@dp.callback_query(lambda c: c.data == 'all_lectures')
async def handle_all_lectures(callback: types.CallbackQuery):
    await callback.answer("Функция просмотра всех лекций в разработке", show_alert=True)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())