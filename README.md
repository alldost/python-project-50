### Hexlet tests and linter status:
[![Actions Status](https://github.com/alldost/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/alldost/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/16005ca9e19412f1d11d/maintainability)](https://codeclimate.com/github/alldost/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/16005ca9e19412f1d11d/test_coverage)](https://codeclimate.com/github/alldost/python-project-50/test_coverage)
[![Python CI](https://github.com/alldost/python-project-50/actions/workflows/python-app.yml/badge.svg)](https://github.com/alldost/python-project-50/actions)

"Вычислитель отличий" представляет собой CLI-утилиту, которая сравнивает содержимое двух файлов и выводит информацию об изменениях во втором файле относительно первого.
Утилита вызывается командой gendiff, принимает на вход два обязательных аргумента - пути до сравниваемых файлов, и один опциональный - формат отоборажения результата.

Минимальные требования для запуска:
* Python версии 3.9 или выше
* Pip версии 21 или выше
* Poetry версии 1.2.0 или выше (для установки можно воспользоваться командой make install)

Для установки пакета необходимо выполнить следующие команды:

1. Выполнить сборку командой make build (альтернативна - poetry build)
2. Выполнить публикацию командой make publish (альтернатива - poetry publish --dry-run)
3. Выполнить установку пакета командой make package-install (альтернатива - python3 -m pip install --user dist/*.whl)
4. !Опционально! В случае, если пакет уже был установление, но в него были внесены изменеиня, следует переустановить пакет командой make package-reinstall (альтернатива - python3 -m pip install --user --force-reinstall dist/*.whl)

[![asciicast](https://asciinema.org/a/G8O1Q0tghVMazJHphvDOpvZps.svg)](https://asciinema.org/a/G8O1Q0tghVMazJHphvDOpvZps)


Сравнение доступно для файлов формата .json и .yaml. Сравниваться могут как "плоские" файлы, так и файлы, имеющие вложенную структуру.
Для отображения результата доступно 3 формата:

1. stylish (по умолчанию):
[![asciicast](https://asciinema.org/a/oH4yQz9q8VR56serUCPc4L2de.svg)](https://asciinema.org/a/oH4yQz9q8VR56serUCPc4L2de)
2. plain:
[![asciicast](https://asciinema.org/a/x5MXjpupyoC9rlvdtG8RgsYhh.svg)](https://asciinema.org/a/x5MXjpupyoC9rlvdtG8RgsYhh)
3. json:
[![asciicast](https://asciinema.org/a/0eiTA1tY3q7XbOVjFD8KhIArL.svg)](https://asciinema.org/a/0eiTA1tY3q7XbOVjFD8KhIArL)


Помимо утилиты пакет содержит модуль gendiff c функцией generate_diff(). Вызов этой функции возвращает строку с разницей между содержимым двух файлов:
[![asciicast](https://asciinema.org/a/kA4oekrZWcKRhKAr7EIzE7a8j.svg)](https://asciinema.org/a/kA4oekrZWcKRhKAr7EIzE7a8j)
