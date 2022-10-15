# test-train split-labeler
import glob
import os

current_dir = 'darknet/'

# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
file_train = open('darknet/data/train.txt', 'w')
file_test = open('darknet/data/test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir + 'data/dataset/', "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
#
    if counter == index_test:
        counter = 1
        file_test.write("data/dataset" + "/" + title + '.jpg' + "\n")
    else:
        file_train.write("data/dataset" + "/" + title + '.jpg' + "\n")
        counter = counter + 1
