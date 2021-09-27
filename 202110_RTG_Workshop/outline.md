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
  - try to split up code and test only the parts that have been changed.

- (debugging)

- code quality
  - how does this help
  - tools for matlab and python
  - new project vs existing project
  - pep8 / style guidelines
  - [P] pylint/pycodestyle / [M] checkcode
  - again - what about jupyter notebooks

- suggested workflow when developing including git
