import os

from kivy.app import App
from kivy.logger import Logger
from kivy.lang import Builder

from kivyui.theme import UITheme


class UIApp(App, UITheme):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def load_all_kv_files(self, directory: str, *args) -> None:
        """
        Recursively load all kv files from a given directory.
        """

        for root, dirs, files in os.walk(directory):
            if "kivyui" in directory:
                Logger.critical(
                    "KivyUI: "
                    "Do not use the word 'kivyui' in the name of the "
                    "directory from where you download KV files"
                )
            if "venv" in root or ".buildozer" in root or os.path.join("kivyui") in root:
                continue
            for file in files:
                if (
                    os.path.splitext(file)[1] == ".kv"
                    and file != "style.kv"  # if use PyInstaller
                    and "__MACOS" not in root  # if use Mac OS
                ):
                    path_to_kv_file = os.path.join(root, file)
                    Builder.load_file(path_to_kv_file)
