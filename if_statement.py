class IfBlock():

    def __init__(self, value, startLine, endLine = 1):
        self.value = value
        self.startLine = startLine
        self.endLine = endLine

    def __str__(self) -> str:
        return f"Bloco SE com valor de condição {self.value}, começando na linha {self.startLine} e acabando na linha {self.endLine}"