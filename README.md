## Описание
Скрипт получает на вход ссылку, сокращает её и указывает количество кликов по ней
## Требования
Для работы требуется библиотека requests 2.32.4 и python-decouple 3.8
```
pip install requests==2.32.4
```
```
pip install python-decouple==3.8
```
## Использование
При запуске скрипта требуется указать ссылку с ключом `-l` или `--link`. 
```
python main.py -l https://www.google.com/
```
<img width="477" height="60" alt="image" src="https://github.com/user-attachments/assets/c4d16e86-88b3-4b2e-ae9a-47c424acfd3b" />

Если ссылка уже сокращена скрипт выдаст количество кликов по ней.
```
python main.py -l https://vk.cc/snBwO
```
<img width="446" height="45" alt="image" src="https://github.com/user-attachments/assets/2caa1968-30dc-4cf4-bc4d-5a121a543dad" />
