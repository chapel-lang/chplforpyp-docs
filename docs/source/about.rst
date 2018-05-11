=================
Python and Chapel
=================

SciPy and its accompanying software stack[2] provides a powerful environment for scientific computing in Python. The fundamental building block of SciPy is the multidimensional arrays provided by NumPy[1]. NumPy expands Python by providing a means of doing array-oriented programming using array-notation with slicing and whole-array operations.

The high-level abstractions, however, fails the user in the quest for high performance. In which case the user must take control and choose between porting to another language or integrate with low-level APIs.

The following project ideas seek to cover some ground when choosing to port a Python/NumPy application to Chapel, or use Chapel as a backend for Python/NumPy both implicitly and explicitly.

Chapel for Python/NumPy Users
=============================

The output of this project is an introduction to the Chapel language and concepts from the perspective of a NumPy user. The introduction is written to answer the question "I am used to doing X in NumPy, how would I express X in Chapel?".


npbackend / Hidden Chapel
=========================

The strong suits of Python/NumPy are high-level abstractions, convenient array-notation and a rich environment/software stack. It would be interesting to explore how to treat NumPy as a DSL and map  array operations transparently to Chapel.

Thereby maintaining abstractions, environment, existing Python/NumPy sourcecode but somehow transparently delegating parallelization to Chapel. Using and possibly expanding upon the experiences gained from the previously described project and applying sensible default strategies for mapping to domains and locales. Strategies which would to a great extent rely on implicit data-parallelism of array operations.

The work can build upon experiences from our integration of Bohrium and NumPy and would involve factoring out the glue between NumPy and Bohrium into a self-contained component which could be retargeted to Chapel.

pyChapel
========

The pyChapel implementation is now deprecated in favor of an approach utilizing
Cython.  This is a work in progress effort, but should hopefully come online
shortly.
