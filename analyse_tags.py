import shelve
'''
stores and fetches tags from dict
'''

class Tags:


    def setTagData(self, tag, data):
        tags_shelf = shelve.open("tags_db.dat")
        keys = list(tags_shelf.keys())
        
        if type(data) is not list:
            data = [data] 
        if tag in keys:
            tags_shelf[tag] += data #appending information
        else :
            keys.append(tag)
            tags_shelf[tag] = data #appending information
        print('tag updated :', tag, ": ",  tags_shelf[tag])
        #self.tags_shelf[tag] = list(set(self.tags_shelf[tag])) #for unique tags
        tags_shelf.close()

    def getTagData(self, tags):
        tags_shelf = shelve.open("tags_db.dat")
        keys = list(tags_shelf.keys())

        tag_data = []
        for tag in tags:
            if tag in keys:
                tag_data.append(tags_shelf[tag])                
        
        tags_shelf.close()
        return tag_data


if __name__ == "__main__":
    tag_link = Tags()
    #print(tag_link.getTagData(['car', 'cap']))  
    tag_link.setTagData('car',[9999999, 1, 2, 121411])
    print(tag_link.getTagData(['car', 'cap']))        