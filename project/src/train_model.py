import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
data_path = os.path.join(base_dir, 'data', 'NSL-KDD', 'KDDTrain+.txt')
columns_path = os.path.join(base_dir, 'data', 'NSL-KDD', 'KDDFeatureNames.txt')

with open(columns_path, 'r') as f:
    cols = [line.strip() for line in f.readlines()]

df = pd.read_csv(data_path, names=cols)
df.drop("difficulty", axis=1, inplace=True)
df['target'] = df['target'].apply(lambda x: 'normal' if x == 'normal' else 'attack')

features = ['protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes']
df_small = df[features + ['target']].copy()

# Encode categorical features
label_encoders = {}
for col in ['protocol_type', 'service', 'flag']:
    le = LabelEncoder()
    df_small[col] = le.fit_transform(df_small[col])
    label_encoders[col] = le

X = df_small[features]
y = df_small['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

model_path = os.path.join(base_dir, 'model', 'ids_model_simple.pkl')
joblib.dump((clf, label_encoders), model_path)
print(f"Model saved at {model_path}")
