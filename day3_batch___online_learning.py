# -*- coding: utf-8 -*-
"""day3  Batch | Online Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YIIQA5q3-FTCo6_BuVFcxvuSMg8_rIpT

**main difference between batch learning and online learning in machine learning**

Batch Learning:

Definition: In batch learning, the model is trained on the entire dataset at once.
Process:
1. The entire dataset is divided into batches.
2. The model is trained on each batch sequentially.
3. The model parameters are updated after processing the entire dataset.
Advantages:
1. Typically more stable and less sensitive to noisy data.
2. The model is trained on the complete dataset, which may lead to better convergence.
Disadvantages:
1. Requires storing the entire dataset in memory, which can be challenging for large datasets.
2.Computationally expensive, especially for big datasets.

Online Learning (or Incremental Learning):

Definition: In online learning, the model is updated incrementally as new data becomes available.
Process:
1. The model is initially trained on a subset of the data.
2. As new data points become available, the model is updated iteratively.
3. The model adapts to changes in the data distribution over time.
Advantages:
1. Well-suited for streaming data or scenarios where the data evolves over time.
2. Lower memory requirements as the model doesn't need to store the entire dataset.
Disadvantages:
1. Prone to be more sensitive to noise, as each data point can have an immediate impact on the model.
2. May require careful tuning to maintain model stability.
"""

