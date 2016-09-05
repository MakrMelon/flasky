from flask import Blueprint

main = Blueprint('main',__name__)

from . import views,errors
from ..models import Permission

#To inject new variables automatically
# into the context of a template, context processors exist in Flask.
@main.app_context_processor
def inject_permissions():
	return dict(Permission=Permission)