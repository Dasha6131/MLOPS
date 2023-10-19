import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 fill_na.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage2", "train.csv")
os.makedirs(os.path.join("data", "stage2"), exist_ok=True)

def process_data(fd_in, fd_out):
    arr_age = []
    arr_education = []
    arr_sex = []
    arr_hours = []
    arr_salary = []

    for line in fd_in:
        line = line.rstrip('\n').split(',')
        arr_education.append(line[1])
        arr_sex.append(line[2])
        arr_hours.append(line[3])
        arr_salary.append(line[4])
        if line[0]:
            arr_age.append(float(line[0]))
        else:
            arr_age.append(0)

    s = sum(arr_age)

    for i in range(len(arr_age)):
        if arr_age[i] == 0:
            arr_age[i] = round(s / len(arr_age), 3)

    for p_age, p_education, p_sex, p_hours, p_salary in zip(arr_age, arr_education, arr_sex, arr_hours, arr_salary):
        fd_out.write("{},{},{},{}\n".format(p_age, p_education, p_sex, p_hours, p_salary))


with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)