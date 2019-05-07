from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb+srv://admin:admin@c4e29-cluster-brpnb.mongodb.net/test?retryWrites=true"

# 1. Create connection
client = MongoClient(uri)

# 2. Get / Create database
first_db = client.first_database

# 3. Get / Create collection
first_coll = first_db["first_collection"]

# 4. Create document
first_document = {
  "game": "Dota",
  "description": "MOBA",
}

game_list = [
  {
    "game": "Pikachu",
    "description": "Always lost money",
  },
  {
    "game": "FO4",
    "description": "Football game",
  }, 
]

# 5. CREATE
# 5.1 Create one
# first_coll.insert_one(first_document)

# 5.2 Create many
# first_coll.insert_many(game_list)

# 6. READ
# 6.1 Read all
# all_games = first_coll.find()
# Lazy loading 

# for game in all_games:
#   print(game)

# 6.2 Read one
# pikachu_game = first_coll.find_one({'_id': ObjectId('5cc064b368a3ff17f48aaa62')})
# print(pikachu_game)

# 7. UPDATE
# pikachu_game = first_coll.find_one({'_id': ObjectId('5cc05e2f68a3ff2af42d2b74')})
# new_value = { "$set": { "game": "AUTO CHESS" } }
# first_coll.update_one(pikachu_game, new_value)
# print(pikachu_game)

# 8. DELETE
pikachu_game = first_coll.find_one({'_id': ObjectId('5cc05e2f68a3ff2af42d2b74')})
if pikachu_game is not None:
  first_coll.delete_one(pikachu_game)
else:
  print("Not Found")
