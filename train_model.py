import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load your data (must contain 'headline' and 'label')
df = pd.read_csv("stock_headlines.csv")
assert 'headline' in df.columns and 'label' in df.columns, "CSV must have 'headline' and 'label' columns"

X = df['headline'].astype(str)  # Ensure it's string
y = df['label']

# Initialize and fit vectorizer
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Training complete and models saved.")
