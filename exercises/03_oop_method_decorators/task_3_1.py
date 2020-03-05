# -*- coding: utf-8 -*-
'''
Задание 3.1

Скопировать класс IPv4Network из задания 1.1.
Переделать класс таким образом, чтобы методы hosts и unassigned
стали переменными, но при этом значение переменной экземпляра вычислялось
каждый раз при обращении и запись переменной была запрещена.


Пример создания экземпляра класса:
In [1]: net1 = IPv4Network('8.8.4.0/29')

In [2]: net1.hosts
Out[2]: ('8.8.4.1', '8.8.4.2', '8.8.4.3', '8.8.4.4', '8.8.4.5', '8.8.4.6')

In [3]: net1.allocate('8.8.4.2')

In [4]: net1.allocate('8.8.4.3')

In [5]: net1.unassigned
Out[5]: ('8.8.4.1', '8.8.4.4', '8.8.4.5', '8.8.4.6')

Запись переменной:

In [6]: net1.unassigned = 'test'
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-6-c98e898835e1> in <module>
----> 1 net1.unassigned = 'test'

AttributeError: can't set attribute

'''