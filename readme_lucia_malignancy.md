# Tutorial: Steps for running the **nodule_malignancy** model

### **Description:**

<br>

This model uses deep learning to predict the development of lung cancer in a patient, by giving the malignancy score of lung nodules detected in a CT-scan volume.

Specifically, it uses a 3D convolutional neural network (3D CNN), with an AUC was 0.85.

The results are the centroid coordinates for each detected lung nodule, together with their size, the malignancy score and the probability of it being a nodule (the last two as a number between 0 and 1).

<br>

> **Note:** For more details go to the [model](https://github.com/pfillard/tpx-kaggle-dsb2017#kaggle---data-science-bowl-2017---therapixel-solution) site.

<br>

---

<br>

**1.** Run the container with:

    docker exec -it b3b3f6a4174c bash

**2.** Insert a `.mhd` and a `.raw` file in an input folder in the main directory (e.g. name the folder: `patient1/`)

<br>

**3.**  Run the `predict.py` script with the following command: 

    python3 -m predict -i submission2.csv -d patient1

Where `patient1` is the name of the input folder and `submission2.csv` is the name of a default csv file.

<br>

**4.** The output will be a **csv** in a created `predict_results/` default folder, called `output_nodules_characteristics.csv`

For example, for five detected nodules, it will contain the following information:


| seriesuid |	coordX |	coordY |	coordZ |	probability |	malignancy |	size |
| ------ | ------ | ------ | ------ | ------ |  ------ | ------ |
| 1	| 75.75 |	87.75 |	951.625 |	0.9999798 |	0.14961852 |	3.925066 |
| 1	| -34.25 |	159.625	| 1010.375 |	0.9999285 |	0.5908394 |	9.939271 |
| 1	| 58.875 |	202.75 |	1002.875 |	0.99968064 |	0.8804302 |	16.776213 |
| 1	| 76.375 |	162.125 |	1019.125 |	0.69688934 |	0.45521757 |	6.0080557 |
| 1	| -53.0 |	95.875 |	938.5 |	0.6764742	| 0.44104528 |	4.512931 |




