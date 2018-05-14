#!/usr/bin/env python

"""Test all the .py files in the examples/ dir.

Each module should have its own test case.
"""

from __future__ import print_function

import os.path
import shlex
import subprocess
import sys
import unittest


class _PyTestCase(unittest.TestCase):
    """Helper class for testing .py scripts."""

    def runpy(self, py_file, stdin=None):
        """Run python script and return output.

        This is sort of like check_output, which was introduced in python 2.7.
        """
        cmd = [sys.executable]
        cmd += shlex.split(py_file)
        stdin_val = subprocess.PIPE if stdin else None
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, stdin=stdin_val)
        output, _ = p.communicate(input=stdin)
        return output


class PyToChplTests(_PyTestCase):

    def test_arrays_init(self):
        self.assertEqual(
            """[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
""",
            self.runpy('arrays.init.py'))

    def test_arrays_promo(self):
        self.assertEqual(
            """[1.         1.41421356 1.73205081 2.         2.23606798 2.44948974
 2.64575131 2.82842712 3.         3.16227766]
['3.0', '6.0', '9.0', '12.0', '15.0', '18.0', '21.0', '24.0', '27.0', '30.0']
['6.0', '12.0', '18.0', '24.0', '30.0', '36.0', '42.0', '48.0', '54.0', '60.0']
""",
            self.runpy('arrays.promo.py'))

    def test_arrays(self):
        self.assertEqual(
            """0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
(0,0) = 0.000000
(0,1) = 0.000000
(0,2) = 0.000000
(0,3) = 0.000000
(0,4) = 0.000000
(0,5) = 0.000000
(0,6) = 0.000000
(0,7) = 0.000000
(0,8) = 0.000000
(0,9) = 0.000000
(1,0) = 0.000000
(1,1) = 0.000000
(1,2) = 0.000000
(1,3) = 0.000000
(1,4) = 0.000000
(1,5) = 0.000000
(1,6) = 0.000000
(1,7) = 0.000000
(1,8) = 0.000000
(1,9) = 0.000000
(2,0) = 0.000000
(2,1) = 0.000000
(2,2) = 0.000000
(2,3) = 0.000000
(2,4) = 0.000000
(2,5) = 0.000000
(2,6) = 0.000000
(2,7) = 0.000000
(2,8) = 0.000000
(2,9) = 0.000000
(3,0) = 0.000000
(3,1) = 0.000000
(3,2) = 0.000000
(3,3) = 0.000000
(3,4) = 0.000000
(3,5) = 0.000000
(3,6) = 0.000000
(3,7) = 0.000000
(3,8) = 0.000000
(3,9) = 0.000000
(4,0) = 0.000000
(4,1) = 0.000000
(4,2) = 0.000000
(4,3) = 0.000000
(4,4) = 0.000000
(4,5) = 0.000000
(4,6) = 0.000000
(4,7) = 0.000000
(4,8) = 0.000000
(4,9) = 0.000000
(5,0) = 0.000000
(5,1) = 0.000000
(5,2) = 0.000000
(5,3) = 0.000000
(5,4) = 0.000000
(5,5) = 0.000000
(5,6) = 0.000000
(5,7) = 0.000000
(5,8) = 0.000000
(5,9) = 0.000000
(6,0) = 0.000000
(6,1) = 0.000000
(6,2) = 0.000000
(6,3) = 0.000000
(6,4) = 0.000000
(6,5) = 0.000000
(6,6) = 0.000000
(6,7) = 0.000000
(6,8) = 0.000000
(6,9) = 0.000000
(7,0) = 0.000000
(7,1) = 0.000000
(7,2) = 0.000000
(7,3) = 0.000000
(7,4) = 0.000000
(7,5) = 0.000000
(7,6) = 0.000000
(7,7) = 0.000000
(7,8) = 0.000000
(7,9) = 0.000000
(8,0) = 0.000000
(8,1) = 0.000000
(8,2) = 0.000000
(8,3) = 0.000000
(8,4) = 0.000000
(8,5) = 0.000000
(8,6) = 0.000000
(8,7) = 0.000000
(8,8) = 0.000000
(8,9) = 0.000000
(9,0) = 0.000000
(9,1) = 0.000000
(9,2) = 0.000000
(9,3) = 0.000000
(9,4) = 0.000000
(9,5) = 0.000000
(9,6) = 0.000000
(9,7) = 0.000000
(9,8) = 0.000000
(9,9) = 0.000000
""",
            self.runpy('arrays.py'))

    def test_arrays_reduc(self):
        self.assertEqual(
            """55.0
[ 1.  3.  6. 10. 15. 21. 28. 36. 45. 55.]
""",
            self.runpy('arrays.reduc.py'))

    def test_arrays_whole(self):
        """Check that 100 random lines are printed."""
        self.assertEqual(
            100, len(self.runpy('arrays_whole.py').splitlines()))
        # Also spot check the results when seeded with 173...
        seed_173_results = self.runpy(
            '-c "import numpy; numpy.random.seed(173); import arrays_whole"').splitlines()
        self.assertAlmostEqual(1.93667466205, eval(seed_173_results[0]))
        self.assertAlmostEqual(2.5402632511, eval(seed_173_results[42]))
        self.assertAlmostEqual(0.964120007336, eval(seed_173_results[-1]))

    def test_classes(self):
        self.assertEqual('Green\n', self.runpy('classes.py'))

    def test_comments(self):
        self.assertEqual('', self.runpy('comments.py'))

    def test_cond_if_green(self):
        self.assertEqual(
            """Which color is the traffic light?
You can cross the street now.
You can cross the street now.
You can cross the street now.
You can cross the street now.
""",
            self.runpy('cond.if.py', 'green\n'))

    def test_conf_if_red(self):
        self.assertEqual(
            """Which color is the traffic light?
Wait for the green light.
Do not cross!
""",
            self.runpy('cond.if.py', 'red\n'))

    def test_conf_if_yellow(self):
        self.assertEqual(
            """Which color is the traffic light?
Wait for the green light.
CAUTION!
CAUTION!
""",
            self.runpy('cond.if.py', 'yellow\n'))

    def test_cond_switch_green(self):
        self.assertEqual(
            """Which color is the traffic light?
You can cross the street now.
""",
            self.runpy('cond.switch.py', 'green\n'))

    def test_cond_switch_red(self):
        self.assertEqual(
            """Which color is the traffic light?
Do not cross!
""",
            self.runpy('cond.switch.py', 'red\n'))

    def test_cond_switch_yellow(self):
        self.assertEqual(
            """Which color is the traffic light?
CAUTION!
""",
            self.runpy('cond.switch.py', 'yellow\n'))

    def test_cond_switch_garbage(self):
        self.assertEqual(
            """Which color is the traffic light?
WARNING! Traffic-light is broken!
""",
            self.runpy('cond.switch.py', 'Hawt Garbage\n'))

    def test_console(self):
        self.assertEqual(
            """Hello, you.
Hello, you.
""",
            self.runpy('console.py'))

    def test_console_read__true_true(self):
        self.assertEqual(
            """The Answer to the ultimate question is?
That is True
What is the largest biological computer?
That is True
""",
            self.runpy('console.read.py', '42\nEarth\n'))

    def test_console_read__true_false(self):
        self.assertEqual(
            """The Answer to the ultimate question is?
That is True
What is the largest biological computer?
That is False
""",
            self.runpy('console.read.py', '42\nCray XC\n'))

    def test_console_read__false_true(self):
        self.assertEqual(
            """The Answer to the ultimate question is?
That is False
What is the largest biological computer?
That is True
""",
            self.runpy('console.read.py', '17\nEarth\n'))

    def test_console_read__false_false(self):
        self.assertEqual(
            """The Answer to the ultimate question is?
That is False
What is the largest biological computer?
That is False
""",
            self.runpy('console.read.py', '101010\nGoogel\n'))

    def test_dicts(self):
        self.assertEqual(
            """Key=0, Value=Green
Key=1, Value=Yellow
Key=2, Value=Red
""",
            self.runpy('dicts.py'))

    def test_division(self):
        self.assertEqual(
            """Result of 9.0 / 4 = 2.25
Result of 9 / 4.0 = 2.25
Result of 9 / 4 = 2
Result of 9.0 / 4.0 = 2.25
""",
            self.runpy('division.py'))

    def test_func_decl(self):
        import func_decl
        self.assertEqual('', self.runpy('func_decl.py'))
        self.assertEqual(10, func_decl.abs(10))
        self.assertEqual(10, func_decl.abs(-10))
        self.assertEqual(0, func_decl.abs(0))

    def test_hw(self):
        self.assertEqual('Hello, World!\n', self.runpy('hw.py'))

    def test_hw_main(self):
        self.assertEqual('Hello, World!\n', self.runpy('hw.main.py'))

    def test_literals(self):
        self.assertEqual('', self.runpy('literals.py'))
        import literals
        self.assertFalse(literals.bl)
        self.assertEqual(42, literals.ud)
        self.assertEqual(-42, literals.sd)
        self.assertEqual(42, literals.hd)
        self.assertEqual(42, literals.bd)
        self.assertEqual(42.0, literals.r)
        self.assertEqual('42', literals.s)
        self.assertEqual(1.0, literals.z.real)
        self.assertEqual(2.0, literals.z.imag)

    def test_loops_enumerate(self):
        self.assertEqual(
            """0 running
1 with
2 scissors
""",
            self.runpy('loops.enumerate.py'))

    def test_loops_for(self):
        self.assertEqual(
            """1
2
3
4
5
6
7
8
9
""",
            self.runpy('loops.for.py'))

    def test_loops_while(self):
        self.assertEqual(
            """1
2
3
4
5
6
7
8
9
10
1
2
3
4
5
6
7
8
9
10
""",
            self.runpy('loops.while.py'))

    def test_modules_import(self):
        self.assertEqual('', self.runpy('modules_import.py'))
        import modules_import
        self.assertEqual(modules_import.Random, modules_import.random.Random)

    def test_modules_main(self):
        self.assertEqual('', self.runpy('modules_main.py'))
        import modules_main
        self.assertEqual(None, modules_main.main())

    def test_numpy_random(self):
        self.assertEqual('', self.runpy('numpy_random.py'))

        import numpy
        numpy.random.seed(173)
        import numpy_random

        self.assertEqual(9, numpy_random.a.size)
        self.assertEqual((3, 3), numpy_random.a.shape)
        self.assertEqual(0.093257479552558031, numpy_random.a[0][0])
        self.assertEqual(0.60640382464326914, numpy_random.a[1][1])
        self.assertEqual(0.078458465901735885, numpy_random.a[2][2])

    def test_par_task_nosync(self):
        self.assertEqual('Hello, bob\n', self.runpy('par.task.nosync.py'))

    def test_par_task_pool(self):
        self.assertEqual('', self.runpy('-c "import par_task_pool; par_task_pool.do_work()"'))

    def test_par_task(self):
        self.assertEqual('Hello, bob\n', self.runpy('par.task.py'))

    def test_ranges_inf(self):
        self.assertEqual('', self.runpy('ranges_inf.py'))

    def test_ranges(self):
        self.assertEqual('', self.runpy('ranges.py'))
        import ranges
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], list(ranges.r1))
        self.assertEqual([], list(ranges.r2))

    def test_ranges_short(self):
        self.assertEqual('', self.runpy('ranges_short.py'))
        import ranges_short
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], list(ranges_short.ns))

    def test_ranges_skip(self):
        self.assertEqual('', self.runpy('ranges_skip.py'))
        import ranges_skip
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], list(ranges_skip.r1))
        self.assertEqual([1, 3, 5, 7, 9], list(ranges_skip.r2))
        self.assertEqual([9, 8, 7, 6, 5, 4, 3, 2, 1], list(ranges_skip.r3))
        self.assertEqual([9, 7, 5, 3, 1], list(ranges_skip.r4))

    def test_tuples(self):
        self.assertEqual(
            """coord = ('47.606165', '-122.332233')
Latitude = 47.606165 , Longitude = -122.332233
Latitude = 47.606165 , Longitude = -122.332233
""",
            self.runpy('tuples.py'))

    def test_vars_decl(self):
        self.assertEqual('', self.runpy('vars_decl.py'))
        import vars_decl
        self.assertEqual(42, vars_decl.answer)
        self.assertEqual(123.45, vars_decl.distance)
        self.assertEqual('Earth', vars_decl.computer)


if __name__ == '__main__':
    unittest.main()
