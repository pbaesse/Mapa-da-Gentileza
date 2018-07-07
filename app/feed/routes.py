from flask import render_template
from app.feed import bp_feed
from app.feed.forms import NewKindnessForm


@bp_feed.route("/new_kindness", methods=['GET', 'POST'])
def new_kindness():
	pass




