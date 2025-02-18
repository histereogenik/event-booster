class MinhaClasse:
    def __enter__(self):
        print("entrei")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("saí")

with MinhaClasse() as mc:
    print("to dentro!")