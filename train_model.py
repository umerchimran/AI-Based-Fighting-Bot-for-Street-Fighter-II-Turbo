import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import joblib

# 1. Load the data
df = pd.read_csv("gameplay_data.csv")

# 2. Drop rows with missing or invalid command
df = df.dropna(subset=['Command'])  # Remove NaN in 'Command'
df = df[df['Command'].apply(lambda x: isinstance(x, str))]  # Keep only strings

# 3. Features and target
X = df[['X', 'Y', 'Left', 'Right', 'Up', 'Down', 'A', 'B', 'Y_btn', 'L', 'R']]
y = df['Command']

# 4. Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# 5. Split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# 6. Train
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 7. Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_.astype(str)))

# 8. Save
joblib.dump(model, "trained_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

print("Model and label encoder saved successfully.")
