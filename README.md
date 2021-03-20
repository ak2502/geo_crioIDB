# Exploratory Analysis of Geolocational Data

This is my project for #IBelieveinDoing Projects Edition program from Crio.Do

1) Filter and cleaned the existing dataset by selecting suitable attributes and handling NaN values. Saving the cleaned dataset as csv file.
   
2) Plotting the cleaned data using boxplot and analysing the results.

3) Cluster the data using K-means clustering

4) Finding a suitable K using trial and error

5) Plotting Boxplot and making inference for the desired value of K

6) The optimal value of K=3.

7) Using  HERE Geocoding & Search API to get Geolocational Data.

8) Collecting residential locations around IIT Bombay.

9) Cleaning the collected data.

10) Count of grocery stores, restaurants, gyms etc. around each residential location
   
|    |   position.lat |   position.lng |   Cafes |   Department Stores |   Gyms |
|----|----------------|----------------|---------|---------------------|--------|
|  0 |        19.1255 |        72.9193 |      13 |                   4 |     16 |
|  1 |        19.1234 |        72.9127 |      20 |                   5 |     20 |
|  2 |        19.1193 |        72.9123 |      20 |                   6 |     20 |
|  3 |        19.111  |        72.8988 |       7 |                   5 |     15 |
|  4 |        19.1206 |        72.8856 |      12 |                   2 |     20 |
|  5 |        19.1175 |        72.8837 |      16 |                   2 |     20 |
|  6 |        19.1627 |        72.9329 |      11 |                   5 |      6 |
|  7 |        19.1175 |        72.8803 |      15 |                   3 |     18 |
|  8 |        19.096  |        72.9136 |      20 |                  14 |     16 |
|  9 |        19.1148 |        72.8782 |      20 |                   4 |     19 |
| 10 |        19.1117 |        72.8751 |      20 |                   4 |     20 |
| 11 |        19.1002 |        72.8813 |      20 |                   3 |     13 |

11) Applied K-Means on API dataset

|    |   position.lat |   position.lng |   Cafes |   Department Stores |   Gyms |   Cluster |
|----|----------------|----------------|---------|---------------------|--------|-----------|
|  0 |        19.1255 |        72.9193 |      13 |                   4 |     16 |         2 |
|  1 |        19.1234 |        72.9127 |      20 |                   5 |     20 |         1 |
|  2 |        19.1193 |        72.9123 |      20 |                   6 |     20 |         1 |
|  3 |        19.111  |        72.8988 |       7 |                   5 |     15 |         0 |
|  4 |        19.1206 |        72.8856 |      12 |                   2 |     20 |         2 |
|  5 |        19.1175 |        72.8837 |      16 |                   2 |     20 |         2 |
|  6 |        19.1627 |        72.9329 |      11 |                   5 |      6 |         0 |
|  7 |        19.1175 |        72.8803 |      15 |                   3 |     18 |         2 |
|  8 |        19.096  |        72.9136 |      20 |                  14 |     16 |         1 |
|  9 |        19.1148 |        72.8782 |      20 |                   4 |     19 |         1 |
| 10 |        19.1117 |        72.8751 |      20 |                   4 |     20 |         1 |
| 11 |        19.1002 |        72.8813 |      20 |                   3 |     13 |         1 |

