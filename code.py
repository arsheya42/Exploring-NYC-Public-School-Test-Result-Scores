# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

#Which NYC school has the best math results 

#subsetting the schools with the best math results:

best_math_schools = schools[schools["average_math"] >= 0.8*800]
best_math_schools = best_math_schools[["school_name", "average_math"]].sort_values("average_math", ascending=False)
print(best_math_schools)

#What are the top 10 performing schools based on the combined SAT score

#create a new column of total avg score
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

top_10_schools = schools[["school_name", "total_SAT"]].sort_values("total_SAT", ascending=False)

top_10_schools = top_10_schools.head(10)

print(top_10_schools)

#Find the single borough with the largest standard deviation in the total sat

finding_largest = schools.groupby("borough")["total_SAT"].agg(["count","mean", "std"]).round(2)

largest_std_dev = finding_largest[finding_largest["std"] == finding_largest["std"].max()]

largest_std_dev = largest_std_dev.rename(columns={"count":"num_schools", "mean":"average_SAT", "std":"std_SAT"})

print(largest_std_dev)
