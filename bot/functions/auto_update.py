import subprocess
import sys
import os


def pull_latest_code():
    """Проверка обновлений и выполнение git pull с уже настроенного удалённого репозитория."""
    # Выполняем git pull с origin и основной ветки (например, main или master)
    result = subprocess.run(['git', 'pull', 'origin', 'main'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Проверяем результат выполнения команды
    if result.returncode == 0:
        output = result.stdout.decode('utf-8')
        if "Already up to date." in output:
            print("Обновлений нет.")
            return False
        else:
            print("Код обновлён.")
            return True
    else:
        print(f"Ошибка при обновлении кода: {result.stderr.decode('utf-8')}")
        return False


def restart_program():
    """Перезапуск программы."""
    print("Перезапуск программы...")
    python = sys.executable
    os.execl(python, python, *sys.argv)


if __name__ == "__main__":
    # Проверка обновлений при запуске
    if pull_latest_code():
        restart_program()

    # Основная логика программы
    print("Программа запущена.")
