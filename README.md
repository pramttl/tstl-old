tstl: A template scripting testing language
===========================================

TSTL is a langauge that greatly simplifies testing a system using multiple testing approaches and generating a test harness quickly.
It simplifies the definition of system under test.

TSTL is based on the research done by [Dr. Alex Groce](http://eecs.oregonstate.edu/people/groce-alex) and Jervis Pinto. School of Electrical Engineering and Computer Science, Oregon State University. The origial code can be found here: [harness-maker](https://code.google.com/p/harness-maker/). TSTL was taught in `CS562 Applied Softwre Engineering` Winter 2015 (at Oregon State University). The current repository packages the original code into a python package so that it can be installed easily and used conveniently by the name `tstl`

There is not much documentation yet but that should change soon.

`harnessmaker.py` is renamed as `tstl` and once package is installed there is no need to write `python harnessmaker.py`.
You can simply use `tstl` instead.


Installation
------------


    git clone https://github.com/pramttl/tstl.git
    cd tstl
    python setup.py install
    # Might need to do a sudo on the last step if not using virtualenv


Usage
-----

    tstl -a <action_file_name>

This will generate a file called `sut.py` which is the System Under Test.

Correctly not much user documentation is available for TSTL. For details please refer to this [paper](http://www.cs.cmu.edu/~agroce/nfm15.pdf).


Developer Info
--------------

There are no developer docs yet which will hopefully change in future. TSTL package includes simple unit tests to test modules within `tstl/src/harnessmaker.py`, which is the main file that makes up most of the TSTL langauge. Once you clone the repository to run the tests do the following:

    python test/unit_tests.py

Writing tests for TSTL is currently work in progress. But we know that testing everything is important, even if it is testing the code for a langauge for testing.

