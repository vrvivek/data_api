
import connexion
from flask import  Flask, render_template

app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

application = app.app
