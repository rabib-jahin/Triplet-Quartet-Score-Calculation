import subprocess
import os
import sys
import dendropy
command = ['python3', 'compute_quartet_score.py']
folder_path = f"./{sys.argv[1]}"  # Replace with the actual folder path
folder_path2 = f"./{sys.argv[2]}"

# Get a list of all files in the folder
files = os.listdir(folder_path)
files2 = os.listdir(folder_path2)

# Print the file names
print(files2)

# Open the output file in append mode to avoid overwriting previous results
with open('out2.txt', 'w') as file:
    sys.stdout = file

    for i in range(len(files)):
        for j in range(len(files2)):
            file1 = files[i]
            file2 = files2[j]
            print("file1", file1)
            print()
            print("file2", file2)
            print()

            with open(f"./{sys.argv[1]}/" + file1, "r") as f1:
                print("tree1 :")
                print()
                s=f1.read()
                tree = dendropy.Tree.get(
                data=s,
                schema="newick")
                print(s)
                print(tree.as_ascii_plot())

            with open(f"./{sys.argv[2]}/" + file2, "r") as f2:
                print("tree2 :")
                print()
                s=f2.read()
                tree = dendropy.Tree.get(
                data=s,
                schema="newick")
                print(s)
                print(tree.as_ascii_plot())

            if (sys.argv[1] == sys.argv[2] and i == j):
                pass
            else:
                command = ['python3', 'compute_quartet_score.py', f"./{sys.argv[1]}/" + file1,
                           f"./{sys.argv[2]}/" + file2, '2']

                # Run the script with file arguments and capture the output
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()

                # Decode the bytes and print the output to the file
                stdout_str = stdout.decode('utf-8')
                print(stdout_str, file=file)

                # Decode the bytes and print the error messages to the file (if any)
                stderr_str = stderr.decode('utf-8')
                if stderr_str:
                    print(stderr_str, file=file)
