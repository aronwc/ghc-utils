# ghc-utils
utilities for interacting with github classroom

## Installation

`pip install ghc-utils`

## Usage

### grades

First, create a file named `students.txt` containing each student's github id, one per line.

To download all grades for an assignment named `assignment-01` from an organization name `myorg` and save it to `grades.csv`:

`ghc-utils grades -u <your_githubid> -p <your_github_password> -o <myorg> -a assignment-01 -s students.txt -g grades.csv`

```
ghc-utils grades --help
Usage: ghc-utils grades [OPTIONS]

  Download all grades for an assignment.

Options:
  -u, --username TEXT           your github username  [required]
  -p, --password TEXT           your github password  [required]
  -o, --organization TEXT       github organization name, e.g., tulane-
                                cmps2200  [required]
  -a, --assignment-prefix TEXT  assignment name prefix, e.g., assignment-01
                                [required]
  -s, --student-file PATH       text file with one student github id per line
                                [required]
  -g, --grade-file PATH         output csv file  [required]
  --help                        Show this message and exit.
```
