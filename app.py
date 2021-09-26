
# import connexion
from flask import  Flask
from swagger_ui import api_doc

app = Flask(__name__) #connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
# app.add_api('swagger.yml')

api_doc(app,config_path='swagger.yml',url_prefix='/api/doc')
# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
