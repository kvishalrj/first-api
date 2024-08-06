from flask import Flask # type: ignore
from resources.item import blp as ItemBluePrint
from resources.user import blp as UserBluePrint
from flask_smorest import Api # type: ignore
from flask_jwt_extended import JWTManager # type: ignore


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Items Rest API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

app.config["JWT_SECRET_KEY"] = "149851650586615244878968700145410090380"

api = Api(app)
jwt = JWTManager(app)

api.register_blueprint(ItemBluePrint)
api.register_blueprint(UserBluePrint)