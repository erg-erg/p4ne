'''описать/создать класс IPv4RandomNetwork унаследованный от IPv4Network библиотеки ipaddress
должен содержать метод regular, возвращающий True, если сеть обычная, и False — в остальных случаях (воспользуйтесь полями базового класса IPv4Network.is_*)

создавать экземпляры и проверять на соответствие is.global далее выводить на печать, список из 50 адресов
Диапазон — между 11.0.0.0 (0x0B000000) и 223.0.0.0 (0xDF000000)
Диапазоны адресов должны быть реальными (не частными)
Маска — между /8 и /24
используйте функцию sorted; задайте функцию сортировки и передайте её в качестве параметра key в функцию sorted'''
#Должен появиться список IP-адресов с масками, отсортированный сначала по длине префикса (короткие вверху), затем по значению

from ipaddress import IPv4Network
import random

#создаем класс IPv4RandomNetwork унаследованный от IPv4Network библиотеки ipaddress
class IPv4RandomNetwork(IPv4Network):
    def __init__(self, n=):
        IPv4Network.__init__(self, …)





net = random.randint(0x0b000000, 0xdf000000)
mask = random.randint(8, 24)
net3 = ipaddress.IPv4Network((net, mask), strict=False)



    def key_value(self):
        return ...

int(IPv4Network.network_address) #получить адрес подсети в виде числа
int(IPv4Network.netmask) #получить маску подсети в виде числа
sorted(, key=) #(последовательность, key=функция) — возвращает отсортированную последовательность
