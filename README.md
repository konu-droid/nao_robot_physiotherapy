# nao_robot_physiotherapy
This repository contains files for robot physiotherapist using the nao robot, specifically for use with rehabilitation and recovery of patients who have undergone ASL surgery

### New patient
Please begin by editting the new patient name in the speech_funtions.py

### Run the robot
please run the following code in a python 2.7 env with nao sdk installed
``` shell
python robot_physiotherapist.py  
``` 

### Exercise
All the exercises are placed in [exercises folder](exercises) folder, to add a new exercise please edit both [speech_functions](speech_functions.py) function as well as [logic](logic.py) file.

Add your new exercise into the [exercises folder](exercises) and import it in [logic](logic.py). An example for exercises would be [squat](exercises/squat.py)
