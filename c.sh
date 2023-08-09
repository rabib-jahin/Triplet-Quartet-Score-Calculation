#!/bin/bash

# Loop 7 times
for i in {1..30}
do
    # Execute the command and append the output to the text file
    ./triplets.soda2103 genTree 5 >> output.txt
    
    # Add a new line
    echo >> output.txt
done


