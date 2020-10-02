import os
import time
# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['/var/www/pythonProjects/HelloWorld']   # ['"C:\\My Documents"', 'C:\\Code']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = '../task_backup'   # Подставьте тот путь, который вы будете использовать.
# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
# os.sep - '/' в GNU/Linux и Unix 3 , '\\' в Windows и ':' в Mac OS.
target = target_dir + os.sep + time.strftime('%Y:%m:%d_%H:%M:%S') + '.zip'
# 5. Используем команду "zip" для помещения файлов в zip-архив
# https://www.oslogic.ru/knowledge/473/shpargalka-po-arhivatoru-zip/
zip_command = "zip -qr {0} {1} -x {2} {3}".format(target, ' '.join(source), source[0] + "/venv/*", source[0] + "/task_backup/*")
# Запускаем создание резервной копии
print(zip_command)
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
