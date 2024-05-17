import random
from typing import List


class MasterMindSolver:

    def __init__(self, secret_key: List[int]):
        self.secret_key = secret_key
        self.number_of_bits = len(secret_key)
        self.candidates = self.generate_bit_combinations(num_bits=self.number_of_bits)
        self.guess = None


    def generate_bit_combinations(self, num_bits: int, prefix=[], combinations=[]) -> List[list]:
        if num_bits == 0:
            combinations.append(prefix)
        else:
            self.generate_bit_combinations(num_bits - 1, prefix + [0], combinations)
            self.generate_bit_combinations(num_bits - 1, prefix + [1], combinations)
        return combinations


    def get_not_XOR(self, intput1: List[int], intput2: List[int]) -> List[int]:
        not_XOR_result = [int(not (bit ^ intput2[i])) for i, bit in enumerate(intput1)]
        return not_XOR_result


    def get_guess_grade(self) -> int:
        not_XOR = self.get_not_XOR(self.guess, self.secret_key)
        return sum(not_XOR)


    def get_candidate_grade(self, candidate: List[int]) -> int:
        not_XOR = self.get_not_XOR(candidate, self.guess)
        return sum(not_XOR)


    def predict_secret(self) -> List[List[int]]:
        self.guess = random.choice(self.candidates)

        while len(self.candidates) > 1:

            self.fix_candidate_list()
            shorter_candidates_with_amps = self.shorten_candidates_with_amp()
            self.guess = random.choice(self.candidates)


        return self.candidates


    def fix_candidate_list(self) -> None:
        guess_grade = self.get_guess_grade()
        for candidate in self.candidates:
            candidate_not_XOR = self.get_not_XOR(candidate, self.guess)
            candidate_grade = self.get_candidate_grade(candidate)
            guess_candidate_diff = guess_grade - candidate_grade

            if guess_candidate_diff > 0:
                for bit_index in range(self.number_of_bits):
                    if candidate_not_XOR[bit_index] == 0:
                        candidate[bit_index] = 1 - candidate[bit_index]
                        candidate_not_XOR = self.get_not_XOR(candidate, self.guess)
                        guess_candidate_diff -=1
                    if guess_candidate_diff == 0:
                        break
            elif guess_candidate_diff < 0:
                for bit_index in range(self.number_of_bits):
                    if candidate_not_XOR[bit_index] == 1:
                        candidate[bit_index] = 1 - candidate[bit_index]
                        candidate_not_XOR = self.get_not_XOR(candidate, self.guess)
                        guess_candidate_diff +=1
                    if guess_candidate_diff == 0:
                        break


    def shorten_candidates_with_amp(self) -> dict:
        vector_counts = {}
        for vector in self.candidates:
            vector_tuple = tuple(vector)
            if vector_tuple in vector_counts:
                vector_counts[vector_tuple] += 1
            else:
                vector_counts[vector_tuple] = 1

        unique_tuples = set(tuple(vector) for vector in self.candidates)

        self.candidates = [list(vector) for vector in unique_tuples]
        vector_counts_after_removal = {tuple(vector): vector_counts[tuple(vector)] for vector in self.candidates}

        return vector_counts_after_removal
