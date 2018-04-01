# photo-engine
A tool for fetching photos as per the input query.


Input: Query
Output: Retrieved images

The website or web application provides two distinct operations.
1. Linking photos (link existing photos to our database)
2. Searching photos (input a query and the code will fetch images)

Operation 1.

The user adds the photos by browsing through a browsing window.

Once the user selects the photos, we create a mapping. We assign ids to images.
We also need the image name and its location.

So, a dictionary.
Example:
    photo_dict[1] = ["IMG20180321.jpg", "/home/ritesh/photos/camera"]



The code processes the image. A CNN or some variation of CNN detects objects, more like identifies them.
Example: person, cow, book, fruit. These objects are keys in our new dictionary. Lets call the objects tags.
The code manages a huge dictionary. Objects are keys. And the value for each key is an array of images.
Images are ids. 

Example:
    tag_dictionary["person"] = [1,4,11,14,67,2]
    tag_dictionary["car"] = [14,15,67,2,119,221]
    Images 1,4,11,14,67,2 have person(s)
    Images 13,15,67,2,119,221 have car(s)
    Images 14,67,2 have both.

That's operation 1.

Operation 2.

Now, there's a search box. User types a query. 
The code looks for tags in that query. 

Example: query = "man with three dogs"
         tags extracted = [man, dogs] (problem, will explain later)

So, the retreivaxl code will extract tags.
Then from our tag_dictionary will fetch the arrays associated with those tags. 

Example:
    tag_dictionary["man"] = [1,5,6,99,12,15,9]
    tag_dictionary["dog"] = [1,2,5,99,12,17,9,5,71,73]

    We have arrays of images. So, we just need to find the common ids from those arrays.
    1,5,99,12,9 have man and dog.

So, the code has image ids. Using photo_dict it gets the names and the image locations.
And the web application looks for those images in our file system and displays them.
    
