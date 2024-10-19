# Импортируем нужные библиотеки.
import tkinter
from tkinter import ttk, NSEW
import locale
import calendar
import datetime
from datetime import datetime


class CalendarGui:
    def __init__(self):
        # Переводим в русскую локаль.
        locale.setlocale(locale.LC_ALL, "")
        # Главное окно программы.
        self.window = tkinter.Tk()
        # Список дней.
        self.days = []
        # Дата.
        self.now = datetime.now()
        # Месяц.
        self.month = self.now.month
        # Год.
        self.year = self.now.year

        # Кнопка "Назад".
        self.back_button = ttk.Button(text='<', command=self.back)
        self.back_button.grid(row=0, column=0, sticky=NSEW)

        # Кнопка "Вперед".
        self.next_button = ttk.Button(text='>', command=self.next)
        self.next_button.grid(row=0, column=6, sticky=NSEW)

        # Информационное окно между кнопками.
        self.info_label = ttk.Label(text='0', width=1, font='Arial 10 bold')
        self.info_label.grid(row=0, column=1, columnspan=5, sticky=NSEW)

        for n in range(7):
            lbl = tkinter.Label(text=calendar.day_abbr[n], width=1, font='Arial 10 bold')
            lbl.grid(row=1, column=n, sticky=NSEW)

        for row in range(6):
            for col in range(7):
                lbl = tkinter.Label(text='0', width=4, font='Arial 10 bold')
                lbl.grid(row=row + 2, column=col, sticky=NSEW)
                self.days.append(lbl)

        self.fill()

        month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
                 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
        year = self.year

        tkinter.mainloop()


    def back(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.fill()

    def next(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.fill()

    def fill(self):
        self.info_label['text'] = calendar.month_name[self.month] + ', ' + str(self.year)
        month_days = calendar.monthrange(self.year, self.month)[1]
        if self.month == 1:
            back_month_days = calendar.monthrange(self.year - 1, 12)[1]
        else:
            back_month_days = calendar.monthrange(self.year, self.month - 1)[1]
        week_day = calendar.monthrange(self.year, self.month)[0]

        for n in range(month_days):
            self.days[n + week_day]['text'] = n + 1
            self.days[n + week_day]['fg'] = 'black'
            if self.year == self.now.year and self.month == self.now.month and n == self.now.day:
                self.days[n + week_day - 1]['bg'] = 'yellow'
                self.days[n + week_day]['bg'] = 'gray'
            else:
                self.days[n + week_day]['bg'] = 'gray'

        for n in range(week_day):
            self.days[week_day - n - 1]['text'] = back_month_days - n
            self.days[week_day - n - 1]['fg'] = 'gray'
            self.days[week_day - n - 1]['bg'] = '#f3f3f3'
        for n in range(6 * 7 - month_days - week_day):
            self.days[week_day + month_days + n]['text'] = n + 1
            self.days[week_day + month_days + n]['fg'] = 'gray'
            self.days[week_day + month_days + n]['bg'] = '#f3f3f3'


if __name__ == '__main__':
    calendar = CalendarGui()