from linking import Linking

sys.path.append("..")
from object_detection import extract_tags

def add_images_to_shelve(img_paths):
    '''
    assuming we get a full 'location+img_name.ext'
    '''
    img = img_paths.split('/') 
    img_path, img_name = "/".join(img[:-1]), img[-1]
    