from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load dataset
df = pd.read_csv("data.csv")

# Features & Target
X = df.drop(columns=["target"])
y = df["target"]

# Scale data for SVR
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train models
models = {
    "Linear Regression": LinearRegression().fit(X, y),
    "Ridge Regression": Ridge().fit(X, y),
    "Lasso Regression": Lasso().fit(X, y),
    "Decision Tree": DecisionTreeRegressor().fit(X, y),
    "Random Forest": RandomForestRegressor().fit(X, y),
    "Support Vector Regressor": SVR().fit(X_scaled, y)
}

@app.route("/")
def home():
    return render_template("index.html", feature_names=list(X.columns), model_names=list(models.keys()))

@app.route("/predict", methods=["POST"])
def predict():
    try:
        selected_model = request.form.get("model")
        features = [float(request.form.get(f)) for f in X.columns]

        if selected_model == "Support Vector Regressor":
            features = scaler.transform([features])
        else:
            features = [features]

        prediction = models[selected_model].predict(features)[0]
        return render_template("result.html", prediction=prediction, model=selected_model)
    except Exception as e:
        return render_template("result.html", prediction=f"Error: {str(e)}", model="Error")

if __name__ == "__main__":
    app.run(debug=True)
