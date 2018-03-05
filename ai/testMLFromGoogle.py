# from https://www.youtube.com/watch?time_continue=412&v=cKxRvEZd3Mw
# exist two must popular libs: scikit-learn and TensorFlow
# in this example we using scikit-learn
# scikit-learn depend of numpy and scipy
# for install:
# pip install numpy scipy scikit-learn

from sklearn import tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]] # 1 = 'smooth'; 2 = 'bumpy'
labels = [0, 0, 1, 1] # 0 = 'apple', 1 = 'orange'
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print( clf.predict([[144, 0]]) )