import pandas as pd

data = pd.read_csv("data.csv",encoding='latin-1')

columns = list(data.columns)

# for i in columns:
#     print(f"Column : {i} \n Quick values : \n ")
#     print(data[i].unique(), "lenght : ", len(data[i].unique()))
    





# print(data["sales_channel"].unique(), "lenght : ", len(data["sales_channel"].unique()))
# print(data["trip_type"].unique(), "lenght : ", len(data["trip_type"].unique()))
# print(data["flight_day"].unique(), "lenght : ", len(data["flight_day"].unique()))
# print(data["wants_extra_baggage"].unique(), "lenght : ", len(data["wants_extra_baggage"].unique()))
# print(data["wants_preferred_seat"].unique(), "lenght : ", len(data["wants_preferred_seat"].unique()))
# print(data["wants_in_flight_meals"].unique(), "lenght : ", len(data["wants_in_flight_meals"].unique()))


