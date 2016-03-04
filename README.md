# Perceptron_SpamChecker

Download train and test data from : https://drive.google.com/open?id=0B52R7grj75McQlNRem4wbXRQUHc
In the downloaded archive you will find:
webspam wc normalized unigram.svm: This file contains info on 350000 web pages. Each webpage is a feature of length 254. The file contains info for each webpage, one per line. Each line has the following format label feature index1:feature val1 feature index2:feature val2 ...... . Label is +1/ ? 1. “feature index:feature val” format describes that the given feature index has the corresponding value. For instance if the line is [+1, 10:0.001 112:1.3], then it means the document has label +1, feature number 10 has value 0.001, feature number 112 has value 1.3 and all other features are 0.
