# __README FILE FOR 5 PRACTICAL WORK__

![Римск Мемас](https://github.com/IWorkForFood/5W/assets/152487755/fe342615-48db-42ae-9fec-c369d101f7e1)

### **_Приветствуем!_**

### Введение

Данный код написан для следующих задач:
* _перевод десятичных числительных в римские_
* _перевод из римских числительных в десятичные_
* _осуществление выполнения арифметических операций с римскими числами_

С римскими числами выполняются следующие арифметические операции:
* [ ] *сложение*
* [ ] *вычитание*
* [ ] *умножение*
* [ ] *деление*
 
### Немного о начинке

Выполнение арифметических операций было выполнено при помощи перегрузки опреаторов арифметических действий
Перегразка '+':

```
def __add__(self, other_number):
        self_value = self.convert_from_roman(self.roman_value)
        other_value = self.convert_from_roman(other_number.roman_value)
        int_result = self_value + other_value
        roman_result = self.convert_to_roman(int_result)
        return roman_result
```
В результате мы сможем выполнять сложение аргументов объектов класса romanNumbers

$VII + C = CVII$

### Полезные ссылки с информацией, которая необходима для понимания кода
* [ООП на Python: концепции, принципы и примеры реализации](https://proglib.io/p/python-oop?ysclid=lq62d27v27782879973)
* [Перегрузка операторов в python](https://codechick.io/tutorials/python/oop-operator-overloading?ysclid=lq62fvlkrd140227502)
* [100% рабочие способы повысит зарплату](https://www.youtube.com/watch?v=un_Gn6Uriwc)


