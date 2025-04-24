# CS470: Introduction to Artificial Intelligence - Spring 2025

# Installation

# Tutorial Links
- Tutorial 1: [1-1](https://githubtocolab.com/pidipidi/CS470_IAI_2025_Spring/blob/main/tutorial_1/MLP_tutorial_1_1.ipynb/), [1-2](https://githubtocolab.com/pidipidi/CS470_IAI_2025_Spring/blob/main/tutorial_1/MLP_tutorial_1_2.ipynb/), [1-3](https://githubtocolab.com/pidipidi/CS470_IAI_2025_Spring/blob/main/tutorial_1/MLP_tutorial_1_3.ipynb/)
- [Tutorial 2](https://githubtocolab.com/pidipidi/CS470_IAI_2025_Spring/blob/main/tutorial_2/cs470_tutorial2.ipynb/)
- [Tutorial 3](https://github.com/pidipidi/CS470_IAI_2025_Spring/blob/main/tutorial_3/README.md)

# Assignment Links
- [Assignment 1-1](https://githubtocolab.com/pidipidi/CS470_IAI_2025_Spring/blob/main/assignment_1/problem_1.ipynb)
- [Assignment 1-2](https://githubtocolab.com/pidipidi/CS470_IAI_2025_Spring/blob/main/assignment_1/problem_2.ipynb)
- [Assignment 2](https://githubtocolab.com/pidipidi/CS470_IAI_2025_Spring/blob/main/assignment_2/CS470_Assignment2_problem.ipynb/)
- [Assignment 3](https://githubtocolab.com/pidipidi/cs470_IAI_2025_Spring/blob/main/assignment_3/assignment3_problem.ipynb)
- [Assignment 4](https://githubtocolab.com/pidipidi/CS470_IAI_2025_Spring/blob/main/assignment_4/CS470_Assignment4_problem.ipynb/)
- [Assignment 5](https://github.com/pidipidi/CS470_IAI_2025_Spring/blob/main/assignment_5/src/py_astar_planner/src/py_astar_planner/astar.py)


# Quiz
- [Tutorial Quiz 1](https://githubtocolab.com/pidipidi/CS470_IAI_2025_Spring/blob/main/tutorial_1/MLP_tutorial_quiz_quest.ipynb/)
- [Tutorial Quiz 2](https://githubtocolab.com/pidipidi/CS470_IAI_2025_Spring/blob/main/tutorial_2/RL_tutorial_quiz_problem.ipynb/)

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