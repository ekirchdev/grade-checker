from sys import platform

if platform == "linux" or platform == "linux2":
    def open_alert(title, message):
        """
        Does nothing to ensure the application is not crashing on Unix systems.
        """
        pass

elif platform == "win32":
    import ctypes

    def open_alert(title, message):
        """
        Open an alert-box in foreground.
        :param title: Title of alert box.
        :param message: Message of alert box.
        """
        ctypes.windll.user32.MessageBoxW(0, title, message, int(64) + 4096)
