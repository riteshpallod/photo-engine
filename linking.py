import shelve

'''
gets a photo or a file i.e. name, location and adds it into a shelf
fetches it back
'''

class Linking:
    photo_shelf = shelve.open("photo_db.dat")
    counter = len(photo_shelf.keys())
    keys = photo_shelf.keys()
    pipeline = photo_shelf["pipeline"]

    def addToShelf(self, file_name, file_location):
        self.photo_shelf[str(len(self.photo_shelf.keys()))] = [file_name, file_location] #check needed
        
        #assuming that there is always going to be a piplline
        self.photo_shelf["pipeline"] += [len(self.photo_shelf.keys())-1] #[self.counter]
        print(self.counter)
        self.counter += 1

    def getPhotoFromShelf(self, key):
        if key not in self.keys:
            return
        return self.photo_shelf[str(key)]

    def create_pipeline(self):
        self.photo_shelf["pipeline"] = []

    def load_pipeline(self):
        return self.photo_shelf["pipeline"]

    def update_pipeline(self, new_pipe):
        self.photo_shelf["pipeline"] = new_pipe    

if __name__ == '__main__':
    link = Linking()
    #link.addToShelf("selfie.jpg", "/home/bandu")
    #link.addToShelf("marathon.jpg", "/home/ritesh")
    #link.addToShelf("cat.jpg", "/home/cats")
    #pipeline = link.load_pipeline()
    #pipeline = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    #link.update_pipeline(pipeline)
    pipeline = link.load_pipeline()
    for p in pipeline:
        print(p)
    print(link.getPhotoFromShelf("0"))
    print(link.getPhotoFromShelf("1"))
    print(link.getPhotoFromShelf("2"))
    print(link.keys)
    for k in link.keys:
        print(k)
                