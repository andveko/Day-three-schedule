# Эта программа показывает
# температуру в выбранном городе.


# подключаем библиотеку для работы с запросами
import requests
import tkinter
import tkinter.messagebox
from typing import Any


class TempGUI:
    def __init__(self) -> None:
        # Создаем главное окно.
        self.main_window = tkinter.Tk()
        self.main_window.title('Температура в городе ...')
        self.main_window.geometry('350x100')
        # Создаём три рамки, чтобы сгруппировать виджеты.
        self.top_frame: tkinter.Frame = tkinter.Frame()
        self.mid_frame: tkinter.Frame = tkinter.Frame()
        self.mid_frame_1: tkinter.Frame = tkinter.Frame()
        self.bottom_frame: tkinter.Frame = tkinter.Frame()

        # Создаем виджеты верхнего фрейма.
        self.text_label: tkinter.Label = tkinter.Label(self.top_frame, text='Введите город:')
        self.city_entry: tkinter.Entry = tkinter.Entry(self.top_frame, width=20, bg='white')

        # Упаковываем виджеты верхнего фрейма.
        self.text_label.pack(side='left')
        self.city_entry.pack(side='left')

        # Видджеты среднего фрейма.
        self.values_city: tkinter.StringVar = tkinter.StringVar()
        self.city_temperature_label: tkinter.Label = tkinter.Label(self.mid_frame, text='Температура в городе')
        self.city_label: tkinter.Label  = tkinter.Label(self.mid_frame, textvariable=self.values_city)
        self.city_temperature_feels_label: tkinter.Label  = tkinter.Label(self.mid_frame_1, text='Ощущается, как')

        #
        self.values_temperature: tkinter.StringVar = tkinter.StringVar()
        self.values_temperature_feels: tkinter.StringVar = tkinter.StringVar()

        #
        self.city_temp: tkinter.Label = tkinter.Label(self.mid_frame, textvariable=self.values_temperature)
        self.city_temp_feels: tkinter.Label = tkinter.Label(self.mid_frame_1, textvariable=self.values_temperature_feels)

        # Упаковываем виджеты среднего фрейма.
        self.city_temperature_label.pack(side='left')
        self.city_label.pack(side='left')
        self.city_temperature_feels_label.pack(side='left')
        self.city_temp.pack(side='left')
        self.city_temp_feels.pack(side='left')

        # Нижний фрейм.
        self.temperature_button: tkinter.Button = tkinter.Button(self.bottom_frame, text='Показать температуру', command=self.temperature)
        self.quit_button: tkinter.Button = tkinter.Button(self.bottom_frame, text='Закрыть', command=self.main_window.destroy)

        # Упаковываем кнопки.
        self.temperature_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Упаковываем фреймы.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.mid_frame_1.pack()
        self.bottom_frame.pack()

        # Главный цикл программы.
        tkinter.mainloop()


    def temperature(self):
        # Считываем название города.
        city: str = self.city_entry.get().title()
        if city != '':
            try:
                url: str = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
                weather_data: Any = requests.get(url).json()
                if weather_data['cod'] == 200:
                    temperature: Any = round(weather_data['main']['temp'])
                    temperature_feels: Any = round(weather_data['main']['feels_like'])
                    self.values_city.set(city)
                    self.values_temperature.set(temperature)
                    self.values_temperature_feels.set(temperature_feels)
                elif weather_data['cod'] == '404':
                    tkinter.messagebox.showerror('Ошибка!', f'Такого города {city} не существует!')
            except Exception as e:
                tkinter.messagebox.showerror('Ошибка', f'Произошла ошибка: {e}')
        else:
            tkinter.messagebox.showerror('Ошибка', "Пожалуйста, введите город!")


# Создаем экземпляр класса.
if __name__ == '__main__':
    temperature = TempGUI()