import requests

BASE = "http://127.0.0.1:5000/"

wishlists = [
    {"wishlist_id": 1, "user_id": "sofia", "book_id": "book1", "is_available": "Y"},
    {"wishlist_id": 2, "user_id": "sofia", "book_id": "book2", "is_available": "Y"},
    {"wishlist_id": 3, "user_id": "tim", "book_id": "book2", "is_available": "Y"},
    {"wishlist_id": 4, "user_id": "tim", "book_id": "book3", "is_available": "Y"}
]

wishlist_new = {"wishlist_id": 5, "user_id": "sofia", "book_id": "book111", "is_available": "Y"}

# update the stock is_available to N
wishlist_upd = {"wishlist_id": 1, "user_id": "sofia", "book_id": "book3", "is_available": "N"}

# test 1 - uncomment first time to create db and insert 4 rows
'''
response = requests.get(BASE + "/api/wishlist_populate")
print(response)

for i, w in enumerate(wishlists):
    response = requests.post(BASE + "/api/wishlist", json=wishlists[i])
    print(response)
'''

# test 2 - get all the wishlists
response = requests.get(BASE + "/api/wishlist")
print(response)

# test 3 - get a specific wishlist
response = requests.get(BASE + "/api/wishlist/1")
print(response)

# test 4 - update a specific wishlist
response = requests.put(BASE + "/api/wishlist/1", json=wishlist_upd)
print(response)

# test 5 - insert a wishlist using post
response = requests.post(BASE + "/api/wishlist", json=wishlist_new)
print(response)

# test 6 - delete a specific wishlist
response = requests.delete(BASE + "/api/wishlist/5", json=wishlist_upd)
print(response)
