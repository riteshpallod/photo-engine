import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

from collections import Counter
from collections import defaultdict
from io import StringIO

from matplotlib import pyplot as plt
from PIL import Image


sys.path.append("object_detection")
print('in extract.. current dir: ', os.getcwd())
from utils import label_map_util


def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)


def visualize_boxes_and_labels_on_image_array( boxes,
                                                classes,
                                                scores,
                                                category_index,
                                                min_score_thresh=.35,
                                                agnostic_mode=False):

    max_boxes_to_draw = 20
    tags = []
    for i in range(min(max_boxes_to_draw, boxes.shape[0])):
        if scores is None or scores[i] > min_score_thresh:
            #print("i am here!")
            if not agnostic_mode:
                if classes[i] in category_index.keys():
                    class_name = category_index[classes[i]]['name']
                else:
                    class_name = 'N/A'
                
                display_str = '{}: {}%'.format(
                    class_name,
                    int(100*scores[i]))  
            else:
                display_str = 'score: {}%'.format(int(100 * scores[i]))
            tags.append(class_name)
    return tags

def load_and_detect(TEST_IMAGE_PATHS):
    #loading model
    sys.path.append("..")

    NUM_CLASSES = 545 
    print("pwd", os.getcwd())
    
    PATH_TO_CKPT = 'object_detection/ssd_mobilenet_v1_coco_2017_11_17/frozen_inference_graph.pb'
    #PATH_TO_CKPT = 'object_detection/faster_rcnn_inception_resnet_v2_atrous_lowproposals_oid_2018_01_28/frozen_inference_graph.pb'
    PATH_TO_LABELS = os.path.join('object_detection/data', 'mscoco_label_map.pbtxt')

    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    #loading label map
    print('loading label map..')
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    print('loaded label map')
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    print('converting it to categories')
    category_index = label_map_util.create_category_index(categories)
    print('category index created')
    ALL_TAGS = []
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            for image_path in TEST_IMAGE_PATHS:
                print('image path: ', image_path)
                image = Image.open(image_path)
                # the array based representation of the image will be used later in order to prepare the
                # result image with boxes and labels on it.
                image_np = load_image_into_numpy_array(image)
                print('image loaded')
                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(image_np, axis=0)
                # Actual detection.
                print('doing actual detection .. ')
                (boxes, scores, classes, num) = sess.run(
                    [detection_boxes, detection_scores, detection_classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})        
                print('detection done ')    
                tags = visualize_boxes_and_labels_on_image_array(
                    np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores),
                    category_index)
                print('kachra done')
                print(tags)
                ALL_TAGS.append(tags)
    return ALL_TAGS
            

if __name__ == "__main__":
    print(sys.path)
    PATH_TO_TEST_IMAGES_DIR = 'test_images'
    TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image{}.jpg'.format(i)) for i in range(1, 7) ]

    tags = load_and_detect(TEST_IMAGE_PATHS)
    for tag in tags:
        print(tag)
