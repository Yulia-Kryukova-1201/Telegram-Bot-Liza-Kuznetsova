import asyncio
import aiogram
import random
from aiogram import types
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message,FSInputFile,InputFile,URLInputFile,BufferedInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

bot = Bot(token='7919511150:AAGm0_D71jCR-Yb7z-zRpfUT0Kw7G9YwVV0')
storage = MemoryStorage()
dp = Dispatcher()
router = Router()

images_path = "images/formulka.jpg"


newWords = ['Демпинг - искусственное заниженные цены.', 'Валоризация: представьте, что правительство или группа компаний совместно работают над повышением стоимости чего-либо, например, ценных бумаг, пенсии и вообще любых товаров. Этот процесс и есть валоризация.', 'Арбитраж - торговая стратегия, нацеленная на извлечение прибыли из разницы в  цене на один и тот же товар на разных рынках. Например, торговец покупает что-либо по низкой цене в одном месте, затем продаёт совершенно в другом месте по более высокой цене.', 'Laissez-faire - французский термин, который означает «пусть делают» или «оставьте всë как есть».В экономике он означает, что бизнесу разрешено работать при незначительном вмешательстве государства.', 'Хеджирование - можно назвать это запасным планом. Представим, что бизнес или инвесторы предпринимают действия, чтобы защитить себя от возможных потерь. Например, фермер может застраховаться от падения цен на урожай, заранее зафиксировав цену.', 'Эффект Веблена - величина, на которую возрастает спрос из-за того, что товар имеет более высокую, а не более низкую цену. Он выражает стремление потребителя приобретать дорогие товары, недоступные для большинства.', 'Эффект сноба - величина, на которую упадёт спрос, потому что другие увеличивают потребление этого товара. Он выражает стремление потребителя владеть уникальными товарами, а не просто товарами массового производства.', 'Товар Гиффена — это вид блага, спрос на который растёт (падает) с ростом (снижением) его цены.', 'Амортизация — это процесс разделения стоимости долгосрочного актива на протяжении его срока службы. В результате амортизации стоимость актива уменьшается со временем до его полного износа или устаревания.', 'Волатильность - показатель, показывающий изменчивость цены. Волатильным называется актив, который за определённый промежуток времени может резко подорожать или снизиться в цене', 'Дефолт - ситуация, когда заемщик не может вовремя погасить процент по долгу. Дефолт может возникнуть как на уровне индивидуального заёмщика, так и на уровне государства.', 'Маржа — это разница между выручкой от продажи товаров или услуг и затратами на их производство. Она показывает, сколько денег остается компании после того, как она покрыла свои расходы.']
@router.message(Command('start'))
async def send_welcome(message: Message):
    kb = [
        [
            types.KeyboardButton(text='Учебники'),
            types.KeyboardButton(text='Новое слово'),
            types.KeyboardButton(text='Реши задачу'),
            types.KeyboardButton(text='Формулы'),
            types.KeyboardButton(text='Чек-лист')

        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer("Всем привет! Меня зовут Лиза Кузнецова и я преподаватель по экономике. Я создала этот бот, чтобы помочь моим ученикам еще больше подружиться с этой занимательной, но не простой наукой! Надеюсь, он сможет ответить на ваши вопросы: просто нажмите на кнопку ниже в соответствии с вашим запросом)", reply_markup=keyboard)

@router.message(F.text.lower() == "учебники")
async def send_book(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text='Мария Бойко "Азы экономики"',
        url="https://azy-economiki.ru/docs/the_basics_of_Economics.pdf"
    ))
    builder.add(types.InlineKeyboardButton(
        text='Мэнкью "Принципы экономикс"',
        url="https://drive.google.com/file/d/1zWkeb8-3HyuLWeH-DgkJJNLI6bYSVXbm/view?usp=share_link"
    ))
    builder.add(types.InlineKeyboardButton(
        text='Корнейчук "Микроэкономика"',
        url="https://urait.ru/viewer/mikroekonomika-537612#page/1"
    ))
    builder.add(types.InlineKeyboardButton(
        text='Акимов "Сборник задач"',
        url="https://drive.google.com/file/d/1lsLwRejU2ihu0Ucvs8WBKWdba1AR0i35/view?usp=share_link"
    ))
    builder.add(types.InlineKeyboardButton(
        text='Учебник по финансовой грамотности"',
        url="https://drive.google.com/file/d/1hiDEH3oJYST17sDcrmWDPpXgemghSY08/view?usp=share_link"
    ))
    await message.answer("Эти учебники позволят тебе освоить базовые экономические теории! Начинать советую с Бойко (азы экономики) или Мэнкью (принципы экономикс),а отрабатывать полученные знания с помощью прорешивания задачника (Акимов) ",
                         reply_markup=builder.as_markup())

@router.message(F.text.lower() == "новое слово")
async def random_newWord(message: types.Message):
    newWord= random.choice(newWords)
    await message.answer(newWord)

@router.message(F.text.lower() == "реши задачу")
async def send_solution(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text='безработица',
        callback_data='unemployed'
    ))
    builder.add(types.InlineKeyboardButton(
        text='инфляция',
        callback_data='inflation'
    ))
    builder.add(types.InlineKeyboardButton(
        text='ВВП',
        callback_data='GDP'
    ))
    await message.answer(
        "Выбери тему, по которой необходимо решить задачу и затем введи условия задачи",
        reply_markup=builder.as_markup())

