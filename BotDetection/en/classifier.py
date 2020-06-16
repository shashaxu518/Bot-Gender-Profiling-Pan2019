#!/usr/bin/python3


from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.calibration import CalibratedClassifierCV


def SVM():
    return SVC(kernel='rbf', probability=True, random_state=0, gamma='auto')


def adaboost(clf):
    from sklearn.ensemble import AdaBoostClassifier
    return AdaBoostClassifier(clf, n_estimators=30, algorithm='SAMME.R', random_state=0, learning_rate=65)


def voting(features_train, labels_train):
    SVM = SVC(kernel='rbf', probability=True, gamma='auto', random_state=0)
    votingCLF = VotingClassifier(estimators=[('SV', SVC(kernel='rbf', probability=True, random_state=0, gamma='auto')),
                                             ('ADA', AdaBoostClassifier(SVM, n_estimators=30, algorithm='SAMME.R',
                                                                        random_state=0, learning_rate=65))],
                                 voting='soft',
                                 weights=[1, 1], n_jobs=-1)
    votingCLF = CalibratedClassifierCV(votingCLF)
    votingCLF.fit(features_train, labels_train)
    return votingCLF



def voting2(features_train, labels_train, clf):
    SVM = SVC(kernel='rbf', probability=True, gamma='auto', random_state=0)
    votingCLF = VotingClassifier(estimators=[('SV', SVC(kernel='rbf', probability=True, random_state=0, gamma='auto')),
                                             ('ADA', AdaBoostClassifier(SVM, n_estimators=30, algorithm='SAMME.R',
                                                                        random_state=0, learning_rate=65)),
                                             clf],
                                 voting='soft',
                                 weights=[1, 1, 1])
    #votingCLF = CalibratedClassifierCV(votingCLF)
    votingCLF.fit(features_train, labels_train)
    return votingCLF