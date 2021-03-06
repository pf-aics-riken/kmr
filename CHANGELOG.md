# CHANGELOG

The list is sketchy.

## 1.10 (2021-06-22)

- Nothing changed to KMR, but new utility programs are added in the
  "tool" directory
- Change the branch name "master" to "main"
- Flexdice was moved from "ex" to "tool"

## 1.10 (2020-11-16)

- 1.10 is a minor update
- Update Python code to Python3
- Add a support of Fugaku in configure, drop a K/FX10/FX100 support

## 1.9 (2018-08-27)

- 1.9 is a minor update
- Move GitHub repository from pf-aics-riken to riken-rccs
- Change the copyright holder name: RIKEN AICS to RIKEN R-CCS

## 1.8.1 (2016-04-25)

- Add ex/kmreprun.py, an example of simple shell command invoker
- Improve support of Mac OS X
- Several small bug fixes

## 1.8.0 (2015-12-25)

- Add a function tracing option for KMRViz, a KMR visualizer
- Add a simple scan function, kmr_scan_on_value()
- Add a load-leveling shuffle, kmr_shuffle_leveling_pair_count()
- Add a new kmr example, pagerank.c
- BUGFIX: kmr_match(), kmr_histogram_count_by_ranks(), kmr_find_key()

## 1.7.1 (2015-06-29)

- BUGFIX: kmr_take_one()
- BUGFIX: kmrrungenscript.py

## 1.7 (2015-06-22)

- Change license to BSD
- Strictly check options passed to kmr functions
- Add support for FOCUS supercomputer in kmrrungenscript.py
- Add Python API

## 1.6 (2015-04-01)

- Disable keep_open option in kmr functions except mapper functions
- Support no-fsync mode in Checkpoint/Restart
- Improve performance of KMRRUN when many input files are given
- BUGFIX: Checkpoint/Restart
- EXPERIMENTAL: Support selective mode that reduces IO overhead in
  Checkpoint/Restart

## 1.5 (2015-02-04)

- Reduce overhead of KMRRUN
- Temporal files for reducers are generated in subdirectories when
  using KMRRUN
- WORKAROUND: Abort on calling kmr_read_file_xxx with some MPI
  implementations
- WORKAROUND: Abort on calling kmr_map_processes and using KMRRUN
  with some Open MPI versions (1.6.3 - 1.8.1)

## 1.4 (2014-12-25)

- Resolved a scalability issue of KMRRUN and map functions that
  spawns child programs

## 1.3.2 (2014-11-07)

- Improve job script generator for KMRRUN

## 1.3.1 (2014-11-04)

- Add a word counting sample of KMRRUN
- BUGFIX: KMRRUN command line option parsing

## 1.3 (2014-09-17)

- Add a new function for affinity-aware file assignment

## 1.2 (2014-06-27)

- Support Checkpoint/Restart
- Add KMRRUN command that executes simple MapReduce workflow

## 1.1 (2013-09-20)

- 1.1 is a minor update

## 1.0 (2013-04-26)

- First release
