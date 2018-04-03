import shelve

'''
gets a photo or a file i.e. name, location and adds it into a shelf
fetches it back
'''
class Linking:
    photo_shelf = shelve.open("photo_db.dat")
    counter = len(photo_shelf.keys())
    keys = photo_shelf.keys()
    
    def addToShelf(self, file_name, file_location):
        self.photo_shelf[str(self.counter)] = [file_name, file_location]
        print(self.counter)
        self.counter += 1

    def getPhotoFromShelf(self, key):
        if key not in self.keys:
            return
        return self.photo_shelf[str(key)]

if __name__ == '__main__':
    link = Linking()
    #link.addToShelf("selfie.jpg", "/home/bandu")
    #link.addToShelf("marathon.jpg", "/home/ritesh")
    #link.addToShelf("cat.jpg", "/home/cats")

    print(link.getPhotoFromShelf("0"))
    print(link.getPhotoFromShelf("1"))
    print(link.getPhotoFromShelf(2))
    print(link.keys)
                