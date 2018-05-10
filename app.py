from flask import *
from fetch_image import fetch_images_from_query
import os

app = Flask(__name__)

def copyPhotosToStatic(photo_locations):
	photo_names = []
	num = int(len(photo_locations)/4)
	if num == 0:
		num = 1
	for photo in photo_locations:
		cmd = "cp "+ photo + " static/images/"
		os.system(cmd)
		print(cmd)
		photo = photo.split("/")
		photo_names.append(photo[-1])

	photo_arrays = []
	i = 0
	print(num)
	num_col = 0
	while i < len(photo_names):
		n = i+num
		if n > len(photo_names):
			n = len(photo_names) 
		ar = photo_names[i:n]
		photo_arrays.append(ar)
		num_col += 1
		i += num
	while num_col < 4:
		num_col+= 1
		ar = []
		photo_arrays.append(ar)
	print(photo_arrays)
	return photo_arrays

@app.route('/')
def home():
	return render_template('header.html', show_results = False)


@app.route('/search', methods=['POST','GET'])
def imgsrch():
	query = request.form['query']
	photo_locations = fetch_images_from_query(query)
	photo_names = copyPhotosToStatic(photo_locations)
	return render_template('header.html', show_results = True, photo_names = photo_names)



if __name__ == '__main__':
	app.run()
