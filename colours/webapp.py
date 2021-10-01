import json
import random
from functools import wraps
from flask import Flask, Response, send_file, send_from_directory

from colours.colour_types import Rgb, Hsl

webapp = Flask(__name__, static_folder=None)

def json_response(f):
    @wraps(f)
    def inner(*args, **kwargs):
        result = f(*args, **kwargs)
        return Response(json.dumps(result), mimetype="application/json")
    return inner


@webapp.route("/")
def index():
    return send_file("front_end/build/index.html")


@webapp.route("/static/<path:path>")
def static_dist(path):
    return send_from_directory("front_end/build/static", path)


@webapp.route("/api/get_colours")
@json_response
def get_colours():
    '''
    Returns json for a number of colours. Example format:

    {
        "colours": [
            {
                "type": "rgb",
                "data": {"red": 2, "green": 2, "blue": 2},
                "css": "rgb(2,2,2)"
            },
            ...
        ]
    }
    '''

    # this could be further customised by query params
    available_colours = [Rgb(), Hsl()]
    num_colours = 5

    response_colours = []
    for _ in range(num_colours):
        response_colours.append(random.choice(available_colours).generate_json())

    return {
        "colours": response_colours
    }