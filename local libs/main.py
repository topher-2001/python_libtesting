###Imports the mylib module
#import mylib


###Imports the mylib module with a simplified name
#import mylib as ml


###imports the "find_index" function only allowing us to call it without needing the module name
###supports , such as "from mylib import find_index, test_string"
###note import still supports "as" eg "from mylib import find_index as fi"
###now you can call "fi" to call "find_index"
#from mylib import find_index


courses = ["Art", "Math", "English", "Computer Science"]

search = "Art"
index = find_index(courses, search)
print("index of " + search + " = " + str(index))
