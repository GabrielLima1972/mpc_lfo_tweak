# MPC lfo tweak workaround

## Purpose
As of the moment of this writing (july 2023), there is a bug in the Akai Force software
(and possibly on MPC One/Live/Live II/X too), where, if one saves projects using keygroup instruments
which have LFO parameters set, when afterwards reloading said projects,
an awful wobble can be heard on said keygroup instrument tracks.

Most keygroup instruments expansions do not have this problem, as they do not have any LFO parameters set,
BUT there are a few that do. At least, this has been noted in a few F9 MPC expansions.

One way to workaround this, is to, in the project, manually reset the LFO parameters
of all the keygroups in the affected keygroup instruments, before saving the project. 
But this is quite tedious to do.

So as a small workaround, this project consists of a small Python script, which, when executed, 
resets the LFO parameters of keygroup instruments in the MPC expansions directly.

This way, when one loads the keygroup instruments from said expansions into a project,
and afterwards save the project, one should not have any problems afterwards when loading said project again.

## Disclaimer

The Python script in this project may or may not work at all, and may possibly mess things up.
Try it out ONLY on a directory containing keygroup instruments IF you have a backup of said directory.
So, use it at your own risk.

## The Python script (mpc_lfo_tweak.py)
This project consists of a Python script (mpc_lfo_tweak.py), 
which given the path to an existing directory structure, will look for 
MPC keygroup instruments (.xpm files) in said directory (and subdirectories), and for each such file, 
either:

1. CLEAN the values of the lfo parameters ("LfoPitch", "LfoCutoff", "LfoVolume", "LfoPan") to zero, 
overwriting the .xpm files, and creating backup copies (.xpm.backup) of the modified files, or
2. RESTORE the previous values of the lfo parameters of said files, by deleting the modified .xpm files, and then restoring them from the backup copies (the .xpm.backup files).

This script must be downloaded, 
and executed from a command line terminal capable of executing Python 3.9 (or later) scripts,
and receives two arguments:
1. the path to the directory structure to work with
2. the execution mode of the script, which is either CLEAN_LFOS or RESTORE_LFOS.


## Examples

How to CLEAN the LFO values (using CLEAN_LFOS mode):

    python mpc_lfo_tweak.py "/Users/foo/Downloads/F9 Origins House Standalone" CLEAN_LFOS

How to RESTORE the original LFO values (using RESTORE_LFOS mode):

    python mpc_lfo_tweak.py "/Users/foo/Downloads/F9 Origins House Standalone" RESTORE_LFOS

