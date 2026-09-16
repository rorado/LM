import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# x = np.array(
#     [
#         [
#             [
#                 [210, 2, 9, 9],
#                 [98, 9, 2, 90]
#             ],
#             [
#                 [9, 2, 2, 500],
#                 [3, 4, 7, 5]
#             ]
#         ],
#         [
#             [
#                 [5, 6, 4, 41],
#                 [5, 5, +6, 4]
#             ],
#             [
#                 [8, 7, 8, 4],
#                 [63, 7, 8, 4]
#             ]
#         ],
#         [
#             [
#                 [5, 6, -4, 401],
#                 [5, 5, +6, 4]
#             ],
#             [
#                 [101, 7, 88, 5],
#                 [876, 47, 8, 254]
#             ]
#         ]
#     ]
# )


# # print("ndin", x.ndim, "shap", x.shape, "len", len(x), "size", x.size, "dateType", x.dtype, "sum", x.sum(), "min", x.min(), "unique", np.sort(x))
# print(x[0, 0, 0, -1])


# ex0 = np.array(
#         [
#             [28, 1200],
#             [25, 1000],
#             [35, 2300],
#             [29, 1400],
#             [38, 2500],
#             [40, 3000]
#         ]
#     )

# salaries = ex0[:, 1]
# ages = ex0[:, 0]
# print("average ages", np.mean(ages))
# print("average salarieas", np.mean(salaries))
# print("highest salary", salaries.max())
# print("lowest age", ages.min())
# print("All salaries greater than 1500:", salaries[salaries > 1500])
# print("ages of people whose salary is greater than",ages[salaries > 1500])
# print("average salary of people older than 30", np.mean(salaries[ages > 30]))


# data = {
#     "name": ["sohaib", "lifo", "mido"],
#     "age": [85, 78, 25],
#     "salary": [5000, 6000, 6300],
# }

# df = pd.DataFrame(data)
# print(df[df["salary"] < 5005]["age"])

import pandas as pd

data = {
    "name": ["Ali", "Sara", "Omar", "Adam", "Lina"],
    "age": [28, 25, 35, 29, 38],
    "salary": [1200, 1000, 2300, 1400, 2500],
}

df = pd.DataFrame(data)

