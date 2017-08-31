import os

for i in range(len(os.listdir("T:\\WebDev\\folio\\jekyll\\img\\collections\\\dinosaurrr-170118\\2048"))):
    count = i + 1
    if count < 10:
        markdown_file = open('dinosaurrr-170118-0' + str(count) + '.md', 'w')
        markdown_file.write('---\n')
        markdown_file.write('image_2048: /img/collections/dinosaurrr-170118/2048/dinosaurrr-170118-0' + str(count) + '.jpg\n')
        markdown_file.write('image_1024: /img/collections/dinosaurrr-170118/1024/dinosaurrr-170118-0' + str(count) + '.jpg\n')
        markdown_file.write('image_512: /img/collections/dinosaurrr-170118/512/dinosaurrr-170118-0' + str(count) + '.jpg\n')
    else:
        markdown_file = open('dinosaurrr-170118-' + str(count) + '.md', 'w')
        markdown_file.write('---\n')
        markdown_file.write('image_2048: /img/collections/dinosaurrr-170118/2048/dinosaurrr-170118-' + str(count) + '.jpg\n')
        markdown_file.write('image_1024: /img/collections/dinosaurrr-170118/1024/dinosaurrr-170118-' + str(count) + '.jpg\n')
        markdown_file.write('image_512: /img/collections/dinosaurrr-170118/512/dinosaurrr-170118-' + str(count) + '.jpg\n')
    markdown_file.write('image_title: Dinosaur Jr.\n')
    markdown_file.write('weight: 1\n')
    markdown_file.write('image_date: 2017-01-18\n')
    markdown_file.write('location: Amplifier Capitol\n')
    markdown_file.write('featured: false\n')
    markdown_file.write('isblog: false\n')
    markdown_file.write('---\n')
    markdown_file.close()
