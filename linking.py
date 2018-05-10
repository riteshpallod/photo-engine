import shelve

'''
gets a photo or a file i.e. name, location and adds it into a shelf
fetches it back
'''

class Linking:


    def addToShelf(self, file_name, file_location):
        photo_shelf = shelve.open("photo_db.dat")
        counter = len(photo_shelf.keys())
        keys = photo_shelf.keys()
        pipeline = photo_shelf["pipeline"]
        
        photo_shelf[str(len(photo_shelf.keys()))] = [file_name, file_location] #check needed
        
        #assuming that there is always going to be a piplline
        photo_shelf["pipeline"] += [len(photo_shelf.keys())-1] #[self.counter]
        
        photo_shelf.close()
        

    def getPhotoFromShelf(self, key):
        photo_shelf = shelve.open("photo_db.dat")
        keys = photo_shelf.keys()
        
        if key not in keys:
            photo_shelf.close()
            return
        isko_bhej = photo_shelf[str(key)]
        photo_shelf.close()    
        return isko_bhej

        

    def create_pipeline(self):
        photo_shelf = shelve.open("photo_db.dat")
        photo_shelf["pipeline"] = []
        photo_shelf.close()    


    def load_pipeline(self):
        photo_shelf = shelve.open("photo_db.dat")
        isko_bhej = photo_shelf["pipeline"]
        photo_shelf.close()    

        return isko_bhej

    def update_pipeline(self, new_pipe):
        photo_shelf = shelve.open("photo_db.dat")
        photo_shelf["pipeline"] = new_pipe
        photo_shelf.close()        

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
                