from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()
X, y = iris.data, iris.target

def evaluate_model(train_size, max_depth=None, min_samples_split=2):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=train_size, random_state=42, stratify=y
    )
    
    model = DecisionTreeClassifier(criterion='entropy', max_depth=max_depth, min_samples_split=min_samples_split, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"\nTrain Size: {train_size*100:.0f}%")
    print(f"Max Depth: {max_depth}, Min Samples Split: {min_samples_split}")
    print(f"Accuracy: {acc:.4f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))
    
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=iris.target_names, yticklabels=iris.target_names)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

train_sizes = [0.5, 0.7, 0.9]
depths = [None, 3, 2]
min_splits = [2, 5]

for train_size in train_sizes:
    for depth in depths:
        for min_split in min_splits:
            evaluate_model(train_size=train_size, max_depth=depth, min_samples_split=min_split)
