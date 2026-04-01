# Python Code Merger / Объединение нескольких файлов .py в один TXT-документ.

[English](#english) | [Русский](#русский)

---

## English

### Description
**Python Code Merger** is a GUI tool that combines multiple `.py` files into a single TXT document. Perfect for AI chat systems (ChatGPT, Claude, DeepSeek) that limit file uploads to 5 files.

### Features
- ✅ Merge any number of Python files into one TXT
- ✅ Preserve structure with file headers (`=== filename.py ===`)
- ✅ UTF-8 support (Russian characters, comments)
- ✅ Simple GUI using tkinter
- ✅ Select and remove files from the list
- ✅ Auto-open folder with file highlighting (Windows via PowerShell)
- ✅ Add timestamp and file count to the output

### Installation & Usage

#### Run as Python script (requires Python 3.6+):
python pymerger.py

#### Create standalone .exe (no Python required):
pip install pyinstaller
pyinstaller --onefile --windowed pymerger.py

### How to Use
- Click "Add files" and select your .py files
- Remove unnecessary files if needed
- Click "Browse" to choose save location
- Click "Merge files"
- Done! Upload the resulting .txt file to your AI chat

### Requirements
No external dependencies - all modules are in Python standard library:
 - tkinter - GUI
 - os - file operations
 - subprocess - folder opening
 - platform - OS detection
 - datetime - timestamps

### License
MIT

## Русский
Описание
Python Code Merger — это утилита с графическим интерфейсом для объединения нескольких файлов .py в один TXT-документ. Идеально подходит для AI-чатов (ChatGPT, Claude, DeepSeek), которые ограничивают загрузку файлов (обычно до 5 штук).

Возможности
 - ✅ Объединение любого количества .py-файлов
 - ✅ Сохранение структуры с заголовками (=== имя_файла.py ===)
 - ✅ Поддержка UTF-8 (русские символы, комментарии)
 - ✅ Простой графический интерфейс на tkinter
 - ✅ Удаление файлов из списка
 - ✅ Автоматическое открытие папки с выделением файла (Windows через PowerShell)
 - ✅ Добавление даты и количества файлов в результат

### Установка и запуск

#### Запуск скрипта (требуется Python 3.6+):
python pymerger.py

#### Создание .exe (Python не требуется):
pip install pyinstaller

pyinstaller --onefile --windowed pymerger.py

### Как пользоваться

- Нажмите "Добавить файлы" и выберите все .py-файлы вашего проекта
- При необходимости удалите лишние файлы из списка
- Нажмите "Обзор..." и выберите место сохранения результата
- Нажмите "Объединить файлы"
- Готово! Загрузите полученный .txt файл в AI-чат

### Зависимости
Нет внешних зависимостей — все модули входят в стандартную библиотеку Python:
- tkinter — графический интерфейс
- os — работа с файлами
- subprocess — открытие папок
- platform — определение ОС
- datetime — работа с датой

### Лицензия
MIT