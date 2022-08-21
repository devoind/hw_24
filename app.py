from function import *
from flask import Flask, request, jsonify, Response

app = Flask(__name__)


@app.route("/perform_query", methods=["POST"])
def perform_query():
    data: dict = request.json
    file_name: str = data["file_name"]
    if not os.path.exists(os.path.join(DATA_DIR, file_name)):
        raise BadRequest

    return jsonify(do_query(data))


if __name__ == "__main__":
    app.run()
