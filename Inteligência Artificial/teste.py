from sklearn.model_selection import train_test_split
import numpy as np

X = np.array([10, 20, 30, 40, 50])
y = np.array([1, 2, 3, 4, 5])

# Com random_state=42
print("=== random_state=42 ===")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Treino:", X_train, "| Teste:", X_test)

# Sem random_state (aleatório)
print("\n=== Sem random_state ===")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print("Treino:", X_train, "| Teste:", X_test)