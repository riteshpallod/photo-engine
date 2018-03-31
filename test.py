import sys, os
import time

sys.path.append("..")
from object_detection import extract_tags


PATH_TO_TEST_IMAGES_DIR = os.getcwd() + '/test_images'
TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image{}.jpg'.format(i)) for i in range(3, 4) ]


start = time.time()
tags = extract_tags.load_and_detect(TEST_IMAGE_PATHS)
done = time.time() - start
print("time :", done)
for tag in tags:
    print(tag)