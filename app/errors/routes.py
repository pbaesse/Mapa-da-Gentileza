from app.errors import bp_errors
from flask import render_template


#construir templates personalizados para os erros.
#adicionar rotas para outros erros.

@bp_errors.errorhandler(404)
def not_found_error(error):
	pass


@bp_errors.errorhandler(500)
def internal_error(error):
	pass

