# NJS (Number Jumble Solver)

## Introduction

This is a Flask web app wrapper with a solver for 'number jumbles', a common math puzzle.

## Number Jumbles

Number jumbles are a math puzzle where you have 5 random numbers and have to create another number from those five numbers. You can use any number of operations.

For example, the number jumble with numbers 1, 2, 3, 4, 5 to reach 25 can be solved by `5 * (4 + 3 - 2 * 1)` or `5 + 4 * (3 + 2 * 1)`.

## Operations

There are many operations in this number jumble solver, some of which are not common in mathematics (and some which were invented solely for the purpose of number jumbles).

##### Plustorial

Sum of all positive numbers less than or equal than the operand (if the operand is positive) or the sum of all negative numbers greater than or equal to the operand (if the operand is negative.)

`5p! = 5 + 4 + 3 + 2 + 1 = 15`

##### Subtorial

Similar to the plustorial operation, but with subtraction.

`5s! = 5 - 4 - 3 - 2 - 1 = -5`
`(-5)s! = -5 - -4 - -3 - -2 - -1 = 5`

##### Double Factorials

Similar to regular factorials, but with every other number skipped from the original number.

`5!! = 5 * 3 * 1 = 15`
`8!! = 8 * 6 * 4 * 2 = 384`
`5p!! = 5 + 3 + 1 = 9`

## Deployment
The number jumble solver itself is just an imported module; the function used is contained inside of [numberjumble.py](https://github.com/ajzliu/njs/blob/master/numberjumble.py).

The web wrapper is a Flask web app designed to be deployed on Heroku. The requirements and server setup are specified in [requirements.txt](https://github.com/ajzliu/njs/blob/master/requirements.txt) and [Procfile](https://github.com/ajzliu/njs/blob/master/Procfile), respectively.

The application can be deployed by simply forking this repository and then deploying to Heroku.

By default, the username and password for the solver are both test, although this can be changed in app.py. This was not designed to be secure in access or design in anyway and should not be treated as such.

## License

All source code in this repository are distributed under the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this repository, you can obtain one [here](https://mozilla.org/MPL/2.0/).

For more information on the redistribution or modification of this code, you can read an abridged version [here](https://tldrlegal.com/license/mozilla-public-license-2.0-(mpl-2)) or [here](https://choosealicense.com/licenses/mpl-2.0/).