# CS7643_Project
We used the original code implementation of [Boosting method](https://github.com/compphoto/BoostingMonocularDepth) as a starting point, and made some modifications to the resolution selection part and refined the code structure. We combined code implementations of [MiDaS](https://github.com/isl-org/MiDaS) as the backbone and [Pix2Pix](https://github.com/phillipi/pix2pix) as the merge network togerther with the boosting implementation. In addition, we implemented a script to apply noise and corruptions to NYU-v2 dataset, and evaluated the model performance on that dataset.

The link to Boosting Monocular Depth Estimation Github repository is at 
https://github.com/compphoto/BoostingMonocularDepth

The link to MiDaS Github repository is at 
https://github.com/isl-org/MiDaS

The link to Pix2Pix Github repository is at 
https://github.com/phillipi/pix2pix

The Github repository for our final project is at 
https://github.com/DavidLXu/CS7643_Project/

run commands:

**Running the method using MiDas**

`python run.py --Final --data_dir ./inputs --output_dir  ./outputs_midas/ --depthNet 0`

**Running the method using LeRes**

`python run.py --Final --data_dir ./inputs --output_dir  ./outputs_leres/ --depthNet 2`

