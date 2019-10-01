How to use `test.py`:
`python test.py <TESTING_PROGRAM> <TEST_CASES>`

To disable stderr you can redirect this one to NUL, to save results to file - redirect stdout.

`python test.py __main__.py test_cases.txt 2>NUL`

`python test.py __main__.py test_cases.txt >output.txt 2>NUL`
