terminal1
=========
copy paste sensor_stick folder inside ~/catkin_ws/src directory

cd ~/catkin_ws
rosdep install --from-paths src --ignore-src --rosdistro=kinetic -y
catkin_make

export GAZEBO_MODEL_PATH=~/catkin_ws/src/sensor_stick/models
source ~/catkin_ws/devel/setup.bash

roslaunch sensor_stick training.launch

NOTE:
-You should see an empty scene in Gazebo with only the sensor stick robot.

terminal2
=========
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
rosrun sensor_stick capture_features.py

NOTE:
-The features will now be captured and you can watch the objects being spawned in Gazebo. It should take 5-10 sec. for each random orientations (depending on your machine's resources) so with 7 objects total it takes awhile to complete. 
-When it finishes running you should have a training_set.sav file.

sudo pip install sklearn scipy

rosrun sensor_stick train_svm.py


capture_feature.py
==================
-generates point cloud data at different angles for each object
-to improve:
	-increase the range(5) to a higher value to capture more angles
	-use HSV color space by setting using_hsv=True

train_svm.py
============
-trains the model using SVM and plots confusion matrix

