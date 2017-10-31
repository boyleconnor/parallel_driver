import subprocess
import csv


PROBLEM_SIZES = (200000, 400000, 800000, 1600000, 3200000, 6400000, 12800000)
NUM_THREADS = (2, 4, 8, 16)


output_file = open('output.csv', 'w')
output = csv.writer(output_file)
output.writerow(['']+[str(i) for i in PROBLEM_SIZES])


for num_threads in NUM_THREADS:
    row = [str(num_threads)]
    for problem_size in PROBLEM_SIZES:
        result = subprocess.run(['mpirun', '-np', str(num_threads), '--map-by', 'node', 'mergeSortMPI', str(problem_size)], stdout=subprocess.PIPE)
        row += [result.stdout.decode('utf-8').strip()]
    output.writerow(row)

output_file.close()
