from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import time  # Para medir o tempo de execução

# --- Passo 1: Carregar dados ---
print("Carregando dados...")
california = fetch_california_housing()
X = pd.DataFrame(california.data, columns=california.feature_names)
y = california.target

# --- Passo 2: Divisão simplificada ---
print("Dividindo dados...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- Passo 3: Modelo mais leve para teste ---
print("Treinando modelo...")
start_time = time.time()

# Usando parâmetros reduzidos para teste rápido
model = RandomForestRegressor(
    n_estimators=50,  # Reduzido de 200 para 50
    max_depth=5,      # Reduzido de 10 para 5
    random_state=42,
    n_jobs=-1         # Usa todos os núcleos do CPU
)
model.fit(X_train, y_train)

print(f"Modelo treinado em {time.time() - start_time:.2f} segundos")

# --- Passo 4: Avaliação ---
print("Avaliando...")
y_pred = model.predict(X_test)

print("\n" + "="*50)
print(f"MSE: {mean_squared_error(y_test, y_pred):.4f}")
print(f"R²: {r2_score(y_test, y_pred):.4f}")
print("="*50 + "\n")

# --- Passo 5: Feature Importance ---
print("Features mais importantes:")
importances = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)
print(importances)

# Depois tentar com outra base de dados pra ver como funciona