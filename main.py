import pandas as pd

worker = [

    ["Ahmed", "Engineering"],
    ["Mohamed", "Hr"],
    ["Keram", "Accounting"],
    ["Abdallah", "Engineering"],
    ["Fouad", "office boy"],
    ["Hassan", "Engineering"],
    ["Rade", "Accounting"]

]

mangers = [

    ["Omer", "Accounting"],
    ["Tarek", "Engineering"],
    ["bassant", "Hr"],
    [None, "office boy"]
]

worker_df = pd.DataFrame(worker, columns=["Name", "Section"])
manger_df = pd.DataFrame(mangers, columns=["Manger", "Section"])

print(worker_df)
print('\n')
print(manger_df)

new_one = pd.merge(worker_df, manger_df)
print('\n')
print(new_one)