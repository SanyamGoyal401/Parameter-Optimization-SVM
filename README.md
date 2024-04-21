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
| S1     | 0.997         | 9.48    | 2.91        | poly   |
| S2     | 0.998         | 9.68    | 2.45        | poly   |
| S3     | 0.998         | 8.76    | 2.09        | poly   |
| S4     | 0.997         | 9.65    | 2.72        | poly   |
| S5     | 0.998         | 9.43    | 2.14        | poly   |
| S6     | 0.998         | 9.74    | 2.37        | poly   |
| S7     | 0.998         | 9.92    | 1.75        | poly   |
| S8     | 0.998         | 9.85    | 2.62        | poly   |
| S9     | 0.998         | 9.79    | 1.91        | poly   |
| S10    | 0.998         | 9.98    | 1.64        | poly   |

### Result Graph

The convergence graph below illustrates the accuracy convergence over 100 iterations.

![Convergence of SVM](convergence_plot.png)

### Additional Analytics

- **Dataset Shape**: (8124, 22)
- **Number of Classes**: 2
- **Missing Values**: 0

![Distribution of Target Classes](class_distribution.png)

The distribution of target classes shows a balanced dataset with two classes.