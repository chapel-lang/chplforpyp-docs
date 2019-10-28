.. warning::
    This page was contributed in 2015 and is not being actively maintained.  Please refer to chapel-lang.org/docs instead.

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

We hypothesize that much can be achieved by treating Python/NumPy as a DSL and mapping array-operations into Chapel. However, at some point even these abstractions and mappings break down. This project would explore what to do when the abstractions fail.

Inspiration could be taken from work such as pyOpenCL[3]/pyCuda[4] that allow the user to take control within Python by representing a GPU-kernel function as a string with access to NumPy arrays.
A similar approach could be adopted where the user describes a "kernel-function" in Chapel operating on NumPy arrays.
An example of its use would be to take a compound array-expression exhibiting an excessive use of temporary arrays. The user would replace the array-expression and instead formulate it as a small snippet of Chapel code utilizing zipped iterators. One could also view it as "inlining Chapel code".

Another approach would be to map Python functions to Chapel. Python can be expanded through the use of modules[8], ctypes[9], and most conveniently through cython[7]. These approaches expand python modules and functions through a c-implementation.
The work would explore a similar approach but with the implementation done in Chapel. It would apply for situations where control is needed on a level exceeding kernel-functions in order to apply the parallelization needed. The motivation for this approach is to apply the Chapel code on the same data-structures as used within Python such that Python acts as the glue code for orchestration of computation and visualization. 
