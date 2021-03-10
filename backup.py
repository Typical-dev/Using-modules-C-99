import os
import shutil
source = input("Enter The Directory To be Backed Up:")
destination = input("Enter The Destination To Backup To:")
source = source + "/"
destination = destination + "/"
list_of_files = os.listdir(source)
for f in list_of_files:
    source1 = source + f
    shutil.copy(source1, destination)

