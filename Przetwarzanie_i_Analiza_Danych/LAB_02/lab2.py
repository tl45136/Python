import numpy as np
import pandas as pds
import matplotlib.pyplot as plt
from scipy import stats


# manipulowanie danymi
def manipulowanie():
    data = pds.date_range('2020-03-01', periods=5)
    numbers = np.random.randint(100, size=(5, 3))
    data_frame = pds.DataFrame(data=numbers, columns=list('ABC'), index=data)
    data_frame.index.name = 'data'
    print(data_frame)


# wygeneruj tabele
def tabela():
    tab = pds.DataFrame(np.random.randint(-100, 100, size=(20, 3)), columns=list('ABC'))
    tab.index.name = 'id'
    print(tab)
    print(tab.head(3))  # trzy pierwsze wiersze tabeli
    print(tab.tail(3))  # trzy ostatnie wiersze tabeli
    print(tab.index.name)  # indeks tabeli
    print(list(tab.columns))  # nazwy kolumn
    print(tab.values)  # dane bez indeksow i naglowkow
    print(tab.sample(5))  # losowo wybrane wiersze
    print(tab['A'])  # tylko wartosci A
    print(tab[['A', 'B']])  # tylko wartosci A i B
    print(tab.iloc[0:3, [0, 1]])  # wyswietla 3 pierwsze wiersze i kolumny A i B
    print(tab.iloc[5, :])  # wyswietla 5 wiersz
    print(tab.iloc[[0, 5, 6, 7], [1, 2]])  # wyswietla wiersze 0,5,6,7 i kolumny 1 oraz 2
    # describe generuje statystyki opisowe-
    print(tab > 0)  # sprawdza ktore dane sa wieksze od 0
    print(tab[tab > 0])  # wyswietla tylko dane wieksze od 0
    print(tab['A'] > 0)  # sprawdza ktore dane w kolumnie A sa wieksze od 0
    print(tab.mean(axis=0))  # srednia z kolumn
    print(tab.mean(axis=1))  # srednia z wierszow


# łączenie tabel
def konkatenacja():
    first_frame = {"Name": ["Pankaj", "Lisa"], "ID": [1, 2]}
    second_frame = {"Name": "David", "ID": 3}
    ff = pds.DataFrame(first_frame, index={1, 2})
    sf = pds.DataFrame(second_frame, index={3})
    concat_frames = [ff, sf] # laczenie tabel
    concated_frames = pds.concat(concat_frames)
    print(concated_frames)
    print(concated_frames.transpose())


# sortowanie
def sortowanie():
    data_frame = pds.DataFrame({'x': [1, 2, 3, 4, 5], 'y': ['a', 'b', 'a', 'b', 'b']}, index=np.arange(5))
    data_frame.index.name = 'id'
    print(data_frame.sort_index())
    print(data_frame.sort_values(by=['y'], ascending=False))


# grupowanie danych
def grupowanie():
    slownik = {'Day': ['Mon', 'Tue', 'Mon', 'Tue', 'Mon'], 'Fruit': ['Apple',
                                                                     'Apple', 'Banana', 'Banana', 'Apple'],
               'Pound': [10, 15, 50, 40, 5], 'Profit': [20, 30, 25, 20, 10]}

    data_frame3 = pds.DataFrame(slownik)
    print(data_frame3)
    print(data_frame3.groupby('Day').sum())
    print(data_frame3.groupby(['Day', 'Fruit']).sum())


# Wypełnianie danych
def wypelnianie():
    data_frame = pds.DataFrame(np.random.randn(20, 3), index=np.arange(20), columns=['A', 'B', 'C'])
    data_frame.index.name = 'id'
    print(data_frame)
    data_frame['B'] = 1  # ustawia "B" same jedynki
    print(data_frame)
    data_frame.iloc[1, 2] = 10  # Ustawia wartosc 10 w 2 wierszu w 3 kolumnie
    print(data_frame)
    data_frame[data_frame != 0] = -data_frame  # odwraca znak na przeciwny
    print(data_frame)
    return data_frame


# uzupełnianie danych
def uzupelnianie(data_frame):
    data_frame.iloc[[0, 3], 1] = np.nan  # wstawia NaN w 1 i 4 wiersz w 2 kolumnie
    data_frame.fillna(0, inplace=True)  # zamienia NaN na 0
    data_frame.iloc[[0, 3], 1] = np.nan
    print(data_frame.replace(to_replace=np.nan, value=-9999))  # zamienia NaN na wartości -9999
    data_frame.iloc[[0, 3], 1] = np.nan
    print(pds.isnull(data_frame))  # w miejscach NaN wstawia True, a w wartościach False


# manipulowanie()
# tabela()
# konkatenacja()
# sortowanie()
# grupowanie()
# wypelnianie()
# uzupelnianie(wypelnianie())
# Zadania
xy_frame = pds.DataFrame({"x": [1, 2, 3, 4, 5], "y": ['a', 'b', 'a', 'b', 'b']})


# 1
def zad1(df):
    print(df.groupby("x"))  # grupujemy po zmiennej x
    print(df.groupby("y").mean())  # wyznaczamy srednia wartosc atrybutu y w grupie x


zad1(xy_frame)


# 2
def zad2(df):
    print(df['x'].value_counts())  # rozklad licznosci atrybutow
    print(df['y'].value_counts())


zad2(xy_frame)

# 3
auto = pds.read_csv('autos.csv')  # wczytujemy csv
autos = 'autos.csv'
car = np.loadtxt(autos, dtype=str)
# read_csv wyswietla jako podzielona tabele, a loadtxt, ciagiem bez formatowania

# 4
print(auto.groupby(['make'])[
          ['city-mpg', 'highway-mpg']].mean())  # grupuje ramke po zmiennej make i wyznacza srednie spalanie atrybutow

# 5
print(auto.groupby(['make', 'fuel-type']).size().to_string())  # grupuje ramke po make dla atrybutu fuel

# 6

polynomial_1dg = np.polyfit(auto['city-mpg'], auto['length'], 1)  # wielomian 1 stopnia
print(np.polyval(polynomial_1dg, 1))
polynomial_2dg = np.polyfit(auto['city-mpg'], auto['length'], 2)  # wielomian 2 stopnia
print(np.polyval(polynomial_2dg, 1))

# 7
print(stats.pearsonr(auto['city-mpg'], auto['highway-mpg']))  # wspolczynnik korelacji

# 8
plt.plot(auto['length'], auto['city-mpg'], '.', label='Probka')
plt.plot(np.unique(auto['length']),
         np.poly1d(np.polyfit(auto['length'], auto['city-mpg'], 1))(np.unique(auto['length'])), 'red', label='Krzywa')
plt.legend()
plt.show()

# 9
sort = np.sort(auto['length'])
x = stats.gaussian_kde(sort)
plt.plot(sort, x(sort), 'green', label='Funckcja gestosci')
plt.plot(sort, x(sort), '.', label='Probka')
plt.legend()
plt.show()

# 10
len_sort = np.sort(auto['length'])
wid_sort = np.sort(auto['width'])
x = stats.gaussian_kde(len_sort)
y = stats.gaussian_kde(wid_sort)

plt.subplot(1, 2, 1)
plt.plot(len_sort, x(len_sort), 'black', label='Funkcja gestosci')
plt.plot(len_sort, x(len_sort), 'ro', label='Probka')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(wid_sort, y(wid_sort), 'black', label='Funkcja gestosci')
plt.plot(wid_sort, y(wid_sort), 'ro', label='Probka')
plt.legend()
plt.show()
