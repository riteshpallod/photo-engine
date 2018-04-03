from analyse_tags import Tags
from linking import Linking
from query_process import return_tags_from_query

'''
processes query and returns image locations
'''

def fetch_images_according_to_ids(ids):
    linker = Linking()
    list_locations = []
    #print('debug : ', ids)
    for id in ids:
        img = linker.getPhotoFromShelf(str(id))
        if img != None:
            list_locations.append(img[1]+"/"+img[0])
    #print("debug: me jatoy")
    return list_locations

def fetch_common_ids_from_tags(tags):
    common_set = set(tags[0])
    for s in tags[1:]:
        common_set.intersection_update(s)
    #print("img shortlisted: ", list(common_set))
    return list(common_set)


if __name__ == "__main__":
    tag_obj = Tags()
    tags = return_tags_from_query("person with many cats")
    print("tags fetched: ", tags)
    tag_data = tag_obj.getTagData(tags)
    print("tag data fetched: ", tag_data)
    ids = fetch_common_ids_from_tags(tag_data)
    print("img shortlisted: ", ids)
    photo_locations = fetch_images_according_to_ids(ids)
    for photo in photo_locations:
        print(photo)
