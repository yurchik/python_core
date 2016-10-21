fw = open('example.txt', 'a')
fw.write('Some interesting text!\n')
fw.write('End of file!!!')
fw.close()

fr = open('example.txt', 'r')
fileText = fr.read()
fr.close()

print(fileText)