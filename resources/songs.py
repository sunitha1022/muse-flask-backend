import models
from flask import Blueprint, jsonify, request
# when we get the data from db...db doesnt have the keys
# it converts to dic
from playhouse.shortcuts import model_to_dict
# first argument is blueprints name
# second argument is it's import_name
song = Blueprint('songs', 'song')


@song.route('/', methods=["GET"])
def get_all_songs():
    # find the dogs and change each one to a dictionary into a new array
    try:
        songs = [model_to_dict(song) for song in models.Song.select()]
        print(songs)
        return jsonify(data=songs, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})


@song.route('/', methods=["POST"])
def create_songs():
    # see request payload anagolous to req.body in express
    payload = request.get_json()
    print(type(payload), 'payload')
    song = models.Song.create(**payload)
    # see the object
    print(song.__dict__)
    # Look at all the methods
    print(dir(song))
    # Change the model to a dict
    print(model_to_dict(song), 'model to dict')
    song_dict = model_to_dict(song)
    return jsonify(data=song_dict, status={"code": 201, "message": "Success"})
