import os

albumStub = input("Album Stub?\n> ")
countPath = "T:\\WebDev\\folio\\jekyll\\img\\collections\\" + albumStub + "\\2048"
collectionsPath = "/img/collections/"
imageTitle = input("Album Title?\n> ")
imageDate = input("Date? (YYYY-MM-DD)\n> ")
imageLocation = input("Location?\n> ")
isFeature = input("Featured Image?\n> ")
isHidden1 = input("Secondary Feature #1?\n> ")
isHidden2 = input("Secondary Feature #2?\n> ")

for i in range(len(os.listdir(countPath))):
    count = i + 1
    if count < 10:
        markdown_file = open(albumStub + '-0' + str(count) + '.md', 'w')
        markdown_file.write('---\n')
        markdown_file.write('image_2048: ' + collectionsPath + albumStub + '/2048/' + albumStub + '-0' + str(count) + '.jpg\n')
        markdown_file.write('image_1024: ' + collectionsPath + albumStub + '/1024/' + albumStub + '-0' + str(count) + '.jpg\n')
        markdown_file.write('image_512: ' + collectionsPath + albumStub + '/512/' + albumStub + '-0' + str(count) + '.jpg\n')
    else:
        markdown_file = open(albumStub + '-' + str(count) + '.md', 'w')
        markdown_file.write('---\n')
        markdown_file.write('image_2048: ' + collectionsPath + albumStub + '/2048/' + albumStub + '-' + str(count) + '.jpg\n')
        markdown_file.write('image_1024: ' + collectionsPath + albumStub + '/1024/' + albumStub + '-' + str(count) + '.jpg\n')
        markdown_file.write('image_512: ' + collectionsPath + albumStub + '/512/' + albumStub + '-' + str(count) + '.jpg\n')
    markdown_file.write('image_title: ' + imageTitle + '\n')
    markdown_file.write('weight: \n')
    markdown_file.write('image_date: ' + imageDate + '\n')
    markdown_file.write('location: ' + imageLocation + '\n')
    if count == int(isFeature):
        markdown_file.write('featured: true\n')
    elif count == int(isHidden1):
        markdown_file.write('featured: collapse\n')
    elif count == int(isHidden2):
        markdown_file.write('featured: collapse\n')
    else:
        markdown_file.write('featured: false\n')
    markdown_file.write('isblog: false\n')
    markdown_file.write('image_page: ' + albumStub + '.html\n')
    markdown_file.write('---\n')
    markdown_file.close()
