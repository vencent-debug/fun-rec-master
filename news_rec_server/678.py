from sklearn import cluster, datasets
from sklearn.feature_extraction.image import grid_to_graph

digit = datasets.load_digits()
images = digit.images
x = images.reshape((len(images), -1))
agg = cluster.FeatureAgglomeration(n_clusters=32, connectivity=grid_to_graph(*images[0].shape))
x_ = agg.fit_transform(x)
# print(x_.shape)
images_ = agg.inverse_transform(x_)
images_.shape = images.shape
# print(images_.shape)
# print(images_)