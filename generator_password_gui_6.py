# Импортируем модули.
# Модуль tkinter содержит компоненты
# графического интерфейса пользователя.
from tkinter import Tk, mainloop, messagebox, IntVar, W, StringVar, END
from tkinter.ttk import Frame, Label, Entry, Button, Radiobutton, Checkbutton, LabelFrame
# Модуль secrets предоставляет функции для генерации
# случайного выбора элементов последовательности.
from secrets import choice
from random import shuffle
# Pyperclip предоставляет кроссплатформенный модуль
# Python для копирования и вставки текста в буфер обмена.
import pyperclip


class GUIPassword:

    def __init__(self):
        # Переменная для русских букв.
        self.__ru_letters: str = 'йцукенгшщзхъфывапролджэячсмитьбюё'
        # Переменная для заглавных русских букв.
        self.__capital_ru_letters: str = 'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
        # Переменная для латинских символов.
        self.__en_letters: str = "qwertyuiopasdfghjklzxcvbnm"
        # Переменная для заглавных латинских символов.
        self.__capital_en_letters: str = "QWERTYUIOPASDFGHJKLZXCVBNM"
        # Переменная различных символов.
        self.__sym: str = "!@#$%^&*_-()+=?/.,№;%:|[]{}"
        # Переменная для цифр.
        self.__num: str = "1234567890"

        # Создаем главное окно программы.
        self.main_window = Tk()
        # Название программы.
        self.main_window.title('Генератор паролей')

        # Создаем фреймы. Фреймы помогают
        # упорядочивать элементы в окне программы.
        # Верхний фрейм.
        self.top_frame = LabelFrame(text='Внимание!')
        # Фрейм создан, что-бы упорядочить
        # фреймы с радио кнопками и чек боксами.
        self.main_mid_frame = LabelFrame()
        # Второй верхний фрейм.
        self.top_frame_1 = Frame(self.main_mid_frame)
        # Средний фрейм.
        self.mid_frame = Frame(self.main_mid_frame)
        # Ещё один средний фрейм.
        self.mid_frame_1 = Frame(self.main_mid_frame)
        self.mid_frame_2 = LabelFrame()
        # Нижний фрейм.
        self.bottom_frame = LabelFrame()
        # Второй нижний фрейм.
        self.bottom_frame_1 = Frame()

        # Информационный лейбл.
        self.label_1 = Label(self.top_frame_1, text='Введите количество символов в пароле:')
        # Поле для ввода количества символов в пароле.
        self.entry_1 = Entry(self.top_frame_1, width=5, justify='right')
        # Минимальное количество символов в пароле.
        self.entry_1.insert(0, '4')
        self.entry_1.focus()
        self.label_2 = Label(self.top_frame, text='Длина надежного пароля составляет 10 символов!')

        self.label_1.pack(padx=(21, 0), pady=5, side='left')
        self.entry_1.pack(padx=(0, 21), pady=5, side='left')
        self.label_2.pack(padx=5, pady=10)

        # Переменная для выбора русски или латинских букв.
        self.radio_var = IntVar()
        self.radio_var.set(1)
        # Радиокнопки для выбора.
        self.rb_1 = Radiobutton(self.mid_frame, text='Английские буквы', variable=self.radio_var, value=1)
        self.rb_2 = Radiobutton(self.mid_frame, text='Русские буквы', variable=self.radio_var, value=2)
        self.rb_1.pack(pady=(0, 5), side='left')
        self.rb_2.pack(pady=(0, 5), side='left')

        # Создаем переменные для чек боксов, присваиваем им значения IntVar.
        self.cb_letters = IntVar()
        self.cb_capital_letters = IntVar()
        self.cb_sym = IntVar()
        self.cb_num = IntVar()

        # При открытии окна программы все чек боксы будут выбраны.
        self.cb_letters.set(1)
        self.cb_capital_letters.set(1)
        self.cb_sym.set(1)
        self.cb_num.set(1)

        # Создаем чек боксы.
        self.cb_cap_let = Checkbutton(self.mid_frame_1, text=' Заглавные буквы', variable=self.cb_capital_letters)
        self.cb_let = Checkbutton(self.mid_frame_1, text=' Строчные буквы', variable=self.cb_letters)
        self.cb_symbols = Checkbutton(self.mid_frame_1, text=' Разные символы', variable=self.cb_sym)
        self.cb_number = Checkbutton(self.mid_frame_1, text=' Цифры', variable=self.cb_num)

        # Упаковываем чек боксы.
        self.cb_cap_let.pack(anchor=W)
        self.cb_let.pack(anchor=W)
        self.cb_symbols.pack(anchor=W)
        self.cb_number.pack(anchor=W, pady=(0, 10))

        # Создаем кнопку для генерации пароля.
        self.button_generate = Button(self.bottom_frame, text='Сгенерировать', command=self.__generate)
        self.button_generate.pack(padx=(20, 5), pady=(0, 10), side='left')

        # Информационный лейбл.
        self.label_3 = Label(self.mid_frame_2, text='Скопируйте сгенерированный пароль:')
        self.label_3.pack(padx=50)
        # Создаем кнопку для копирования пароля в буфер обмена.
        self.button_copy = Button(self.bottom_frame, text='Копировать в буфер обмена', command=self.__copy_clipboard)

        self.value_label_4 = StringVar()
        self.label_4 = Label(self.mid_frame_2, textvariable=self.value_label_4)
        self.label_4.pack(pady=5)
        self.button_copy.pack(padx=(5, 20), pady=(0, 10), side='left')

        # Кнопка для закрытия программы.
        self.quit_button = Button(self.bottom_frame_1, text='Закрыть', command=self.main_window.destroy)
        self.quit_button.pack(side='right')

        # Упаковываем фреймы.
        self.top_frame.pack(pady=(10, 0))
        self.top_frame_1.pack()
        self.main_mid_frame.pack()
        self.mid_frame.pack()
        self.mid_frame_1.pack(anchor=W, padx=49, pady=(0, 5))
        self.mid_frame_2.pack()
        self.bottom_frame.pack()
        self.bottom_frame_1.pack(padx=(320, 5), pady=5)

        # Главный цикл программы.
        mainloop()

    # Вспомогательная функция для генерации пароля.
    def __generate(self):

        # Очищаем поле, которое показывает сгенерированный пароль.
        self.value_label_4.set('')
        # Пытаемся считать то, что ввел пользователь.
        try:
            # Если пользователь ввел не числовые символы: - То возникнет ошибка ValueError.
            # Если введенное число меньше 4, то переменной будет присвоено значение 4.
            lenght: int = int(self.entry_1.get())
            if lenght < 4:
                # Выводим информационное окно.
                question = messagebox.askyesno('Вопрос?', 'Минимальная длина генерируемого пароля 4 символа!\nУстановить длину в 4 символа?')
                if question:
                    messagebox.showinfo('Предупреждение', 'Длина сгенерированного пароля будет 4 символа!')
                    lenght: int = 4
                    # Функция очищает поле ввода длинны пароля.
                    # Устанавливает начальное значение.
                    # Устанавливает фокус на поле ввода.
                    self.__set_window_input()
                else:
                    # Функция очищает поле ввода длинны пароля.
                    # Устанавливает начальное значение.
                    # Устанавливает фокус на поле ввода.
                    self.__set_window_input()
                    return
        except ValueError:
            # Информируем пользователя.
            messagebox.showerror('Ошибка', 'Вы ввели неверные символы!')
            # Если пользователь ввел число меньше 4, то задаем ему вопрос.
            question = messagebox.askyesno('Вопрос?', 'Минимальная длина генерируемого пароля 4 символа!\nУстановить длину в 4 символа?')
            # Получаем ответ пользователя.
            if question:
                # При положительном ответе пользователя предупреждаем
                # его о длине созданного пароля и очищаем окно ввода длины пароля.
                messagebox.showinfo('Предупреждение', 'Длина сгенерированного пароля будет 4 символа!')
                lenght: int = 4
                # Функция очищает поле ввода длинны пароля.
                # Устанавливает начальное значение.
                # Устанавливает фокус на поле ввода.
                self.__set_window_input()
            else:
                # Если пользователь даёт отрицательный ответ,
                # то сначала очищаем окно, затем устанавливаем
                # в окне ввода длину равную 4. Устанавливаем фокус, и выходим из функции.
                # Функция очищает поле ввода длинны пароля.
                # Устанавливает начальное значение.
                # Устанавливает фокус на поле ввода.
                self.__set_window_input()
                return

        # Функция генерация пароля.
        password = self.__generate_password(lenght)
        # Если функция возвращает False, то прерываем функцию.
        if not password:
            return

        # Вставляем полученный пароль в поле показа пароля.
        self.value_label_4.set(password)
        # Выводим информационное окно с вопросом, о копировании пароля.
        result = messagebox.askyesno('Вопрос?', 'Программа сгенерировала пароль. '
                                                '\nКопировать сгенерированный пароль в буфер обмена?')
        if result:
            # При положительном ответе пользователя копируем пароль в буфер обмена.
            pyperclip.copy(password)
            # Окно для информирования пользователя.
            messagebox.showinfo('Внимание!', 'Пароль скопирован в буфер обмена!')
            # Функция очищает поле ввода длинны пароля.
            # Устанавливает начальное значение.
            # Устанавливает фокус на поле ввода.
            self.__set_window_input()
        else:
            # Окно при отрицательном ответе пользователя.
            messagebox.showwarning('Внимание!', 'Пароль не был скопирован!')
            # Функция очищает поле ввода длинны пароля.
            # Устанавливает начальное значение.
            # Устанавливает фокус на поле ввода.
            self.__set_window_input()

    # Основная функция для генерации пароля,
    # к аргументам добавляем выбранную пользователем длину пароля.
    def __generate_password(self, l):

        # Переменные для подсчета количества символов в пароле.
        count_letters, count_capital_letters, count_sym, count_num = 0, 0, 0, 0
        # Инициализируем переменную для создания пароля.
        pas: str = ""

        # Цикл генерации пароля. Если в сгенерированном пароле
        # будет не хватать одного символа, то цикл будет повторен.
        while count_letters < 1 or count_capital_letters < 1 or count_sym < 1 or count_num < 1:
            # Если пароль был сгенерирован,
            # то очищаем переменную.
            pas: str = ""
            # Список выбранных символов.
            pas_list: list = []
            # Считываем какие символы выбрал пользователь.
            choice_radio = self.radio_var.get()
            # В зависимости от выбора пользователя, присваиваем
            # переменным либо английские буквы, либо русские буквы.
            if choice_radio == 1:
                letters: str = self.__en_letters
                capital_letters: str = self.__capital_en_letters
            else:
                letters: str = self.__ru_letters
                capital_letters: str = self.__capital_ru_letters
            # Переменные символов и цифр.
            sym: str = self.__sym
            num: str = self.__num

            # Считываем выбор пользователя. Если пользователь
            # снял все флажки, то прерываем выполнение функции.
            selection_capital_letters: int = self.cb_capital_letters.get()
            selection_letters: int = self.cb_letters.get()
            selection_symbols: int = self.cb_sym.get()
            selection_number: int = self.cb_num.get()
            if (selection_capital_letters == 0 and
                    selection_letters == 0 and
                    selection_symbols == 0 and
                    selection_number == 0):
                messagebox.showerror('Ошибка! Ошибка! Ошибка!',
                                     'Выберите хотя бы один флажок!\nПароль не был сгенерирован!')
                return False

            # При снятии флажка присваиваем переменной пустое значение.
            if selection_capital_letters == 0:
                capital_letters = ''
            if selection_letters == 0:
                letters = ''
            if selection_symbols == 0:
                sym = ''
            if selection_number == 0:
                num = ''
            # Цикл генерации пароля.
            for _ in range(l):
                # Переменная символа, выбранного случайным образом.
                x: str = choice(letters + capital_letters + sym + num)
                # Прибавляем полученный символ к списку.
                pas_list.append(x)
            # Перемешиваем полученный список.
            shuffle(pas_list)
            # Создаем пароль из списка.
            pas = ''.join(pas_list)
            # Обнуляем переменные для подсчета количества символов.
            count_letters, count_capital_letters, count_sym, count_num = 0, 0, 0, 0
            # Цикл для подсчета количества символов в пароле.
            for _ in pas:
                if _ in letters:
                    count_letters += 1
                elif _ in capital_letters:
                    count_capital_letters += 1
                elif _ in sym:
                    count_sym += 1
                elif _ in num:
                    count_num += 1
            # Чтобы цикл генерации не получился бесконечным,
            # при снятии пользователем одного из флажков, то присваиваем
            # переменным подсчета количества символов единицу.
            if selection_capital_letters == 0:
                count_capital_letters = 1
            if selection_letters == 0:
                count_letters = 1
            if selection_symbols == 0:
                count_sym = 1
            if selection_number == 0:
                count_num = 1

        # Возвращаем полученный пароль.
        return pas

    # Функция для копирования пароля в буфер обмена.
    def __copy_clipboard(self):

        # Считываем сгенерированный пароль.
        clipboard = self.value_label_4.get()
        # Проверка, что бы поля пароля не было пустым.
        if clipboard:
            # Если пароль не пустой, то копируем в буфер обмена.
            pyperclip.copy(clipboard)
            # Окно для информирования пользователя.
            messagebox.showinfo('Внимание!', 'Пароль скопирован в буфер обмена!')
        else:
            # Информируем пользователя при пустом поле пароля.
            messagebox.showwarning('Внимание!', 'Пароль не был скопирован!')

    # Функция очищает поле ввода длинны пароля.
    # Устанавливает начальное значение.
    # Устанавливает фокус на поле ввода.
    def __set_window_input(self):
        # Очищаем поле ввода длины пароля.
        self.entry_1.delete(0, END)
        # Устанавливаем начальную длину пароля в 4 символа.
        self.entry_1.insert(0, '4')
        # Устанавливаем фокус в поле длины пароля.
        self.entry_1.focus()


if __name__ == '__main__':
    password_gui = GUIPassword()
