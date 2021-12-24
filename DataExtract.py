

import tekore as tk
import csv



client_id = 'a63c903d56cb4298a452cb21581e689d'
client_secret = '5568c44f7bdb4eee80997ff3ec482b98'

app_token = tk.request_client_token(client_id, client_secret)

spotify = tk.Spotify(app_token)

playlist = spotify.playlist('37i9dQZF1E8EOlPaxfU2Do',as_tracks=True)

playlist_sort = playlist['tracks']['items']

#track_id = playlist_sort[44]['track']['id']


with open('VCT.csv', 'a', newline='') as filename:
    headers = ['name', 'id', 'acousticenss', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness',
               'mode', 'speechiness', 'tempo', 'time_signature', 'type', 'uri', 'valence']

    thewriter = csv.DictWriter(filename, fieldnames=headers)
    thewriter.writeheader()
    for x in range(0,30):
        track_id = playlist_sort[x]['track']['id']
        track_info_name = spotify.track(track_id)
        track_info_features = spotify.track_audio_features(track_id)

        thewriter.writerow({'name': str(track_info_name.name), 'id':str(track_info_features.id), 'acousticenss':str(track_info_features.acousticness),
                            'danceability':str(track_info_features.danceability), 'duration_ms':str(track_info_features.duration_ms),
                            'energy':str(track_info_features.energy), 'instrumentalness':str(track_info_features.instrumentalness), 'key':str(track_info_features.key),
                            'liveness':str(track_info_features.liveness), 'loudness':str(track_info_features.loudness), 'mode':str(track_info_features.mode),
                            'speechiness':str(track_info_features.speechiness), 'tempo':str(track_info_features.tempo), 'time_signature':str(track_info_features.time_signature),
                            'type':str(track_info_features.type), 'uri':str(track_info_features.uri), 'valence':str(track_info_features.valence)})







#track_info = str(spotify.track_audio_features(track_id))
#print(track_info)



"""for i in playlist_sort:
    id_list = (i['track']['id'])
    print("SONG NUMBER {}".format(x))
    track_info_name = str(spotify.track(id_list))
    track_info_features = str(spotify.track_audio_features(id_list))
    splitted_list1 = track_info_name.split('=')
    splitted_list2 = track_info_features.split('=')
    print(splitted_list1[5])
    print()
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    x = x+1
    break
"""
"""with open('mycsv.csv', 'w', newline="") as f:

    thewriter = csv.writer(f)
    for i in playlist_sort:
        id_list = (i['track']['id'])
        track_info_name = str(spotify.track(id_list))
        track_info_features = str(spotify.track_audio_features(id_list))
        thewriter.writerow(track_info_name)
        thewriter.writerow(track_info_features)

"""









