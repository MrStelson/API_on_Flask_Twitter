from json import loads
from flask import Flask, jsonify, request
from model.comment import Comment

from model.twit import twits, Twit, get_twit_by_id, get_comment_by_id


app = Flask(__name__)

@app.route('/twit', methods=["POST"])
def app_create_twit():
    twit_json = request.get_json()
    twit = Twit(twit_json['id'],twit_json['body'], twit_json['author'], [])
    twits.append(twit)
    return twit.to_dict()


@app.route("/twits", methods=["GET"])
def app_get_twits():
    return [twit.to_dict() for twit in twits]


@app.post("/get_twit_by_id")
def app_get_twit_by_id():
    twit_id = request.get_json()
    return [twit.to_dict() for twit in twits if twit.twit_id == twit_id['id']]


@app.post("/update_twit_by_id")
def app_update_twit_by_id():
    update_twit = request.get_json()
    twit = get_twit_by_id(update_twit['id'])
    twit.body = update_twit['body']
    twit.author = update_twit['author']
    return jsonify({"status": "success"})


@app.post('/twit/delete')
def app_twit_delete():
    twit_id = request.get_json()
    twit = get_twit_by_id(twit_id['id'])
    twits.remove(twit)
    return jsonify({"status": "success"})


@app.post('/add_comment')
def app_add_comment():
    comment_json = request.get_json()
    twit = get_twit_by_id(comment_json['twit_id'])
    twit.comments.append(Comment(comment_json['comment_id'], comment_json['body'], comment_json['author']))     
    return jsonify({"status": "success"})


@app.post('/del_comment')
def app_del_comment():
    twit_comment_id = request.get_json()
    twit = get_twit_by_id(twit_comment_id['twit_id'])
    twit.comments.remove(get_comment_by_id(twit_comment_id['comment_id'], twit))
    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
