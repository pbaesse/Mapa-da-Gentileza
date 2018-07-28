from flask import render_template, Blueprint


bp_errors = Blueprint('errors', __name__)


# construir templates personalizados para os erros.
# adicionar rotas para outros erros.

@bp_errors.errorhandler(404)
def not_found_error(error):
	return render_template("errors/error_404.html")


@bp_errors.errorhandler(500)
def internal_error(error):
    pass


def configure(app):
    app.register_blueprint(bp_errors)
