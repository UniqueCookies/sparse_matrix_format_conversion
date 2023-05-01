# Test Graphs for Coding algorithms

This archive contains graph data of various sizes for implementing and testing
clustering and multilevel embedding algorithms on.

## Datasets

### Baseball --- n=30 and nnz=300

The files: `baseball.mtx` and `baseball_labels.txt`

This is a symmetric (undirected) relation describing the 2022 major-league
baseball season. The weight on the edge is how many times the teams played that
season. This is a good test for community detection, as strong ground truth
communities exist.

### Cocktail Recipes --- 164 by 216 and nnz=1028

The files: `cocktail.mtx`, `cocktail_labels.txt`, and `ingredient_labels.txt`

This is a bipartite relation between cocktail recipes scraped from New York
Times Cooking blog and the ingredients in the recipes. The rows of the matrix
are recipes and columns are ingredients, or a recipe-ingredient relation.
Composing this relation with it's transpose can produce both a recipe-recipe
or ingredient-ingredient relation as discussed in class.

### Reddit --- n=35,775 and nnz=137,821

The files: `reddit.mtx` and `reddit_labels.txt`

This is a non-symmetric (directed) graph describing when a post one subreddit
links to a post in another subreddit. The relation is square so it can be
generalized to an undirected graph by adding the transpose to the directed
relation.

This relation is larger, but still a manageable size.

### Wikipedia --- n=1,791,489 and nnz=28,511,807

The files: `wikipedia.mtx` and `wikipedia_labels.txt`

This is another directed graph describing the topology of the entirety of
wikipedia. An edge occurs in the graph when one page links to another.
Again, this can be generalized to undirected by adding the transpose.

This is a very large network, good luck with this one.

## Loading the data

I have included some examples to show how to load a `matrix market` format
file into `scipy` and how to relate the labels with the graph. See the code
at `example.py`.
