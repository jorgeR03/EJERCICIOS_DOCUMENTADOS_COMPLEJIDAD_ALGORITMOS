from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Mapeo de dígitos a letras, como en un teclado telefónico tradicional
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        # Si no hay dígitos, no hay combinaciones que devolver
        if not digits:
            return []

        result = []

        # Función recursiva para construir combinaciones letra por letra
        def backtrack(index: int, current_combination: str):
            # Caso base: si ya construimos una combinación completa
            if index == len(digits):
                result.append(current_combination)
                return

            # Recorremos todas las letras asociadas al dígito actual
            for letter in phone_map[digits[index]]:
                # Llamamos recursivamente añadiendo la letra a la combinación actual
                backtrack(index + 1, current_combination + letter)

        # Llamada inicial al backtracking
        backtrack(0, "")

        return result