@dp.callback_query(F.data == 'unemployed')
async def send_unemployed(callback: types.CallbackQuery):
    await callback.message.answer("Введите кол-во безработных и рабочую силу, разделив два числа пробелом.")

@dp.message(lambda message: message.text.strip().count(' ') == 1)
async def calculate_division(message: types.Message):
    try:
        numbers = list(map(float, message.text.split()))
        if len(numbers) != 2:
            await message.answer("Пожалуйста, введите ровно два числа.")
            return

        result = numbers[0] / numbers[1]
        await message.answer(f"Безработица равна: {result}")
    except ValueError:
        await message.answer("Пожалуйста, введите корректные числа.")
    except ZeroDivisionError:
        await message.answer("На ноль делить нельзя.")

@dp.callback_query(F.data == 'inflation')
async def send_inflation(callback: types.CallbackQuery):
    await callback.message.answer('какой бы ответ мы не получили, инфляция в России уж очень высокая...')

@dp.callback_query(F.data == 'GDP')
async def send_GDP(callback: types.CallbackQuery):
    await callback.message.answer('формула для нахождения ВВП уж слишком проста, так что попробуй решить задачу самостоятельно))')

@router.message(F.text.lower() == "формулы")
async def send_question(message: types.Message):
    username = message.from_user.first_name
    await message.answer(username + ', хочешь получить все формулы?... ну это сакральный файл, нужно знать кодовое слово!'+'\n' + 'напиши мне фамилию отца-основателя классической политэкономии, но перед этим поставь знак /'
                          )

@router.message(Command('Смит'))
async def send_photo(message: types.Message):
    await message.answer("Отправляю формулы...")
    with open("formulka.jpg", "rb") as photo:
        await message.answer_photo(photo)


@router.message(F.text.lower() == "чек-лист")
async def send_list(message: Message):
    username = message.from_user.username
    await message.answer(username + ", лови чек-лист по экономике!" + '\n'
                                    ' ' + '\n'                                 
                                    ' МИКРОЭКОНОМИКА:' + '\n'
                                    '- КПВ' + '\n'
                                    '- Спрос, функция спроса и закон спроса' + '\n'
                                    '- Предложение, функция предложения и закон предложения ' + '\n'
                                    '- Издержки' + '\n'
                                    '- Модель рыночного равновесия' + '\n'
                                    '- Налоги' + '\n'
                                    '- теория процентов (простые и сложные)' + '\n'
                                    '- Эластичность' + '\n'
                                    '- Общая и предельная полезность ' + '\n'
                                    '- Фирма в рыночной экономике: доходы, расходы, прибыль' + '\n'
                                    '- экономическая и бухгалтерская прибыль' + '\n'
                                    '- Виды рыночных структур (виды конкуренций: совершенная конкуренция и монополия)' + '\n'
                                    + ' МАКРОЭКОНОМИКА:' + '\n'
                                    '- Кругооборот продукта, расходов и доходов' + '\n'
                                    '- Основные макроэкономические показатели' + '\n'
                                    '- Система национальных счетов (ВВП, ВНП, ВНРД)' + '\n'
                                    '- Равновесие в модели AD-AS' + '\n'
                                    '- Безработица ' + '\n'
                                    '- Деньги в экономике: закон денежного обращения' + '\n'
                                    '- Банковская система, банковский мультипликатор' + '\n'
                                    '- Монетарная и фискальная политика' + '\n'
                                    '- Инфляция и дефляция' + '\n'
                                    '- Концепции внешней торговли: экспорт и импорт'
                         )
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text='помощь',
        callback_data='press'
    ))
    await message.answer('Ты устал решать экономику?',
                        reply_markup=builder.as_markup())

@dp.callback_query(F.data == 'press')
async def send_something(callback: types.CallbackQuery):
    await callback.message.answer("а что ты хотел: экономическую панацею?... тяжело в учении - легко в бою (олимпиаде). Верю в тебя - ты справишься!")



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
