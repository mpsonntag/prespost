## Workshop outline

- start with how to test code
  - why is writing tests a good idea
    - be sure that results are the same after changes have been done
    - code usage documentation + example file for yourself and others
  - does not have to be fancy
  - run an analysis with known input and known outcome. every time the code changes. check the output if the results are still the same.

  - exercises + solutions
    - test table output
    - test image output
    - test figure output

- how to test
  - [P] pytest / [M] testsuite
    - how to install
    - how to write
    - where to save
    - how to run
  - resources
    - other python test frameworks
  - how to handle jupyter notebooks with tests

- what to do with long analysis times
  - use smallest possible input as test to reduce running time
  - try to split up code and test only the parts that have been changed
    -> code quality helps you do that!
  - use an existing tool e.g. like snakemake

- (debugging)

- code quality
  - how does this help
  - tools for matlab and python
  - new project vs existing project
  - pep8 / style guidelines
  - [P] pylint/pycodestyle / [M] checkcode
  - again - what about jupyter notebooks

- suggested workflow when developing including git


## Resources and linklist

### Python
- https://github.com/pycqa/pycodestyle/wiki/RelatedTools
- https://pylint.org/
- https://stackoverflow.com/questions/26126853/verifying-pep8-in-ipython-notebook-code
- https://stackoverflow.com/questions/50358327/using-pylint-in-ipython-jupyter-notebook
- https://www.blog.pythonlibrary.org/2018/10/16/testing-jupyter-notebooks/
- https://pypi.org/project/pytest-notebook/


### Matlab
- https://de.mathworks.com/matlabcentral/fileexchange/2529-matlab-programming-style-guidelines
- http://www.cs.cornell.edu/courses/cs321/2003fa/Matlab%20Coding%20Style.pdf
- https://de.mathworks.com/help/matlab/ref/checkcode.html
- https://de.mathworks.com/help/matlab/matlab-unit-test-framework.html
- https://github.com/bastibe/MatlabCodeAnalyzer

### snakemake
- https://doi.org/10.12688/f1000research.29032.1
