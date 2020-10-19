#!/usr/bin/python3.7

import sys
import getopt
from TwoXSAT import TwoXSAT
from tools import parseFile, exportToDimacs


def showHelp(odir, idir, verb):
    print(
        "main.py -x <X-SAT, [>= 3]> "
        "-d <input dir [default = '" + idir + "']> "
        "-o <output dir [default = '" + odir + "']> "
        "-v <verbose [default = '" + 'True' if verb else 'False' + "']>")
    sys.exit(2)


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

        sat = parseFile(idir + '/test.cnf')
        twoXSAT = TwoXSAT()
        result = twoXSAT.toXSAT(sat, xsat)
        if verb:
            print(exportToDimacs(result))
            print(result)


if __name__ == '__main__':
    main(sys.argv[1:])

