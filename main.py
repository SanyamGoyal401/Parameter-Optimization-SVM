import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd
from ucimlrepo import fetch_ucirepo

# fetch dataset
optical_recognition = fetch_ucirepo(id=80)

# data (as pandas dataframes)
X = optical_recognition.data.features
y = optical_recognition.data.targets

data = pd.concat([X, y], axis = 1)

samples = [data.sample(3000) for _ in range(10)]

def analytics():
    # Basic statistics
    print("Dataset Shape:", X.shape)
    print("Number of Classes:", len(np.unique(y)))

    # Check for missing values
    print("Missing Values:", np.isnan(X).sum())

    # Visualize the distribution of target classes
    plt.figure(figsize=(8, 6))
    plt.hist(y, bins=np.arange(-0.5, 10, 1), edgecolor='black', alpha=0.7)
    plt.xticks(range(10))
    plt.xlabel('Classes')
    plt.ylabel('Count')
    plt.title('Distribution of Target Classes')
    plt.grid(True)
    plt.show()


# function to optimize SVM with given number of iterations
def optimize_svm(X_train, y_train, X_test, y_test, iterations=100):
    best_accuracy = 0
    best_params = None
    convergence = []
    for _ in range(iterations):
        # Randomly sample SVM hyperparameters
        C = np.round(np.random.uniform(0, 100), 2)  # Penalty parameter C
        gamma = np.round(np.random.uniform(0, 100), 2)  # Kernel coefficient for 'rbf'
        kernel = np.random.choice(['linear', 'rbf', 'sigmoid'])  # Randomly choose kernel function

        # Train SVM with sampled hyperparameters
        svm = SVC(C=C, gamma=gamma, kernel=kernel)
        svm.fit(X_train, y_train)

        # Predict on test set
        y_pred = svm.predict(X_test)

        # Calculate accuracy
        accuracy = np.round(accuracy_score(y_test, y_pred), 2)

        # Update best parameters if current accuracy is higher
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_params = {'C': C, 'gamma': gamma, 'kernel': kernel}

        convergence.append(best_accuracy)


    return best_params, convergence, best_accuracy


# function to plot convergence graph
def plot_convergence(convergence):
    plt.ylim(0, 1)
    plt.plot(convergence)
    plt.xlabel('Iterations')
    plt.ylabel('Accuracy')
    plt.title('Convergence of SVM')
    plt.show()


def create_table(data):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Hide axes
    ax.axis('off')

    # Create the table
    table = ax.table(cellText=data, loc='center', cellLoc='center')

    # Adjust font size
    table.auto_set_font_size(False)
    table.set_fontsize(10)

    ax.set_title('Best Parameter Table')

    plt.show()


# table data
data = [['Sample', 'Best Accuracy', 'C value', 'gamma value', 'kernel']]

# Define number of samples
num_samples = 10

max_convergence_list = [0]
max_accuracy = 0
# Perform the task for each sample
for i, sample_data in enumerate(samples):
    print(f"Sample {i + 1}:")
    X = sample_data.drop(columns=['class'])
    y = sample_data['class']

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=np.random.randint(100))

    # Optimize SVM
    best_params, convergence, best_accuracy = optimize_svm(X_train, y_train, X_test, y_test)
    data.append([f"S{i + 1}", max(convergence), best_params['C'], best_params['gamma'], best_params['kernel']])

    print("Best Parameters:", best_params)
    print("Best Accuracy:", best_accuracy)

    if best_accuracy > max_accuracy:
        max_convergence_list = convergence
        max_accuracy = best_accuracy

plot_convergence(max_convergence_list)
create_table(data)
analytics()