import db
from aiogram import Bot, Dispatcher, executor, types

TOKEN = '1781065351:AAE9OVbzdE8anMXWQIoDw3Cu7TA-kl1nDws'
row_num = 10

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(
                        "Привет!\n"
                        "Здесь ты можешь посмотреть подродную информацию о университетах Казахстана\n"
                        "Все университеты:     /all\n")


@dp.message_handler(lambda message: message.text.startswith('/all'))
async def del_expense(message: types.Message):
    global row_num
    result = db.select_all()
    toUser = ''
    print(result)
    for i in range(row_num-10, row_num):
        toUser += result[i][0]+f" /{result[i][1]} \n"
    row_num += 10
    await message.answer(toUser)


@dp.message_handler(lambda message: message.text.startswith('/next'))
async def del_expense(message: types.Message):
    global row_num
    result = db.select_all()
    toUser = ''
    print(result)
    for i in range(row_num-10, min(row_num, 112)):
        toUser += result[i][0]+f" /{result[i][1]} \n"
    row_num += 10
    if row_num > 112:
        row_num = 10
    await message.answer(toUser)


@dp.message_handler(lambda message: message.text.find('@') != -1)
async def del_expense(message: types.Message):
    result = db.select(message.text[1:])
    num = 1
    faculty = result[10]
    print(faculty)
    faculty_to_user = ''
    for i in faculty:
        faculty_to_user += str(num) + ') '+i[0]+'\n'
        num += 1
    toUser = f'Название: {result[1]}\n' \
             f'Адрес: {result[2]}\n' \
             f'Официальная страница: {result[3]}\n' \
             f'Электронная почта: {result[0]}\n' \
             f'Номер для связи: {result[4]}\n' \
             f'Вид: {result[5]}\n' \
             f'Озлата: {result[6]}\n' \
             f'Направление: {result[7]}\n' \
             f'Общежитие: {"Есть" if result[8] == 1 else "Нет"}\n' \
             f'Имя университета: {"Есть" if result[9] == 1 else "Нет"}\n' \
             f'Факультеты:\n{faculty_to_user}'
    await message.answer(toUser)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
