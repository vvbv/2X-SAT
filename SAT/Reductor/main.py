#!/usr/bin/python3.7

import sys
import glob
import getopt
import ntpath
from datetime import datetime
from TwoXSAT import TwoXSAT
from tools import parseFile, exportToDimacs


def showHelp(odir, idir, verb):
    print(
        "main.py -x <X-SAT, [>= 3]> "
        "-d <input dir [default = '" + idir + "']> "
        "-o <output dir [default = '" + odir + "']> "
        "-v <verbose [default = '" + 'True' if verb else 'False' + "']>")
    sys.exit(2)


def printLog(msg):
    print("=> " + str(datetime.now()) + " >>> " + msg)


def main(argv):

    opts = None
    xsat = None
    verb = False
    odir = 'X-SAT'
    idir = '../InstanciasSAT'

    try:
        opts, args = getopt.getopt(argv, "hx:i:o:v:", ["xsat=", "idir=", 'odir=', 'verbose='])
    except getopt.GetoptError:
        showHelp(odir, idir, verb)

    for opt, arg in opts:
        if opt == '-h':
            showHelp(odir, idir, verb)
        elif opt in ("-x", "--xsat"):

            try:
                xsat = int(arg)
            except ValueError:
                showHelp(odir, idir, verb)

            if xsat < 3:
                showHelp(odir, idir, verb)

        elif opt in ("-d", "--idir"):
            idir = arg
        elif opt in ("-o", "--odir"):
            odir = arg
        elif opt in ("-v", "--verbose"):
            verb = True if arg.lower() == 'true' else False

    if xsat:

        printLog("Staring [ SAT to " + str(xsat) + "-SAT ].")

        files = glob.glob(idir + "/*.cnf")
        countFiles = files.__len__()

        printLog("Number of files to convert: " + str(countFiles) + ".")

        i = 1
        for file in files:
            filename = ntpath.basename(file)

            sat = parseFile(file)
            twoXSAT = TwoXSAT()
            result = twoXSAT.toXSAT(sat, xsat)
            resultDimacs = exportToDimacs(result)

            outFilename = filename.replace(".cnf", "-" + str(xsat) + "-SAT" + ".cnf")

            f = open("../X-SAT/" + outFilename, "w")
            f.write(resultDimacs)
            f.close()

            printLog("[ " + str(i) + " / " + str(countFiles) + " ] - " + filename + " → " + outFilename + " ✅.")

            i += 1

            if verb:
                print(resultDimacs)


if __name__ == '__main__':
    main(sys.argv[1:])

