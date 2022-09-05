# References:
# https://www.youtube.com/watch?v=VqCdRT1tREg
# https://pypi.org/project/img2pdf/

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
paperSize = (img2pdf.mm_to_pt(279.4), img2pdf.mm_to_pt(215.9)) #Letter 11 x 8.5
pdfLayout = img2pdf.get_layout_fun(paperSize)
pdf = img2pdf.convert(listImage, layout_fun=pdfLayout)
file = open("convertedToPdf.pdf","wb")
file.write(pdf)
file.close()