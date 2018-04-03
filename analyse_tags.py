import shelve
'''
stores and fetches tags from dict
'''

class Tags:

    tags_shelf = shelve.open("tags_db.dat")
    keys = list(tags_shelf.keys())

    def setTagData(self, tag, data):
        if type(data) is not list:
            data = [data] 
        if tag in self.keys:
            self.tags_shelf[tag] += data #appending information
        else :
            self.keys.append(tag)
            self.tags_shelf[tag] = data #appending information
        print('tag updated :', tag, ": ",  self.tags_shelf[tag])
        #self.tags_shelf[tag] = list(set(self.tags_shelf[tag])) #for unique tags


    def getTagData(self, tags):
        tag_data = []
        for tag in tags:
            if tag in self.keys:
                tag_data.append(self.tags_shelf[tag])                
        
        return tag_data


    def setupHardcodedInfo(self):
        self.tags_shelf['boy'] = [1,2,4,6]
        self.tags_shelf['cara'] = [1,2,6,10]
        self.tags_shelf['cap'] = [2,4]

if __name__ == "__main__":
    tag_link = Tags()
    tag_link.setupHardcodedInfo()
    #print(tag_link.getTagData(['car', 'cap']))  
    tag_link.setTagData('car',[9999999, 1, 2, 121411])
    print(tag_link.getTagData(['car', 'cap']))        