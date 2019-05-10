
# Ambiance - TSP Problem

> Based on the [Ambiance_TSP](https://github.com/Forceflow/Ambiance_TSP) repository from Jeroen Baert's Github. Problem description is taken from his original Ambiance_TSP repository.

# Problem description

In 1999, Belgian songsmith [Sam Gooris](https://nl.wikipedia.org/wiki/Sam_Gooris) rocked the charts with his dance hit [_Ambiance, Ambiance_](https://www.youtube.com/watch?v=EqdQyoAUQZ0).

During the [March 2019 edition](https://soundcloud.com/lieven-scheire/nerdland-maandoverzicht-maart-2019) of the [Nerdland Science Podcast](http://www.nerdland.be) ([listen at 39:08](https://soundcloud.com/lieven-scheire/nerdland-maandoverzicht-maart-2019#t=39:11)), whilst discussing the news that [amoeba had been successfully used in problem-solving](https://phys.org/news/2018-12-amoeba-approximate-solutions-np-hard-problem.html), we looked at the [lyrics](https://muzikum.eu/en/123-173-5017/sam-gooris/ambiance-lyrics.html) of this song. In his anthem, Mr. Gooris eloquently describes how he visits several Belgian villages and cities in order to engage in rhyming party-related activities. However, the order in which he visits these locations is far from optimal. [Bart Van Peer](https://twitter.com/zebbedeusje) posed the question: **_What if Mr. Gooris could rearrange his travel itinerary (and, subsequently, his lyrics) to allow for an optimal usage of his time and mileage?_**

This is a classic example of a [Traveling Salesman](https://en.wikipedia.org/wiki/Travelling_salesman_problem) problem, a well-known problem in Computer Sciences which is [NP-hard](https://en.wikipedia.org/wiki/NP-hardness), which means that the worst-case running time of any problem-solving technique will increase [superpolynomially](https://en.wikipedia.org/wiki/Time_complexity#Polynomial_time) with the number of cities. In this instance, Mr. Gooris visits 24 locations in the following order, derived from the lyrics:

```
Mal -> Ghent -> Leest -> Peer -> As -> Tielt -> Lot -> Puurs -> Lint -> Heist -> Reet -> Bree -> Schriek -> Geel -> Jeuk (*) -> Doel -> Duffel -> Sinaai -> Vorst -> Niel -> Mere (**) -> Gits -> Boom -> Haacht -> Mal
```

We name this problem TSP, a _Travelling Sam Problem_.

(*) There's some discussion regarding "Leut" or "Jeuk" and "Bere" and "Mere". I choose the latter in both cases as they sounded more alike to my hearing.

# Solution strategy

Using the format described in the TSPLIB 95, by Gerhard Reinelt, all the city's are listed in the files with the tsp extension. This optimization problem is solved using Mixed-Integer Linear Programming. The Python [MIP](https://pypi.org/project/mip/) package provided the tools to model and solve this TSP problem.     

# Running

Install the gurobi software from there [website](http://www.gurobi.com/#) inside a virtualenv, install also the mip packages. For this project the academic license of gurobi is used, as well as python 3.6.7. 

Run the following commands to generate a solution:

    $ python solver.py belgium-ambiance-24.tsp > output_files/solve_001.txt 
    $ python parser.py output_files/solve_001.txt belgium-ambiance-24.tsp > output_files/tour_001.txt 

# Solution

In the output_files folder you can find the output from the solver (solve_00*.txt) and the more useful ordered list of the city's (tour_00*.txt).
