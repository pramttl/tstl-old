tstl: A template scripting testing language
===========================================

Based on the research by Dr. Alex Groce and Jervis Pinto. School of Electrical Engineering and Computer Science
Oregon State University. The origial code can be found here: [harness-maker](https://code.google.com/p/harness-maker/).
The current repository packages the original code into a python package so that it can be installed easily and used conveniently by the name `tstl`

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
