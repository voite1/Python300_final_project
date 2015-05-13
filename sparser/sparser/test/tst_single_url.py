from sparser.urlsparser import parseurls
from sparser.pagesparser import parsepages
from sparser.sutil import clean
import pickle
import datetime

if __name__ == "__main__":
	lst = parseurls("https://news.google.com", 2, 8)
	print "URL's", len(lst)

	with open("urls.txt", "wb") as output:
		for i in lst:
			output.write(i + "\n")

	result = parsepages(lst, 8)
	print "Pages", len(result)

	my_dict = {}

	for dict_in_list in result:
		for i in dict_in_list:
			if i in my_dict:
				value = my_dict[i]
				my_dict[i] = (value + dict_in_list[i])
			else:
				my_dict[i] = dict_in_list[i]

	print "the", my_dict["the"]
	print "over", my_dict["over"]
	print "children", my_dict["children"]
	print "wife", my_dict["wife"]
	print "boeing", my_dict["boeing"]

	filename = datetime.date.today().strftime("%m-%d-%Y")
	filename = filename + ".dict.pickle"
        pickle.dump(my_dict, open(filename, "wb"))
