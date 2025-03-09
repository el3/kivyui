__app_name__ = "KivyUI"
__version__ = "0.0.1.dev"

from kivy.logger import Logger

from kivyui.config import ROOT

Logger.info(f"{__app_name__}: {__version__}")
Logger.info(f"{__app_name__}: Installed at {ROOT}")

import kivyui.factory_registers
