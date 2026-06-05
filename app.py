import sys 
import os 


sys.path.append("src")

from flask import Flask
from src.view.Web.liquidacion_routes import blueprint
 
app = Flask(__name__, template_folder="src/templates")
app.register_blueprint(blueprint)
 
if __name__ == "__main__":
    app.run(debug=True)