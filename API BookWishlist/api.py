from flask import Flask, make_response, jsonify, request
import database as db
import json

app = Flask(__name__)
dbfile = "wishlist.db"


@app.route('/api/wishlist_populate', methods=['GET'])
def db_populate():
    # db create for first time
    db.db_create()
    return make_response(jsonify({"message": "DB created and data inserted"}), 200)


@app.route('/api/wishlist', methods=['GET', 'POST'])
def api_wishlist():
    conn = db.create_connection(dbfile)
    if request.method == "GET":
        wishlists = db.get_all_wishlists(conn)
        if wishlists:
            return make_response(wishlists, 200)
        else:
            return make_response(wishlists, 404)  # 404 - not found
    elif request.method == 'POST':
        content = request.json
        # print(content)
        db.ins_wishlist(conn, content)
        return make_response(jsonify({"message": "Wishlist #{} inserted".format(content['wishlist_id'])}), 201)  # 201 - Created


@app.route('/api/wishlist/<wishlist_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_wishlist(wishlist_id):
    conn = db.create_connection(dbfile)
    if request.method == "GET":
        if db.check_wishlist(conn, wishlist_id) == 0:
            return make_response(jsonify({"message": "No data exists"}), 404)
        w_obj = db.get_wishlist(conn, wishlist_id)
        if w_obj is not None:
            return make_response(w_obj, 200)
        else:
            return make_response(jsonify({"message": "Error fetching data"}), 404)
    elif request.method == "PUT":  # update
        if db.check_wishlist(conn, wishlist_id) == 0:
            return make_response(jsonify({"message": "No data exists"}), 404)
        content = request.json
        db.upd_wishlist(conn, content)
        return make_response(jsonify({"message": "Wishlist #{} updated".format(content['wishlist_id'])}), 200)
    elif request.method == "DELETE":
        if db.check_wishlist(conn, wishlist_id) == 0:
            return make_response(jsonify({"message": "No data exists"}), 404)
        db.del_wishlist(conn, wishlist_id)
        return make_response(jsonify({"message": "Wishlist #{} deleted".format(wishlist_id)}), 200)


if __name__ == '__main__':
    app.run(debug=True)
