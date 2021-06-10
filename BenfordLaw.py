import matplotlib.pyplot as plt
import re
import math

def BenfordLaw(Filename, FigFlag=False):
	index = [0]*9
	count = 0.0
	BenfordLaw = [math.log(1+(1/i), 10)*100 for i in range(1,10,1)]
	with open(Filename, 'r', encoding='utf-8') as f:
		for line in f:
			line = line.replace(',', '')
			match = re.findall(r'\d+', line)
			for item in match:
				number = item[0].lstrip('0')
				if number:
					index[int(number[0])-1] += 1
					count += 1

	if FigFlag:
		data = [i/count*100 for i in index]
		fig, ax = plt.subplots()
		plt.bar([i for i in range(1,10,1)], data, color = 'lightblue', label = "data")
		plt.plot([i for i in range(1,10,1)], [i for i in BenfordLaw], 'r-', label = "BenfordLaw")
		plt.legend()
		plt.xticks([i for i in range(1,10,1)])
		plt.xlabel('digit')
		plt.ylabel('count (%)')
		plt.title('Benford\'s Law: Total count={:.0f}'.format(count))
		plt.grid(True)
		plt.box(True)
		plt.show()
	
	return index, count


if __name__ =='__main__':
	index, count = BenfordLaw('text.txt', True)
