from linking import Linking
from analyse_tags import Tags
import sys, os
import time

sys.path.append("..")
from object_detection import extract_tags

def add_images_to_shelve(img_path):
    '''
    assuming we get a full 'location+img_name.ext'
    '''
    img = img_path.split('/') 
    img_path, img_name = "/".join(img[:-1]), img[-1]

    #adding to shelve
    link = Linking()
    link.addToShelf(img_name, img_path)

def execute_pipeline():
    '''
    run od code on imgs from pipeline
    '''
    link = Linking()
    pipeline = link.load_pipeline()
    
    IMG_PATHS = []
    location_map = {}
    print("printing pipeline")
    print(pipeline)
    
    while len(pipeline) != 0:
        img_id = pipeline.pop()
        #get image path and name
        if img_id > 0: #check needed.
            img_name, img_path = link.getPhotoFromShelf(str(img_id))
            complete_img_path = img_path + "/" + img_name
            print("complete_img_path : ", complete_img_path)
            #add to img_paths
            IMG_PATHS.append(complete_img_path)
            location_map[complete_img_path] = img_id
        link.update_pipeline(pipeline) #just to be safe
    #execute od code
    start = time.time()
    tags = extract_tags.load_and_detect(IMG_PATHS)
    done = time.time() - start
    print("time :", done)

    tag_link = Tags()

    for tag_id in range(0, len(tags)):
        #retrive img_id
        img_id = location_map[IMG_PATHS[tag_id]]
        tag = tags[tag_id]
        for t in tag:
            tag_link.setTagData(t, [img_id])
    print("done")

if __name__ == "__main__":
    '''
    add_images_to_shelve("/home/ritesh/0be/Goa_NOKIA_6/IMG_20180219_143707.jpg")
    add_images_to_shelve("/home/ritesh/Desktop/percy/besy/IMG-20171008-WA0005.jpg")
    add_images_to_shelve("/home/ritesh/Desktop/percy/nokia-till15/Camera/IMG_20171106_081250.jpg")
    add_images_to_shelve("/home/ritesh/Desktop/percy/nokia-till15/Camera/IMG_20171107_221610.jpg")
    add_images_to_shelve("/home/ritesh/Desktop/percy/nokia-till15/Camera/IMG_20171107_204955.jpg")
    
    add_images_to_shelve("/home/ritesh/Desktop/Photo2/test_images/art.cellphonekids.gi.jpg")
    add_images_to_shelve("/home/ritesh/Desktop/Photo2/test_images/aff9ddd7f6abc4befa5e4317a5eee5e6.jpg")
    add_images_to_shelve("/home/ritesh/Desktop/Photo2/test_images/maxresdefault.jpg")
    add_images_to_shelve("/home/ritesh/Desktop/Photo2/test_images/cats_n_dogs.jpg")
    add_images_to_shelve("/home/ritesh/Desktop/Photo2/test_images/WhatsApp.jpeg")
    '''
    add_images_to_shelve("/home/ritesh/Documents/cat2.jpg")
    add_images_to_shelve("/home/ritesh/Documents/image2.jpg")
    add_images_to_shelve("/home/ritesh/Documents/carwithpersonanddog.jpeg")
    add_images_to_shelve("/home/ritesh/Documents/mananddof.jpg")
    add_images_to_shelve("/home/ritesh/Documents/image5.jpg")
    add_images_to_shelve("/home/ritesh/Documents/image3.jpg")
    add_images_to_shelve("/home/ritesh/Documents/image6.jpg")
    add_images_to_shelve("/home/ritesh/Documents/cake.jpg")
    add_images_to_shelve("/home/ritesh/Documents/mangiraffe.jpeg")
    add_images_to_shelve("/home/ritesh/Documents/cak2.jpg")
    add_images_to_shelve("/home/ritesh/Documents/car.jpg")
    add_images_to_shelve("/home/ritesh/Documents/caranddogandperson.jpeg")
    add_images_to_shelve("/home/ritesh/Documents/food.jpg")
    add_images_to_shelve("/home/ritesh/Documents/mankite.jpeg")
    add_images_to_shelve("/home/ritesh/Documents/womanumbrella.jpeg")
    add_images_to_shelve("/home/ritesh/Documents/cat1.jpg")
    add_images_to_shelve("/home/ritesh/Documents/cake3.jpg")
    add_images_to_shelve("/home/ritesh/Documents/image4.jpg")
    add_images_to_shelve("/home/ritesh/Documents/catanddogs.jpg")


    execute_pipeline()
    
