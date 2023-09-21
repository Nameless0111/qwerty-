import math

global y
def orto(p):
 while True:
    try:
        p = int(input("Введите номер операции: "))
        x = p
        if x > 0 and x < 11:
         return x
        else:
          print("Было введено недоступное значение. Попробуйте ещё раз.")
    except ValueError:
        print("Было введено недоступное значение. Попробуйте ещё раз.")

def rerl07(l,m):
 while True:
     try:
      l = float(input("Введите делимое: "))
      m = float(input("Введите делитель: "))
      qz = l
      qz1 = m
      if m == 0 :
       print("Было введено недоступное значение. Попробуйте ещё раз.")
       continue
      else:
       return qz,qz1
     except ValueError:
        return print("Было введено недоступное значение. Попробуйте ещё раз.")

     
def rerl(l,m):
 while True:
     try:
      l = float(input("Введите первое число: "))
      m = float(input("Введите второе число: "))
      qz = l
      qz1 = m
      return qz,qz1
     except ValueError:
        return print("Было введено недоступное значение. Попробуйте ещё раз.")

def rerl3(l):
 while True:
     try:
      l = float(input("Введите угол(в радианах): "))
      qz = l
      return qz
     except ValueError:
        return print("Было введено недоступное значение. Попробуйте ещё раз.")

def rerl0(l):
 while True:
     try:
      l = float(input("Введите число: "))
      qz = l
      if qz >= 0 :
         return qz
      else:
         print("Было введено недоступное значение. Попробуйте ещё раз.")
         continue
     except ValueError:
        return print("Было введено недоступное значение. Попробуйте ещё раз.")

def rerlf(l):
 while True:
     try:
      l = int(input("Введите  целое число: "))
      qp = l
      if qp >= 0 :
         return qp
      else:
         print("Было введено недоступное значение. Попробуйте ещё раз.")
         continue
     except ValueError:
        return print("Было введено недоступное значение. Попробуйте ещё раз.")


def rerl1(l,m):
 while True:
     try:
      l = float(input("Введите число: "))
      m = float(input("Введите степень: "))
      qp = l
      qz1 = m
      return qp,qz1
     except ValueError:
        return print("Было введено недоступное значение. Попробуйте ещё раз.")

global e

e = 1
while True:
 print("Добро пожаловать! Выберите желаемую операцию.")
 print ("1. Сложение")
 print ("2. Вычитание")
 print ("3. Умножение")
 print ("4. Деление")
 print ("5. Возведение в степень")
 print ("6. Извлечение квадратного корня")
 print ("7. Факториал числа")
 print ("8. Синус угла(в радианах)")
 print ("9. Косинус угла(в радианах)")
 print ("10. Тангенс угла(в радианах)")
 print ("11. Желаете закончить?")
 print("ВАЖНО!!! При вводе чисел с плавающей точкой необходимо использовать символ(.)")
 z = orto(e)
 if z == 1:
   tre,tre1 = rerl(e,e)
   k = tre + tre1
   print(k)
 elif z == 2:
   tre,tre1 = rerl(e,e)
   k = tre - tre1
   print(k)
 elif z == 3:
   tre,tre1 = rerl(e,e)
   k = tre * tre1
   print(k)
 elif z == 4:
   tre,tre1 = rerl07(e,e)
   k = tre / tre1
   print(k)
 elif z == 5:
   tre,tre1 = rerl1(e,e)
   k = tre ** tre1
   print(k)
 elif z == 6 :
   tre = rerl0(e)
   k =math.sqrt(tre)
   print(k)
 elif z == 7 :
   tre = rerlf(e)
   k =math.factorial(tre)
   print(k)  
 elif z == 8 :
   tre = rerl3(e)
   k =math.sin(tre)
   print(k)  
 elif z == 9 :
   tre = rerl3(e)
   k =math.cos(tre)
   print(k)  
 elif z == 10 :
   tre = rerl3(e)
   k =math.tan(tre)
   print(k)
 elif z == 11 :
   break