from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from sklearn.feature_extraction import FeatureHasher


def main():
	features_dev = []
	features_dev_hashing_source = []
	features_dev_hashing_target = []


	with open("test.features") as f:
		for line in f:
			line = line.strip()
			if(len(line)>0):
				listhashingsource = []
				listhashingtarget = []
				array = []
				arr = line.split("\t")
				for i in range(22): #the maximum number of features I should add
					#7.0	3.0	2.33333333333	140	<s>	Interferons	140	<s>	Interferone	0	0	0	1	2	1	0.6	0.4	0.6	5	1	CD	CARD	140|<s>	140|Interferons	140|140	CD|CARD	140|<s>|140	140|Interferons|140	
					if i==0 or i==1 or i==2 or i==9 or i==10 or i==11 or i==12 or i==13 or i==14 or i==15 or i==16 or i==17 or i==18 or i==19:
						array.append(float(arr[i]))						
					else:
						if i==3 or i==4 or i==5:
							listhashingtarget.append(str(arr[i]))
						if i==6 or i==7 or i==8:
							listhashingsource.append(str(arr[i]))

				features_dev_hashing_target.append(listhashingtarget)
				features_dev_hashing_source.append(listhashingsource)
				features_dev.append(array)
	print(features_dev_hashing_target[0])
	print(features_dev_hashing_source[0])
	h = FeatureHasher(n_features=40, input_type='string')
	f = h.transform(features_dev_hashing_target)
	arrayHashingTarget = f.toarray()

	h = FeatureHasher(n_features=40, input_type='string')
	f = h.transform(features_dev_hashing_source)
	arrayHashingSource = f.toarray()


	#print(arrayHashing[0])


	for i in range(len(features_dev)):
		for j in range(len(arrayHashingTarget[i])):
			features_dev[i].append(arrayHashingTarget[i][j])
		for j in range(len(arrayHashingSource[i])):
			features_dev[i].append(arrayHashingSource[i][j])

	with open("test", 'w') as file:
		for i in range(len(features_dev)):
			for j in range(len(features_dev[i])):
				file.write(str(features_dev[i][j]))
				file.write(",")
			file.write("\n")
		file.close()	

	

if __name__== "__main__":
  main()

