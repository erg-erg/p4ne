from matplotlib import pyplot
from openpyxl import load_workbook

# Загрузка таблицы Excel из файла в переменную wb
wb = load_workbook('C:/Users/vv.smirnov/Documents/GitHub/p4ne_erg-erg/lab1.2/data_analysis_lab.xlsx')
# Загрузка листа с именем "Data" в переменную sheet
sheet = wb['Data']
# Определяем функцию
def getvalue(x):
    return x.value

years = list(map(getvalue, sheet['A'][1:]))
temperature = list(map(getvalue, sheet['C'][1:]))
activity = list(map(getvalue, sheet['D'][1:]))

# Создаём графическое представление, но пока не показываем
pyplot.plot(years, temperature, label="Относит. температура")
pyplot.plot(years, activity, label="Активность Солнца")

# Украшаем график - добавляем надписи
pyplot.xlabel('Годы')
pyplot.ylabel('Температура/Активность Солнца')
pyplot.legend(loc='upper left')

# Отображаем график
pyplot.show()