import math
import random

# input1 = persen
# input2 = nama file
# input4 = file training
# input5 = file testing

class divider:
	# constructor
    def __init__(self, input1, input2, input4, input5):
        self.input1 = input1
        try:
        	self.input2 = open(input2, 'r')
        	self.fileTraining = open(input4, 'w')
        	self.fileTesting = open(input5, 'w')
        except:
        	print "error : File "+input2+" not found\n[-] Exit\n"
        	exit(1)
        self.count = 0
        self.tempArr = []
        
		
    def read(self):
		for line in self.input2:
			if line.strip() == "@data":
				self.count += 1
				self.fileTraining.write(line)
				self.fileTesting.write(line)
	
			elif self.count == 0:
				self.fileTraining.write(line)
				self.fileTesting.write(line)
			else :
				if self.count >= 1 and line.strip() != '':
					self.tempArr.append(line.strip())
					self.count += 1
		
		self.write()
		
    def write(self):
        countTemp = self.count
        for item in range(0, int(math.floor((float(self.input1) / 100) * (countTemp-1)))):
        	ran = random.randint(0, len(self.tempArr) - 1)
        	self.fileTraining.write(self.tempArr[ran] + "\n")
        	self.tempArr.pop(ran)
        
        for item in self.tempArr:
        	self.fileTesting.write(item + "\n")
        	
        self.clean()
    
    # cleaning up memory  
    def clean(self):
    	for k in range(0, len(self.tempArr)):
    		self.tempArr.pop(0)
    	
    	self.input2.close()
    	self.fileTesting.close()
    	self.fileTraining.close()

	
		
if __name__ == '__main__':

    input1 = raw_input("berapa persen : ")
    input2 = raw_input("nama file : ")
    input4 = raw_input("file training : ")
    input5 = raw_input("file testing : ")

    run = divider(input1, input2, input4, input5)

    run.read()
    
    
