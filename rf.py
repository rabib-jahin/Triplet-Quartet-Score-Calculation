from ete3 import Tree
t1 = Tree('(((a,b),c), ((e, f), g));')
t2 = Tree('(((a,c),b), ((e, f), g));')
rf,max_rf,common_leaves,parts_t1,parts_t2 = t1.robinson_foulds(t2)

print("RF distance is %s over a total of %s" %(rf, max_rf))

