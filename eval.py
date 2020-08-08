import numpy as np
import math
import random
from os import listdir, makedirs
from os.path import isfile, join, splitext, exists
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size': 13.5})
classes = ["MD", "RO"]

dialectLabels = {"MD": 0, "RO": 1}

def confusion_mat(YGold, YPredicted):
    numClasses = len(dialectLabels)
    C = np.zeros((numClasses, numClasses))
    for i in range(len(YGold)):
        C[dialectLabels[YGold[i][:2]],dialectLabels[YPredicted[i][:2]]] += 1
    return C

def eval():
    results = []
    
    goldPrefix = "./Test/"
    runsPrefix = "./Runs/"
    evalOutputPrefix = "./Eval_Results/"

    goldFileName = [f for f in listdir(goldPrefix) if isfile(join(goldPrefix, f)) and f[0] != '.' and f[0] != "_"]
    runFileNames = [f for f in listdir(runsPrefix) if isfile(join(runsPrefix, f)) and f[0] != '.' and f[0] != "_"]

    goldFile = open(join(goldPrefix, goldFileName[0]), 'r')
    goldLabels = goldFile.readlines()
    goldFile.close()

    for runFileName in runFileNames:
        print("===> Evaluating run: %s" % runFileName)
        runFile = open(join(runsPrefix, runFileName), 'r')
        runLabels = runFile.readlines()
        runFile.close()

        C = confusion_mat(goldLabels, runLabels)
        precision = np.diag(C) / np.sum(C, axis = 1)
        recall = np.diag(C) / np.sum(C, axis = 0)
        F1Scores = 2 * precision * recall / (precision + recall)
        macroF1 = np.mean(F1Scores)
        weightedF1 = np.sum(F1Scores * (np.sum(C, axis = 1) / np.sum(C)))
        accuracy = np.sum(np.diag(C)) / len(goldLabels)

        print("Macro-F1 score: %.6f" % macroF1)
        print("Weighted-F1 score: %.6f" % weightedF1)
        print("Accuracy (micro-F1 score): %.6f" % accuracy)

        results += [(runFileName[10:-4], runFileName[8:9], macroF1, weightedF1, accuracy)]
        saveRunResults(join(evalOutputPrefix, runFileName[:-4]), C, macroF1, weightedF1, accuracy)
        saveConfusionMatrixPlot(join(evalOutputPrefix, runFileName[:-4]), np.array(C, dtype=int), classes, normalize=False, title=("Confusion matrix for run %s on RDI" % (runFileName[8:9])))

    results.sort(key=lambda tup: -tup[2])
    saveOverallResults(join(evalOutputPrefix, "overall-ranking.txt"), results)

def saveRunResults(evalOutputFileName, C, macroF1, weightedF1, accuracy):
    outputStatsFile = open(evalOutputFileName + "-stats.txt", 'w')
    outputStatsFile.write("macro-F1\tweighted-F1\tmicro-F1 (accuracy)\n")
    outputStatsFile.write("%.6f\t%.6f\t%.6f" % (macroF1, weightedF1, accuracy))
    outputStatsFile.write("\n")
    outputStatsFile.close()

    outputConfusionMatFile = open(evalOutputFileName + "-confusion-mat.txt", 'w')
    for i in range(C.shape[0]):
        for j in range(C.shape[1]-1):
            outputConfusionMatFile.write("%d\t" % C[i][j])
        outputConfusionMatFile.write("%d\n" % C[i][-1])
    outputConfusionMatFile.close()

def saveOverallResults(evalOutputFileName, results):
    outputRankingFile = open(evalOutputFileName, 'w')
    outputRankingFile.write("rank\tteam\trun\tmacro-F1\tweighted-F1\tmicro-F1 (accuracy)\n")
    for i in range(len(results)):
        outputRankingFile.write("%d\t%s\t%s\t%.6f\t%.6f\t%.6f" % (i+1, results[i][0], results[i][1], results[i][2], results[i][3], results[i][4]))
        outputRankingFile.write("\n")
    outputRankingFile.close()

def saveConfusionMatrixPlot(evalOutputFileName, cm, classes, normalize=False, title=None, cmap=plt.cm.Blues):
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix'

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print("Confusion matrix, without normalization")

    fig = plt.figure()
    ax = plt.axes()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')
        
    # Rotate the tick labels and set their alignment.
    # plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
       for j in range(cm.shape[1]):
           ax.text(j, i, format(cm[i, j], fmt),
                   ha="center", va="center",
                   color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    plt.savefig(evalOutputFileName + "-confusion-mat.png", bbox_inches='tight')
    plt.savefig(evalOutputFileName + "-confusion-mat.pdf", bbox_inches='tight')

eval()
