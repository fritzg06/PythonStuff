import img2pdf
import os
import json

# Parsing the list of images
list = os.listdir(".")
listImage = [x for x in list if x.endswith(".jpg")]
print(json.dumps(listImage, indent=4))
print("Total number of images to convert is", len(listImage))

# Exporting list of images to text file
textFile = open("listImages.log","w")
for i in listImage:
    textFile.write(i + "\n")
textFile.close()

# Export to PDF
pdf = img2pdf.convert(listImage)
file = open("convertedToPdf.pdf","wb")
file.write(pdf)
file.close()




