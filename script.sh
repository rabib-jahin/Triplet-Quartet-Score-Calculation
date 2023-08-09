mkdir -p $1
cd tqscore
python3 main.py $1
cd ..
python3 calc.py $1 $2 