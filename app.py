import sys 
import os 


sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from view_gui.payment_gui import LiquidacionApp

if __name__ == "__main__":
    LiquidacionApp().run()