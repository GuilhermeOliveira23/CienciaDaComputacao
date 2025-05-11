from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# Carregar dataset
california = fetch_california_housing()
X = pd.DataFrame(california.data, columns=california.feature_names)  # Features
y = california.target  # Preço médio das casas (em centenas de milhares de dólares)

# Ver as primeiras linhas
print(X.head())
print("\nPreços reais (y):", y[:5])

# Entender essa linha
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Variáveis xtrain{X_train}\n xteste:{X_test}")
# Treinar modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Prever e avaliar
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))