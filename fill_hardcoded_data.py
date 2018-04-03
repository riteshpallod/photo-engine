import shelve

from linking import Linking
from analyse_tags import Tags

link = Linking()
link.addToShelf("actorsridinghorses.jpg", "/home/ritesh/Music")     #0 person, horses
link.addToShelf("selfie_withhuman.jpg", "/home/ritesh/Music")       #1 person, man
link.addToShelf("car.jpg", "/home/ritesh")                          #2 car
link.addToShelf("cats.jpg", "/home/ritesh/Documents")               #3 cat, horse, dog
link.addToShelf("selfie_withcat.jpg", "/home/ritesh/Videos")        #4 cat, person
link.addToShelf("motorcycel.jpg", "/home/ritesh/0be")               #5 motorcycle
link.addToShelf("cat1.jpg", "/home/catasdsa")                       #6 cat, car
link.addToShelf("humansanddogsandfoold andcat.jpg", "/home/bandu")  #7 human, person, dog, food
link.addToShelf("capandbat.jpg", "/home/af/ritesh")                 #8 cap, bat
link.addToShelf("cats1.jpg", "/home/ritesh/Documents")              #9 cat
link.addToShelf("catandme.jpg", "/home/Downloads")                  #10 cat, person
link.addToShelf("foodandcatandmead.jpg", "/home/ritesh/Desktop")    #11 food, cat, person
link.addToShelf("dogsnadcats1.jpg", "/home/Downloads")              #12 dog,cat


#print(link.getPhotoFromShelf(0))
#print(link.getPhotoFromShelf(1))
#print(link.getPhotoFromShelf(2))

tag = Tags()
#tag_link.setupHardcodedInfo()
#print(tag_link.getTagData(['car', 'cap']))  
#tag_link.setTagData('car',[9999999, 1, 2, 121411])
#print(tag_link.getTagData(['car', 'cap']))  

tag.setTagData('person', [0,1,4,7,10,11])
tag.setTagData('cat', [3,4,6,9,10,11,12])
tag.setTagData('dog', [3, 7,12])
tag.setTagData('horse', [1, 3])
tag.setTagData('motorcycle', [5])
tag.setTagData('car', [2, 6])
tag.setTagData('food', [7,11])
tag.setTagData('cap', [8])
tag.setTagData('bat', [8])
