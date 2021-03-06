# -*- coding: utf-8 -*-
import sys
import time

from arduino import Arduino
from multiprocessing import freeze_support

# Два наступних рядки істотні для роботи на ОС Windows.
if __name__ == '__main__':
  freeze_support()
  # Об'єкт який дає доступ до API мотора та молоточків.
  device = Arduino()
  # Комунікаційна бібліотека ігнорує дані деякий час, тому даємо їй час на ініціалізацію.
  time.sleep(0.5)
  start = time.time()
  # Розпочати рух вперед. Платформа буде їхати вперед доки ми її не зупинимо.
  device.forwardMotor()
  while True:
      ###################################
      # Далі йде блок де ви маєте розмістити ваш код. Наведений код є лише прикладом.
      #
      # Якщо ми їдемо 3 секунди - зупинити мотор і припинити виконання програми.
      if time.time() - start > 3:
          device.stopMotor()
          break
      ###################################
      # Гарною практикою є повернення контролю системі на деякий час.
      time.sleep(0.05)
