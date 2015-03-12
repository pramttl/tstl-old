tstl: A template scripting testing language
===========================================

TSTL is a langauge that greatly simplifies testing a system using multiple testing approaches and generating a test harness quickly.
It simplifies the definition of system under test.

TSTL is based on the research done by Dr. Alex Groce [1] and Jervis Pinto. School of Electrical Engineering and Computer Science, Oregon State University. The origial code can be found here: [harness-maker](https://code.google.com/p/harness-maker/). TSTL was taught in `CS562 Applied Softwre Engineering` Winter 2015 (at Oregon State University). There is not much documentation yet but that should change soon. :)

The current repository packages the original code into a python package so that it can be installed easily and used conveniently by the name `tstl`

`harnessmaker.py` is renamed as `tstl` and once package is installed there is no need to write `python harnessmaker.py`.
You can simply use `tstl` instead.


[1] http://eecs.oregonstate.edu/people/groce-alex

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
