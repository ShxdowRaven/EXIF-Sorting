import exifread
import os
import sys

rootDirIn = sys.argv[1]
rootDirOut = sys.argv[2]
#yearFound = False
#monthFound = False
dayFound = False
vidsFound = False
noexifFound = False

#monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
picExts = ["jpg", "png", "jpeg"]
vidExts = ["mp4", "mov", "avi", "3gp", "wmv"]

for root, subdirList, fileList in os.walk(rootDirOut):
	for dname in subdirList: 
		if dname == "Videos":
			vidsFound = True
		if dname == "NoEXIF":
			noexifFound = True

if not vidsFound:
	os.mkdir(rootDirOut + "Videos")
if not noexifFound:
	os.mkdir(rootDirOut + "NoEXIF")

for root, subdirList, fileList in os.walk(rootDirIn):
	print("Found directory: %s" % root)
	for fname in fileList:
		print("File name: %s" % fname)
		for i in picExts:
			#print(".")
			if fname.split(".")[1][0:].lower() == i:
				#print("..")
				with open(rootDirIn + fname) as file:
					print("Opened file: %s" % rootDirIn + fname)
					tags = exifread.process_file(file)
					try:
						data = str(tags["EXIF DateTimeOriginal"])
						year = data[:4]
						month = data[5:7]
						day = data[8:10]
						hour = data[11:13]
						minute = data[14:16]
						second = data[17:19]
						dirName = year + "-" + month + "-" + day + "/"
						print(year + ":" + month + ":" + day + " | " + hour + ":" + minute + ":" + second)
					except:
						dirName = "NoEXIF/"
						#os.rename(rootDirIn + fname, rootDirOut + "NoEXIF/" + fname)

					#for root, subdirList, fileList in os.walk(rootDirOut):
						#for dname in subdirList: 
							#if dname == year:
								#yearFound = True
					#if yearFound == False:
						#os.mkdir(rootDirOut + year)

					#for root, subdirList, fileList in os.walk(rootDirOut + year):
						#for dname in subdirList: 
							#if dname == monthNames[int(month) - 1]:
								#monthFound = True
					#if monthFound == False:
						#os.mkdir(rootDirOut + year + "/" + monthNames[int(month) - 1])

					#for root, subdirList, fileList in os.walk(rootDirOut + year + "/" + monthNames[int(month) - 1]):
						#for dname in subdirList: 
							#if dname == day:
								#os.rename(rootDirIn + fname, rootDirOut + year + "/" + monthNames[int(month) - 1] + "/" + day + "/" + fname)
								#dayFound = True
					#if dayFound == False:
						#os.mkdir(rootDirOut + year + "/" + monthNames[int(month) - 1] + "/" + day)
						#os.rename(rootDirIn + fname, rootDirOut + year + "/" + monthNames[int(month) - 1] + "/" + day + "/" + fname)
					
					#yearFound = False
					#monthFound = False
					dayFound = False

					#print "walking through out for", dirName
					for root, subdirList, fileList in os.walk(rootDirOut):
						#print "Subdirlist", root, subdirList, fileList
						#print "dirName", dirName
						if dirName[:-1] in subdirList:
								print "Moving", dirName[:-1]
								os.rename(rootDirIn + fname, rootDirOut + dirName + fname)
								dayFound = True
						break
					if not dayFound:
						os.mkdir(rootDirOut + dirName)
						os.rename(rootDirIn + fname, rootDirOut + dirName + fname)

		for i in vidExts:
			if fname.split(".")[1][0:].lower() == i:
				os.rename(rootDirIn + fname, rootDirOut + "Videos/" + fname)