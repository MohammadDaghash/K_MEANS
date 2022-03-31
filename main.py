import sys


class KMeans:

    def __init__(self, K, input_filename, output_filename, max_iter = 200, epsilon=0.001):
        self.K = K
        self.max_iter = max_iter
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.epsilon = epsilon
        self.data_points = dict()
        self.initialize_data_points()  # read the given data points from the input file into a dictionary
        self.centroids = dict()
        self.initialize_centroids()
        self.clusters = dict()
        self.initialize_clusters()
        self.N = len(self.data_points)
        self.d = len(self.data_points[1])

    def initialize_data_points(self):
        index = 1
        with open(self.input_filename, 'r') as file:
            for line in file:
                self.data_points[index] = tuple(line.strip().split(","))  # (x,y,z)
                index += 1

    def initialize_centroids(self):
        for i in range(1, self.K + 1):
            self.centroids[i] = self.data_points[i]

    def initialize_clusters(self):
        for centroid in self.centroids:
            self.clusters[centroid] = set()

        def assign_to_clusters(self):
        min = 0
        index = 0
        for x in data_points:
           for i in range(len(x)):
               min += (pow(x[i] - centroids[0][i], 2))
           for j in range(k):
               sum = 0
               for i in range(len(x)):
                   sum += (pow(x[i] - centroids[j][i], 2))
               if sum < min:
                   min = sum
                   index = j
           self.clusters[index].add(self.data_points[i])


    def vecnorm(vec, oldvec):
        norm = 0
        for i in range(len(vec)):
            norm += pow(vec[i] - oldvec[i], 2)
        norm = pow(norm, 0.5)
        return norm

    def update_centroids(self):
        oldcentroids=[[centroids[i][j]for j in range(len(self.d))] for i in range(self.K)]
        for i in range(len(clusters)): #K
            for j in range(len(clusters[i][j])): #d
                for k in range(len(cluster[i])):
                     sum += clusters[i][k][j]
                centroids[i][j] = sum/len(clusters[i])


    def is_converged(self):  # checks the convergence criteria
        for i in range(len(centroids)):
            if vecnorm(centroids[i],oldcentroids[i]) >= self.epsilon:
                return False
        return True


    def output_centroids(self):
        with open(self.output_filename, 'w') as file:
            line = str()
            for centroid in self.centroids:
                for coordinate in centroid:
                    line = line + str("%.4f" % coordinate) + ","
                file.write(line[:-1])
                line = str()
    def sum_vectors(self, x,y):
        """

        :param x:
        :param y:
        :return: the vector x+y
        """
        pass

    def subtract_vectors(self, x,y):
        """
        :param x:
        :param y:
        :return: the vector x-y
        """
        pass

    def scalar_mult(self,x,y):
        """

        :param x:
        :param y:
        :return: the scalar multiplication of x and y
        """
        pass

    def run(self):  # apply the algorithm and save the result in the output file given
        self.initialize_centroids()
        iteration = 0
        while not self.is_converged() and iteration < self.max_iter:
            iteration += 1
            self.assign_to_clusters()
            self.update_centroids()
            self.output_centroids()


def main():
    args = sys.argv[1:]  # need to add argument format validation
    kmeans = KMeans(int(args[0]), args[2], args[3], int(args[1]))
    # K - need to check that it is valid integer
    # max_iter - # need to check that it is valid integer
    # input_filename = args[2]  # need to check that it is valid file name that is openable
    # output_filename = args[3]  # need to check that it is valid file name that is openable
    kmeans.run()


if __name__ == "__main__":
    main()
