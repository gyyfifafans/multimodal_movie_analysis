#!/usr/bin/python
# -*- coding: utf-8 -*

import numpy as np
from sklearn.preprocessing import minmax_scale
from sklearn.metrics.pairwise import cosine_similarity


def find_similar_movies(names, features, threshold = 0.5):
    """
    Helper function for evaluating similarity.
    Prints the similar movies, with more than threshold similarity.
    Input:
        - names: list,
        list of strings, containing the movie names
        - features: np.array,
        N x F sized feature matrix, where N are the movies and F the features
    Output:
        None, just prints the movies for whom the cosine similarity exceeds the threshold
    """
    sim = cosine_similarity(features)
    np.fill_diagonal(sim, 0)
    # threshold = np.mean(sim)
    ii, jj = np.where(np.tril(sim, k=-1) >= threshold)
    print(f'Similar movies found:')
    for i in ii:
        for j in jj:
            print(f'{names[i]} -- {names[j]} : {100 * sim[i, j]:.2f} %')
    print(f'~' * 50)


def find_top_n_similar_pairs(names, features, top_n=10):
    """
    Helper function for evaluating similarity.
    Prints the top_n similar movie pairs.
    Input:
        - names: list,
        list of strings, containing the movie names
        - features: np.array,
        N x F sized feature matrix, where N are the movies and F the features
        - top_n: int,
        number of the top-N scoring movie pairs to show
    Output:
        None, just prints the movies for whom the cosine similarity exceeds the threshold
    """
    sim = cosine_similarity(features)
    sim = np.tril(sim, k=-1)
    indices = np.dstack(np.unravel_index(np.argsort(sim.ravel())[::-1], sim.shape))[0]
    # threshold = np.mean(sim)
    print(f'Top-{top_n} similar movies found:')
    c = 0
    while c < top_n:
        i, j = indices[c, 0], indices[c, 1]
        print(f'{names[i]} -- {names[j]} : {100 * sim[i, j]:.4f} %')
        c += 1
    print(f'~' * 50)
