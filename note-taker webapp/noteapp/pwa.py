from flask import (
    Blueprint, make_response, send_from_directory
    )

bp = Blueprint('pwa', __name__, url_prefix='')

@bp.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')

@bp.route("/sw.js")
def service_worker():
    res = make_response(send_from_directory('static', 'sw.js'))
    res.headers['Cache-Control'] = 'no-cache'
    return res
