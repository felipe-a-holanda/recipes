from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "RecipeBook"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from RecipeBook.views import recipes
    app.register_blueprint(recipes)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
