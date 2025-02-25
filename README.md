# CS470: Introduction to Artificial Intelligence - Spring 2025

# Installation

# Tutorial Links
- Tutorial 1: [1-1](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/tutorial_1/MLP_tutorial_1_1.ipynb/), [1-2](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/tutorial_1/MLP_tutorial_1_2.ipynb/), [1-3](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/tutorial_1/MLP_tutorial_1_3.ipynb/)
- [Tutorial 2](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/tutorial_2/RL_tutorial.ipynb/)
- [Tutorial 3](https://github.com/pidipidi/CS470_IAI_20025_Spring/blob/main/tutorial_3/README.md)

# Assignment Links
- [Assignment 1](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/assignment_1/mlp_problem.ipynb/)
- [Assignment 2-1](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/assignment_2/CNN_problem_1.ipynb/)
- [Assignment 2-2](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/assignment_2/CNN_problem_2.ipynb/)
- [Assignment 2-3](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/assignment_2/CNN_problem_3.ipynb/)
- [Assignment 3](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/assignment_3/CS470_Assignment3_problem.ipynb/)
- [Assignment 4](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/assignment_4/CS470_Assignment4_problem.ipynb/)
- [Assignment 5](https://github.com/pidipidi/CS470_IAI_20025_Spring/blob/main/assignment_5/src/py_astar_planner/src/py_astar_planner/astar.py)

# Assignment Solution Links (must be removed before distribution)
- [Assignment 1](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/assignment_1/mlp_solution.ipynb/)
- [Assignment 2-1](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/assignment_2/CNN_solution_1.ipynb/)
- [Assignment 2-2](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/assignment_2/CNN_solution_2.ipynb/)
- [Assignment 2-3](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/assignment_2/CNN_solution_3.ipynb/)
- [Assignment 3](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/assignment_3/CS470_Assignment3_solution.ipynb/)
- [Assignment 4](https://githubtocolab.com/pidipidi/CS470_IAI_20025_Spring/blob/main/assignment_4/CS470_Assignment_4_sol.ipynb/)
- [Assignment 5](assignment_5/README.md)

# Quiz
- [Tutorial Quiz 1](https://githubtocolab.com/pidipidi/CS470_IAI_2025_Spring/blob/main/tutorial_1/MLP_tutorial_quiz_quest.ipynb/)
- [Tutorial Quiz 2](https://githubtocolab.com/pidipidi/CS470_IAI_2025_Spring/blob/main/tutorial_2/tutorial2_quiz.ipynb/)

# ETC
For educational purpose only. This software cannot be used for any re-distribution with or without modification.

The lecture notebook files are copied or modified from the material of Siamak Ravanbakhsh. 


## How to run Colab in local?

1. Install Jupyter
~~~~bash
conda install -c conda-forge jupyterlab
~~~~

2. Jupyter Server Extension Installation
~~~~bash
pip install jupyter_http_over_ws
jupyter server extension enable --py jupyter_http_over_ws
~~~~

3. Run the Jupyter server
~~~~bash
jupyter notebook --NotebookApp.allow_origin='https://colab.research.google.com' --port=8888 --NotebookApp.port_retries=0
~~~~