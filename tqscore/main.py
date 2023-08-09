import dendropy
import re
from utils import *
import sys

print(sys.argv[1])
with open ("../inputs/unrooted.txt","r") as file:

    tree_str =file.read()


elements = search(tree_str)

elements = [element for element in elements if element.isalnum()]
elements=elements[1:]
n=len(elements)-3



tree = dendropy.Tree.get(
        data=tree_str,
        schema="newick")

# print("Before:")
# print(tree.as_string(schema='newick'))
# #print(tree.as_ascii_plot())
count=1
for elem in (elements):
    mrca = tree.mrca(taxon_labels=[elem])
    tree.reroot_at_edge(mrca.edge, update_bipartitions=False)

    output_filename = f"tree{count}.txt"  # Generate a unique filename based on the element
    with open(f"../{sys.argv[1]}/"+output_filename, 'w') as file:
        file.write(tree.as_string(schema='newick')[5:])
        # file.write(tree.as_ascii_plot())
    count+=1
# print(tree.as_ascii_plot())
items=extract_items(tree_str)
# print(items)
for i in range(n):
    texas=search(items[i])
    
    tree = dendropy.Tree.get(
        data=tree_str,
        schema="newick")

    mrca = tree.mrca(taxon_labels= texas)
    tree.reroot_at_edge(mrca.edge, update_bipartitions=False)
    output_filename = f"tree{count}.txt"  # Generate a unique filename based on the element
    with open(f"../{sys.argv[1]}/"+output_filename, 'w') as file:
        file.write(tree.as_string(schema='newick')[5:])
        # file.write(tree.as_ascii_plot())
    count+=1


