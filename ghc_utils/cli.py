"""Console script for ghc_utils."""
import click
from collections import Counter
import csv
from github3 import login
import sys
import time
import traceback


@click.group()
def main(args=None):
    return 0


@main.command('grades')
@click.option('-u', '--username', required=True, help='your github username')
@click.option('-t', '--token', required=True, help='your github personal access token (https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token)')
@click.option('-o', '--organization', required=True, help='github organization name, e.g., tulane-cmps2200')
@click.option('-a', '--assignment-prefix', required=True, help='assignment name prefix, e.g., assignment-01')
@click.option('-s', '--student-file', required=True, type=click.Path(exists=True), help='text file with one student github id per line')
@click.option('-g', '--grade-file', required=True, type=click.Path(), help='output csv file')
def grades(username, token, organization, assignment_prefix, student_file, grade_file):
    """Download all grades for an assignment."""
    click.echo("getting grades")
    gh = login(username=username, password=token)
    student_file_name = click.format_filename(student_file)
    grade_file_name = click.format_filename(grade_file)
    grade_counts = Counter()
    with open(grade_file_name, 'w', newline='') as csvfile:        
        csvw = csv.writer(csvfile)
        csvw.writerow(['github_id', 'points', 'possible_points', 'run_url'])
        for student in open(student_file_name):
            student = student.strip()
            try:
                repo = gh.repository(organization, '%s-%s' % (assignment_prefix, student))
            except:
                print('cannot find repo for %s' % student)
                traceback.print_exc()
                csvw.writerow(((student, "0", "", 'n/a')))
                continue
            for commit in repo.commits():
                try:
                    run = next(commit.check_runs())
                    grade = run.output.text.split()[1].split('/')
                    numerator = int(grade[0])
                    denominator = int(grade[1])
                    csvw.writerow(((student, numerator, denominator, run.html_url)))
                    print('\t'.join((student, str(numerator), str(denominator), run.html_url)))
                    grade_counts.update([numerator])
                    break
                except:
                    # traceback.print_exc()
                    print('skipping commit without a run')
            time.sleep(.05)

    for grade, count in sorted(grade_counts.items()):
        print('%10s %s' % (grade, ''.join(['*'] * count)))
    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
