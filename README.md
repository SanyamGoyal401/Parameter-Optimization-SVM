### Methodology

1. **Dataset Retrieval**: The mushroom dataset (UCI Repository ID: 602) was fetched using the `ucimlrepo` package.
2. **Data Preprocessing**: The dataset was split into features (X) and target labels (y). Basic analytics such as dataset shape, number of classes, and missing values were examined. Additionally, the distribution of target classes was visualized.
3. **Parameter Optimization**: 
   - Ten random samples of 1000 instances each were generated from the dataset.
   - For each sample:
     - The data was split into training and testing sets.
     - SVM hyperparameters (C, gamma, kernel) were randomly sampled.
     - An SVM model was trained with the sampled hyperparameters.
     - Accuracy was calculated on the test set.
     - This process was repeated for 100 iterations, and the best parameters yielding the highest accuracy were retained.
4. **Convergence Plotting**: A convergence graph was plotted to visualize the accuracy convergence over the iterations.
5. **Result Table Creation**: A table was created to display the best parameters and corresponding accuracies for each sample.
6. **Analytics**: Basic statistics and the distribution of target classes were analyzed on the entire dataset.

### Result Table

| Sample | Best Accuracy | C value | Gamma value | Kernel |
|--------|---------------|---------|-------------|--------|
| S1     | 0.98          | 42.71   | 92.8        | linear |
| S2     | 0.97          | 45.15   | 96.94       | linear |
| S3     | 0.99          | 45.29   | 68.84       | linear |
| S4     | 0.97          | 89.93   | 43.02       | linear |
| S5     | 0.96          | 96.12   | 79.59       | linear |
| S6     | 0.97          | 81.09   | 82.53       | linear |
| S7     | 0.98          | 86.9    | 72.67       | linear |
| S8     | 0.97          | 52.05   | 61.66       | linear |
| S9     | 0.98          | 16.92   | 31.86       | linear |
| S10    | 0.97          | 2.2     | 89.36       | linear |

### Result Graph

The convergence graph below illustrates the accuracy convergence over 100 iterations.

![Convergence of SVM](https://github.com/SanyamGoyal401/Parameter-Optimization-SVM/blob/main/SVM-Convergence.png)

### Additional Analytics

- **Dataset Shape**: (5624, 64)
- **Number of Classes**: 9
- **Missing Values**: 0

![Distribution of Target Classes](https://github.com/SanyamGoyal401/Parameter-Optimization-SVM/blob/main/SVM-Distribution.png)

The distribution of target classes shows a balanced dataset with nine classes.

![Best Parameters Table](https://github.com/SanyamGoyal401/Parameter-Optimization-SVM/blob/main/SVM-Table.png)

The table showing Sample number, Best accuracy, Best C value, Best Gamma value, Best kernel