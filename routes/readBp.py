from flask import Blueprint, render_template
from ..extensions import db
from ..models.read import Read


readBp = Blueprint('readBp', __name__)

@readBp.route('/read')
def read_list():
    # db.create_all()
    print('oi')
    read_query = Read.query.all()
    return render_template('read.html', read = read_query)
    