from PyQt5.QtWidgets import *
from PyQt5.uic import *
from numpy import *


def fact_prem(x, t):
    n = 0
    i = 2
    nb = 0
    while x != 1:
        if x % i == 0:
            nb = nb + 1
            x = x // i
        else:
            if nb != 0:
                t[n] = dict()
                t[n]["FP"] = i
                t[n]["PUIS"] = nb
                n = n + 1
                nb = 0
            i = i + 1
    t[n]["FP"] = i

    t[n]["PUIS"] = nb
    n = n + 1
    return n


def trouve(fp, T, n):
    i = 0
    while i < n and T[i]["FP"] != fp:
        i = i + 1
    if i < n:
        return T[i]["PUIS"]
    else:
        return -1


def trouve(fp, T, n):
    trouver = False
    for i in range(n):
        if T[i]["FP"] == fp:
            trouver = True
    return trouver


def poww(a, b):
    r = 1
    for i in range(b):
        r = r * a
    return r


def PGCD(a, b):
    na = fact_prem(a, ta)
    nb = fact_prem(b, tb)
    res = 1
    for i in range(na):
        min_r = 0
        for j in range(nb):
            if tb[j]["FP"] == ta[i]["FP"]:
                if tb[j]["PUIS"] < ta[i]["PUIS"]:
                    min_r = tb[j]["PUIS"]
                else:
                    min_r = ta[i]["PUIS"]
                res = res * poww(tb[j]["FP"], min_r)
    return res


def PPCM(a, b):
    na = fact_prem(a, ta)
    nb = fact_prem(b, tb)
    res = 1
    for i in range(na):
        min_r = 0
        for j in range(nb):
            if tb[j]["FP"] == ta[i]["FP"]:
                if tb[j]["PUIS"] > ta[i]["PUIS"]:
                    min_r = tb[j]["PUIS"]
                else:
                    min_r = ta[i]["PUIS"]
                res = res * poww(ta[i]["FP"], min_r)
    for i in range(na):
        if trouve(ta[i]["FP"], tb, nb) == False:
            res = res * poww(ta[i]["FP"], ta[i]["PUIS"])
    for i in range(nb):
        if trouve(tb[i]["FP"], ta, na) == False:
            res = res * poww(tb[i]["FP"], tb[i]["PUIS"])
    return res


def play():
    cha = fen.a.text()
    chb = fen.b.text()
    if cha == "" or chb == "":
        mess = QMessageBox.critical(fen, "alerte", "vous devez saisir les 2 entiers")
    else:
        a = int(cha)
        b = int(chb)
        if a > 0 and b <= 0:
            mess = QMessageBox.critical(fen, "alerte", "b doit etre positive")
            fen.b.setText("")
        elif a <= 0 and b > 0:
            mess = QMessageBox.critical(fen, "alerte", "a doit etre positive")
            fen.a.setText("")
        elif a <= 0 and b <= 0:
            mess = QMessageBox.critical(fen, "alerte", "a et b doivent etre positive")
            fen.a.setText("")
            fen.b.setText("")
        else:
            if fen.c.currentText() == "PGCD":
                ch = PGCD(int(a), int(b))
            else:
                ch = PPCM(int(a), int(b))
            fen.res.setText(str(ch))


ta = array([dict()] * 100)
tb = array([dict()] * 100)
app = QApplication([])
fen = loadUi("AR.ui")
fen.aff.clicked.connect(play)
fen.show()
app.exec_()
