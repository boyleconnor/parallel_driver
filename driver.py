import subprocess
import csv
import os


PROBLEM_SIZES = (800000, 1600000, 1600000, 3200000, 6400000, 12800000, 25600000, 51200000, 102400000, 204800000, 409600000)
NUM_THREADS = (2, 4, 8, 16)
CMDS = {'mergeSortMPI': 'mergeSortMPI', 'oddEvenSort': 'mpi_odd_even'}


directory = os.path.basename(os.getcwd())
output_file = open('output.csv', 'w')
output = csv.writer(output_file)
output.writerow(['']+[str(i) for i in PROBLEM_SIZES])


def run_job(num_threads, problem_size):
    result, error = subprocess.Popen(['mpirun', '-np', str(num_threads), '--map-by', 'node', CMDS[directory], str(problem_size)], stdout=subprocess.PIPE).communicate()
    assert not error
    return result.decode('utf-8').strip()


for num_threads in NUM_THREADS:
    row = [str(num_threads)]
    for problem_size in PROBLEM_SIZES:
        result = run_job(num_threads, problem_size)
        row += [result]
        print("Finished problem size: %s threads: %s" % (problem_size, num_threads))
    output.writerow(row)

output_file.close()
