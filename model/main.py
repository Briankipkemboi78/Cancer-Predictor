import pandas as pd
from sklearn.preprocessing import StandardScaler



def create_model(data):
    X = data.drop(['diagnosis'], axis = 1)
    y = data['diagnosis']

    scaler = StandardScaler()
    
    # Scale the data to ensure uniformity
    X = scaler.fit_transform(X)



def get_clean_data():
    data = pd.read_csv("data/data.csv")
    
    data = data.drop(['Unnamed: 32', 'id'], axis=1)
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

    return data


def main():
    data = get_clean_data()

    model = create_model()
    

if __name__ == '__main__':
    main()