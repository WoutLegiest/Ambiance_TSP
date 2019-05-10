
# Ambiance - TSP Problem



# Running

Install the gurobi software from there [website](http://www.gurobi.com/#) inside a virtualenv, install also the mip packages.  

    $ python solver.py belgium-ambianve-24.tsp > solve_alt_001.txt 
    $ python parser.py solve_001.txt belgium-ambianve-24.tsp > tour.txt 