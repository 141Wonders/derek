from flask import Flask, render_template
import vimeo, json
app = Flask(__name__)

client = vimeo.VimeoClient(
  token='00806089b46ed18e0b6655aff77bc3ac',
  key='9166539cbc5edc3a5ed3fb41a58fcc71b74776e1',
  secret='qG+peLO+2N6K5k3OiXgqIB6efu3stPkFWfb1ptpkSCCHHnXoU5GupGqeIgDlbgEJXznqEZZg3VZNl3gRXagGny+Rk9yOfjgDtmbYqoymt77CFF4Tquk1MxWS8RbSsHY+'
)

def decode_json(client):
	# Make the request to the server for the "/me" endpoint.
	about_me = client.get('/me/albums/7693012/videos', params={"fields": "name,link,pictures.sizes.link"})

	# Make sure we got back a successful response.
	assert about_me.status_code == 200

	# convert response to json object
	data_encoded = json.dumps(about_me.json())

	# decode the json encoded object
	data_decoded = json.loads(data_encoded)

	 # initialize video data as list of dictionaries
	video_data = data_decoded["data"]

	return video_data
	# returns a list of dictionaries, each dictionary represents a video's data

main_result = decode_json(client)

thumbnail_list =[]

for i in range(len(main_result)):

	filtered = main_result[i]['pictures']

	more_filter = filtered.get('sizes')

	tn = more_filter[-1]['link']

	thumbnail_list.append(tn)
	

@app.route('/')
def hello_world():
    return render_template('index.html', main_result=main_result, thumbnail_list=thumbnail_list)

@app.route('/campaign/')
def campaign():
	return render_template('generic.html')



if __name__ == '__main__':    
    app.run(debug=True)