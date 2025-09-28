# Эта программа показывает
# температуру в выбранном городе.

# Импортируем модули.
# Модуль tkinter содержит компоненты
# графического интерфейса пользователя.
from tkinter import Tk, mainloop, messagebox, StringVar, END, Canvas, PhotoImage, E
from tkinter.ttk import Frame, Label, Entry, Button
import requests
from PIL import Image, ImageTk
from io import BytesIO
from typing import Any
from PIL.ImageFile import ImageFile


class TempGUI:
    def __init__(self) -> None:
        # Создаем главное окно.
        self.main_window: Tk = Tk()
        self.main_window.title(f'Температура в городе ...')

        # Создаём фреймы, чтобы сгруппировать виджеты.
        self.top_frame: Frame = Frame()
        self.mid_frame: Frame = Frame()
        self.mid_frame_1: Frame = Frame()
        self.bottom_frame: Frame = Frame()

        # Упаковываем фреймы.
        self.top_frame.grid(row=0, columnspan=2, sticky=E, pady=(10, 0), padx=(20, 10))
        self.mid_frame.grid(row=1, pady=10, padx=20)
        self.mid_frame_1.grid(column=1, row=1, padx=(0, 10), pady=5)
        self.bottom_frame.grid(row=2, columnspan=2, sticky=E, padx=(0, 10), pady=10)

        # Дополнительные фреймы.
        self.additional_frame_1: Frame = Frame(self.mid_frame)
        self.additional_frame_2: Frame = Frame(self.mid_frame)
        self.additional_frame_3: Frame = Frame(self.mid_frame)
        self.additional_frame_4: Frame = Frame(self.mid_frame)
        self.additional_frame_5: Frame = Frame(self.mid_frame)

        self.additional_frame_1.pack()
        self.additional_frame_2.pack()
        self.additional_frame_3.pack()
        self.additional_frame_4.pack(pady=(5, 0))
        self.additional_frame_5.pack(pady=(0, 5))

        # Создаем виджеты верхнего фрейма.
        self.text_label: Label = Label(self.top_frame, text='Введите город: ')
        self.city_entry: Entry = Entry(self.top_frame, width=20)
        self.city_entry.focus()

        # Упаковываем виджеты верхнего фрейма.
        self.text_label.pack(side='left')
        self.city_entry.pack(side='left')

        # Виджеты среднего фрейма.
        self.values_city: StringVar = StringVar()
        self.city_temperature_label: Label = Label(self.additional_frame_1, text='Температура в городе ')
        self.city_label: Label = Label(self.additional_frame_1, textvariable=self.values_city)
        self.city_temperature_feels_label: Label = Label(self.additional_frame_2, text='Ощущается, как ')
        self.image_label: Canvas = Canvas(self.mid_frame_1, width=100, height=100, borderwidth=1,relief='raised')

        # Строковые переменные
        self.values_temperature: StringVar = StringVar()
        self.values_temperature_feels: StringVar = StringVar()
        self.values_description: StringVar = StringVar()

        self.city_temp: Label = Label(self.additional_frame_1, textvariable=self.values_temperature)
        self.city_temp_feels: Label = Label(self.additional_frame_2, textvariable=self.values_temperature_feels)
        self.label_description: Label = Label(self.additional_frame_3, textvariable=self.values_description)

        self.label_coord: Label = Label(self.additional_frame_4, text='Географические координаты:')
        self.label_lat: Label = Label(self.additional_frame_5, text='Широта: ')
        self.values_latitude: StringVar = StringVar()
        self.label_latitude: Label = Label(self.additional_frame_5, textvariable=self.values_latitude)
        self.label_lon: Label = Label(self.additional_frame_5, text='Долгота: ')
        self.values_longitude: StringVar = StringVar()
        self.label_longitude: Label = Label(self.additional_frame_5, textvariable=self.values_longitude)

        # Упаковываем виджеты среднего фрейма.
        self.city_temperature_label.pack(side='left')
        self.city_label.pack(side='left')
        self.city_temperature_feels_label.pack(side='left')
        self.city_temp.pack(side='left')
        self.city_temp_feels.pack(side='left')
        self.label_description.pack()
        self.image_label.pack()
        self.label_coord.pack()
        self.label_lat.pack(side='left')
        self.label_latitude.pack(side='left', padx=(0, 5))
        self.label_lon.pack(side='left')
        self.label_longitude.pack(side='left')

        # Нижний фрейм.
        self.temperature_button: Button = Button(self.bottom_frame, text='Показать температуру', command=self.__get_temperature)
        self.quit_button: Button = Button(self.bottom_frame, text='Закрыть', command=self.main_window.destroy)

        # Упаковываем кнопки.
        self.temperature_button.pack(side='left', padx=(0, 5))
        self.quit_button.pack(side='left', padx=(5, 0))

        # Главный цикл программы.
        mainloop()


    def __get_temperature(self) -> Any:
        # Считываем название города.
        city: str = self.city_entry.get().title()
        if city:
            try:
                url: str = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
                # Отправляем GET-запрос с использованием requests.get()
                weather_data: Any = requests.get(url).json()
                if weather_data['cod'] == 200:
                    # Получаем код для погодной иконки.
                    icon_temperature: Any = weather_data['weather'][0]['icon']
                    # Получаем изображение погодной иконки и присваиваем его переменной.
                    self.canvas_image: int = self.image_label.create_image(50, 50, image=self.load_image(icon_temperature))
                    temperature: Any = round(weather_data['main']['temp'])
                    if temperature > 0:
                        temperature = ' +' + str(temperature)
                    temperature_feels: Any = round(weather_data['main']['feels_like'])
                    if temperature_feels > 0:
                        temperature_feels = '+' + str(temperature_feels)
                    description: Any = weather_data['weather'][0]['description'].capitalize()
                    latitude: Any = weather_data['coord']['lat']
                    longitude: Any = weather_data['coord']['lon']
                    # Присваиваем строковым переменным полученные значения.
                    self.values_city.set(city)
                    self.values_temperature.set(temperature)
                    self.values_temperature_feels.set(temperature_feels)
                    self.values_description.set(description)
                    self.values_latitude.set(latitude)
                    self.values_longitude.set(longitude)
                    self.city_entry.delete(0, END)
                    self.city_entry.focus()
                # Обрабатываем неправильное написание города.
                elif weather_data['cod'] == '404':
                    messagebox.showerror('Ошибка!', f'Такого города {city} не существует!')
            # Обрабатываем непредвиденные ошибки.
            except Exception as e:
                messagebox.showerror('Ошибка', f'Произошла ошибка: {e}')
        # Обрабатываем не заполненное поле города.
        else:
            messagebox.showerror('Ошибка', "Пожалуйста, введите город!")

    # Функция скачивания погодной иконки.
    def load_image(self, icon: Any) -> PhotoImage:
        url_icon: str = f'https://openweathermap.org/img/wn/{icon}@2x.png'
        try:
            # Отправляем GET-запрос с использованием requests.get()
            response = requests.get(url_icon)
            # Проверяем успешность запроса (код ответа 200)
            response.raise_for_status()
            # Читаем байты из ответа в объект BytesIO
            image_data: BytesIO = BytesIO(response.content)
            # Открываем изображение с помощью PIL
            img: ImageFile = Image.open(image_data)
            self.widget_image = ImageTk.PhotoImage(img)
            return self.widget_image
        except Exception as e:
            messagebox.showerror('Ошибка!', f"Ошибка при загрузке изображения: {e}")


# Создаем экземпляр класса.
if __name__ == '__main__':
    temperature = TempGUI()
