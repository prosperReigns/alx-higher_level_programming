#!/usr/bin/python3

def square(row):
	return list(map(lambda x: x ** 2, row))

def square_matrix_simple(matrix=[]):
	mat = list(map(square, matrix))
	return mat
