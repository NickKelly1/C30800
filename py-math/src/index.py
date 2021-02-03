#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background');

# a = np.array([1, 2, 3]);
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8 , 9]])
# b[1, 1] = 10;
# print(a.shape)
# print(b.shape)
# print(a.dtype)
# print(b);


# m = np.dot
m = np.matrix([
  [1, 0],
  [0, 1],
]);
x = np.array([
  1,
  2,
]);
y = np.dot(m, x);


ax = plt.axes()
plt.grid();
plt.xlim(0, 10);
plt.ylim(0, 10);
plt.title('Testing...');
print(y);
plt.plot(y[0]);

# plt.savefig('how_to_plot.png', bbox_inches="tight");
plt.show();

# print(y);