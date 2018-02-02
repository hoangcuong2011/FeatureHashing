from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from sklearn.feature_extraction import FeatureHasher


def main():
	features_dev = []
	features_dev_hashing = []


	with open("train.features") as f:
		for line in f:
			line = line.strip()
			if(len(line)>0):
				listhashing = []
				array = []
				arr = line.split("\t")
				for i in range(22): #the maximum number of features I should add
					#7.0	3.0	2.33333333333	140	<s>	Interferons	140	<s>	Interferone	0	0	0	1	2	1	0.6	0.4	0.6	5	1	CD	CARD	140|<s>	140|Interferons	140|140	CD|CARD	140|<s>|140	140|Interferons|140	
					if i==0 or i==1 or i==2 or i==9 or i==10 or i==11 or i==12 or i==13 or i==14 or i==15 or i==16 or i==17 or i==18 or i==19:
						array.append(float(arr[i]))						
					else:
						listhashing.append(str(arr[i]))
				features_dev_hashing.append(listhashing)
				features_dev.append(array)

	h = FeatureHasher(n_features=22, input_type='string')
	f = h.transform(features_dev_hashing)
	arrayHashing = f.toarray()
	#print(arrayHashing[0])


	for i in range(len(features_dev_hashing)):
		for j in range(len(arrayHashing[i])):
			features_dev[i].append(arrayHashing[i][j])

	with open("train", 'w') as file:
		for i in range(len(features_dev)):
			for j in range(len(features_dev[i])):
				file.write(str(features_dev[i][j]))
				file.write(",")
			file.write("\n")
		file.close()	

	

if __name__== "__main__":
  main()

