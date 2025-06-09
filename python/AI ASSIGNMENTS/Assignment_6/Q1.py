import random 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

def gen_data(n):
    data = []
    for _ in range(n):
        Ws = random.random() 
        Is = random.random() 
        Ye = random.random()
        sal = 100000 + 200000 * (2/7*Ws + 1/7*Is + 4/7*Ye)
        data.append([Ws, Is, Ye, sal])
    return data

def knn_pred(x, y, k=3):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=62)
    
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    
    for i in range(len(y_test)):
        print(f"Test Sample {i+1}: Predicted = {y_pred[i]}, Actual = {y_test[i]}")
    
    return knn

def main():
    dat = gen_data(100)  
    
    x = [row[:3] for row in dat]
    y = [row[3] for row in dat]
    knn_model = knn_pred(x, y, k=3)
    
    candidates = [
        [0.8, 0.7, 0.5],   
        [0.7, 0.6, 0.8]    
        ]
    
    predictions = knn_model.predict(candidates)
    
    print("\nPredictions for New Candidates:")
    for i, salary in enumerate(predictions, start=1):
        print(f"Candidate {chr(64+i)}: {salary:}")

main()
