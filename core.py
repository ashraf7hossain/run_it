from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import compiler_strategy
import threading
import time

class CoreInit():

    def __init__(self, file_path, compiler_name):
        self._chrome_options = Options()
        self._driver = None
        self._extension = file_path.split('.')[-1].strip().lower()
        self._file_path = file_path.strip()
        self._compiler = compiler_name.strip().lower()
        self._file_monitor = None  # Store a reference to the FileMonitorThread

    def run_it(self):
        self._driver = webdriver.Chrome(options=self._chrome_options)
        strategy = compiler_strategy.CompilerStrategy()
        if self._extension == 'dart':
            # other strategy is not possible
            strategy = compiler_strategy.Dartpad()
        else:
            match self._compiler:
                case 'programize':
                    strategy = compiler_strategy.Programize()
                case _:
                    strategy = compiler_strategy.Onecompiler()

        url = strategy.generate_url(self._extension)

        self._driver.get(url)

        self._file_monitor = FileMonitorThread(file_path=self._file_path, strategy=strategy, driver=self._driver)
        self._file_monitor.start()

    def quit_it(self):
        if self._file_monitor:
            self._file_monitor.stop()
            self._file_monitor.join()  # Wait for the thread to finish
        self._driver.quit()
    def __del__(self):
        print("Core init destoried ")

class FileMonitorThread(threading.Thread):
    def __init__(self, file_path, strategy, driver):
        super().__init__()
        self._file_path = file_path
        self._strategy = strategy
        self._driver = driver
        self._running = True  # Flag to control the thread's execution

    def stop(self):
        self._running = False

    def run(self):
        file_content = ""
        while self._running:
            try:
                with open(self._file_path, 'r') as f:
                    content = f.read()
                    if content != file_content:
                        file_content = content
                        js_code = self._strategy.js_code(file_content)
                        self._driver.execute_script(js_code)
            except Exception as e:
                print(f"Error reading file: {e}")
            time.sleep(1)
