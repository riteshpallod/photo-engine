import shelve

class Tags:

    tags_shelf = shelve.open("tags_db.dat")
    
    def getTagData(self, tags):
        tag_data = []
        for tag in tags:
            tag_data.append(self.tags_shelf[tag])
        
        return tag_data
    
    def setupHardcodedInfo(self):
        self.tags_shelf['boy'] = [1,2,4,6]
        self.tags_shelf['car'] = [1,2,6,10]
        self.tags_shelf['cap'] = [2,4]

if __name__ == "__main__":
    tag_link = Tags()
    tag_link.setupHardcodedInfo()
    print(tag_link.getTagData(['car', 'cap']))        