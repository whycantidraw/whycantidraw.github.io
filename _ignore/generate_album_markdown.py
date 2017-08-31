import os

imgPath = input('Relative Path? ')
countPath = input('Count Path? [Absolute 2048] ')
fileStub = input('Image stub? [albumname-yymmdd] ')
noImg = len(os.listdir(countPath))
image_title = input('Album Title? ')
weight = input('Sort Weight? ')
image_date = input('Date Taken? ')
location = input('Photo Location? ')
markdown = ['image_2048', 'image_1024', 'image_512', 'image_title', 'weight', 'image_date', 'location']
count = 1
imgPage = fileStub + '.html'

for count in range(len(os.listdir(countPath))):
    markdown_file = open(fileStub + '-' + str(count) + '.md', 'w')
    markdown[image_2048] = imgPath + '2048/' + fileStub + '-' + str(count) + '.jpg'
    markdown[image_1024] = imgPath + '1024/' + fileStub + '-' + str(count) + '.jpg'
    markdown[image_512] = imgPath + '512/' + fileStub + '-' + str(count) + '.jpg'
    markdown[image_title] = image_title
    markdown[weight] = weight
    markdown[image_date] = image_date
    markdown[location] = location
    markdown_file.write('image_2048: ' + markdown[image_2048] + '\n')
    markdown_file.write('image_1024: ' + markdown[image_1024] + '\n')
    markdown_file.write('image_512: ' + markdown[image_512] + '\n')
    markdown_file.write('image_title: ' + markdown[image_title] + '\n')
    markdown_file.write('weight: ' + markdown[weight] + '\n')
    markdown_file.write('image_date: ' + markdown[image_date] + '\n')
    markdown_file.write('location: ' + markdown[location] + '\n')
    markdown_file.write('featured: false' + '\n')
    markdown_file.write('isblog: false' + '\n')
    markdown_file.write('image_page: ' + imgPage + '\n')
    markdown_file.close()
