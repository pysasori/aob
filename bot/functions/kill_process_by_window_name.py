import psutil


def kill_process_by_window_name(window_name):
    for proc in psutil.process_iter(['pid', 'name']):
        print(proc.info['name'])
        if proc.info['name'] == window_name:
            proc.kill()


