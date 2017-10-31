import subprocess


PROBLEM_SIZE = (10000, 20000, 40000, 80000, 160000)
NUM_THREADS = (2, 4, 8, 16)
LOG_FILE_PATH = 'run.log'


log_file = open(LOG_FILE_PATH, 'a')


for num_threads in NUM_THREADS:
    for problem_size in PROBLEM_SIZES:
        log_file = open(LOG_FILE_PATH, 'a')
        subprocess.call(['mpirun', '-np', str(num_threads), 'mergeSortMPI', str(problem_size)], stdout=open(LOG_FILE_PATH, 'a'))
