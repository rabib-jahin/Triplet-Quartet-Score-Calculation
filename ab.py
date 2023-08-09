import subprocess
def check_duplicate_trees(trees):
    unique_trees = set()

    for tree in trees:
        if tree in unique_trees:
            return True
        unique_trees.add(tree)

    return False

unique_trees = []

while len(unique_trees) < 15:
    # Generate a gene tree using the command
    command = "./triplets.soda2103 genTree 3"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    generated_tree = output.decode().strip()

    # Check if the generated tree is unique
    if generated_tree not in unique_trees:
        unique_trees.append(generated_tree)
        print(generated_tree)
# Print the unique gene trees
unique_gene_trees = list(OrderedDict.fromkeys(unique_trees))

print(check_duplicate_trees(unique_gene_trees))
