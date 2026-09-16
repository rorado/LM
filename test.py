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

# import pandas as pd


# data = {
#     "name": ["Ali", "Sara", "Omar", "Adam", "Lina", "Yassine"],
#     "city": ["Casa", "Rabat", "Casa", "Rabat", "Casa", "Rabat"],
#     "age": [28, 25, 35, 29, 38, 32],
#     "salary": [1200, 1000, 2300, 1400, 2500, 2000]
# }

# df = pd.read_csv('products.csv')
# # df = pd.DataFrame(data)

# # counts = df["Product name"].value_counts().head(2)

# # print(df.sort_values("First price", ascending=False)["First price"])


# print(df.groupby("Category")["First price"].max())


import pandas as pd
import numpy as np

data = {
    "product": [
        "Laptop", "Phone", "Laptop",
        "Mouse", "Phone", "Keyboard",
        "Laptop", "Mouse"
    ],

    "category": [
        "Computer", "Mobile", "Computer",
        "Accessory", "Mobile", "Accessory",
        "Computer", "Accessory"
    ],

    "price": [
        1000, 600, 1200,
        30, 650, 80,
        np.nan, 25
    ],

    "quantity": [
        2, 5, 1,
        10, 3, 7,
        2, 15
    ]
}

df = pd.DataFrame(data)

print("1. Print the first 5 rows.")
print(df.head())

print("2 Check how many missing values each column has")
print(df.isnull().sum())

print("3. Find the average price.")
print(df["price"].mean())

print("4. Find how many times each product appears.")
count = df["product"].value_counts()
print(count)

print("5. Show only products that appear more than once.")
# morethatOne = count[count > 1].index
# for i in df.loc[df["product"].isin(morethatOne), "product"].unique():
#     print(i)
print(count[count > 1])

print("6. Show rows where price is greater than 500.")
print(df[df["price"] > 500])

print("7. Sort products from highest price to lowest.")
print(df.sort_values("price", ascending=False))

print("8. Find the average price for each category.")
print(df.groupby("category")["price"].mean())

print("9. Find the total quantity for each category")
print(df.groupby("category")["quantity"].sum())


print("""
10. ⭐ Create a new column:
total_value = price × quantity
""")
df["total_value"] = df["price"] * df["quantity"]
print(df)
