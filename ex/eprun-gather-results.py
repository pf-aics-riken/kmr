#!/usr/bin/env python

# eprun-gather-results.py - It distributes and invokes shell commands
# on ranks.  See "eprun.py" for a simpler exmaple.  A process on
# rank=0 reads a file COMMANDLIST.TXT, which contains lines of a key
# and a shell command.  The shell command is invoked, which is assumed
# to create a file named same as the key.  Each result file is read
# and the values are gathered to a process on rank=0.  The results are
# currently assumed to be a single number, but it can be changed by
# redefining the result-reader function "read_result" defined here.

# USAGE: "mpiexec -n N python ./eprun-gather-results.py COMMANDLIST.TXT".

# For example, COMMANDLIST.TXT may contain commands one per line (note
# that "shut" command is a random number generator):
# dat0.txt shuf -i 0-99 -n 1 >dat0.txt
# dat1.txt shuf -i 0-99 -n 1 >dat1.txt
# dat2.txt shuf -i 0-99 -n 1 >dat2.txt
# ......

from mpi4py import MPI
import kmr4py
from optparse import OptionParser
from optparse import HelpFormatter
from optparse import IndentedHelpFormatter
import time
import sys
import re
from operator import itemgetter

kmr0 = kmr4py.KMR("world")
NPROCS = kmr0.nprocs
RANK = kmr0.rank

class NullHelpFormatter(HelpFormatter):
    """Suppress helps on except rank=0."""

    def __init__(self,
                 indent_increment=0,
                 max_help_position=24,
                 width=None,
                 short_first=0):
        HelpFormatter.__init__(
            self, indent_increment, max_help_position, width, short_first)

    def format_option(self, option):
        return ""

    def format_heading(self, heading):
        return ""

    def format_text(self, text):
        return ""

    def format_usage(self, usage):
        return ""

if (RANK == 0):
    options = OptionParser()
else:
    options = OptionParser(formatter=NullHelpFormatter())

options.add_option("-t", "--trace",
                   dest="trace", action="store_true", default=False,
                   help="prints traces of invoking commands to stderr")
options.add_option("-m", "--per-core",
                   dest="percore", action="store_true", default=False,
                   help="invokes commands per core")

def read_commands(arg):
    k00 = kmr0.make_kvs(value="cstring")
    if (RANK == 0):
        f = open(arg)
        lines = f.readlines()
        f.close()
        for line in lines:
            pair = line.split(" ", 1)
            assert len(pair) == 2, "Ill formatted comand list"
            k00.add(pair[0], "sh\0-c\0" + (pair[1]).rstrip())
    k00.add_kv_done()
    return k00

def identitymap((k, v), kvi, kvo, i, *_data):
    kvo.add(k, v)
    return 0

def read_result((key, command), kvi, kvo, i, *_data):
    """Reads a file named as KEY, which is geneated by an executed
    command, and puts the first field (a string) to a KVS."""
    f = open(key)
    lines = f.readlines()
    f.close()
    for i, line in zip(range(len(lines)), lines):
        resultfields = line.split(" ")
        kvo.add(key, resultfields[0].rstrip())
    return

## MAIN

(opts, args) = options.parse_args()

if (NPROCS == 1):
    sys.stderr.write("eprun needs more than one rank; abort.\n")
    sys.exit(1)

if (len(args) != 1):
    if (RANK == 0):
        sys.stderr.write("Usage: python eprun.py [options] input-file.\n")
    sys.exit(1)

if (opts.trace):
    kmr0.set_option("trace_map_ms", "1")
threading = (opts.percore)

sys.stdout.flush()
sys.stderr.flush()

k20 = read_commands(args[0])
k21 = k20.map_ms_commands(read_result, nothreading=(not threading),
                          separator_space=False, value="cstring")

k22 = k21.replicate(rank_zero=True)
if (RANK == 0):
    resultlist = kmr4py.listify(k22)
    valuelist = map(itemgetter(1), resultlist)
    print valuelist
k22.free()
kmr0.dismiss()

sys.stdout.flush()
sys.stderr.flush()
#time.sleep(1)
#if (RANK == 0):
#    print "eprun OK"
#sys.stdout.flush()
