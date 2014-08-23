# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-22 15:59:58
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
k-Nearest Neighbor
分类器
"""


from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    print 'dataSet:', dataSet
    dataSetSize = dataSet.shape[0]
    print u'重复:', tile(inX, (dataSetSize, 1))
    print 'dataSetSize:', dataSetSize
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    print 'diffMat:', diffMat
    sqDiffMat = diffMat ** 2
    print 'sqDiffMat:', sqDiffMat
    sqDistances = sqDiffMat.sum(axis=1)
    print 'sqDistances:', sqDistances
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    print 'sortedDistIndicies:', sortedDistIndicies
    classCount = {}
    for i in range(k):
        votelabel = labels[sortedDistIndicies[i]]
        print 'votelabel:', votelabel, 'classCount.get(votelabel, 0):',
        classCount.get(votelabel, 0)
        classCount[votelabel] = classCount.get(votelabel, 0) + 1
        print 'classCount:', classCount
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1), reverse=True)
    print 'classCount.iteritems()', classCount.iteritems()
    print 'sortedClassCount', sortedClassCount
    return sortedClassCount[0][0]

if __name__ == '__main__':
    group, labels = createDataSet()
    print classify0([0, 0], group, labels, 3)
# This is the end
