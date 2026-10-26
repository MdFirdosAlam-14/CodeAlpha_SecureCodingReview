"""Intentionally insecure training sample. Do not use in a real application."""
import pickle

password = "demo-password-change-me"  # Example only: hard-coded credential
user_expression = input("Enter an expression: ")
result = eval(user_expression)  # Unsafe: evaluates user-controlled input

# Unsafe with untrusted data: pickle.load can execute code during deserialization.
# with open("untrusted.dat", "rb") as stream:
#     value = pickle.load(stream)
