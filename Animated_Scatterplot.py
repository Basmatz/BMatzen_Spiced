import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gapminder_total_fertility.csv")
df2 = pd.read_excel("gapminder_lifeexpectancy.xlsx")


#print(df2)

df = df.melt(id_vars="Total fertility rate",
        var_name="year",
        value_name="fertility")

df.rename(columns={"Total fertility rate": "country"}, inplace=True)

df2 = df2.melt(id_vars="Life expectancy",
        var_name="year",
        value_name="life expectancy")

df2.rename(columns={"Life expectancy": "country"}, inplace=True)

df["year"] = df["year"].astype(int)
df2["year"] = df2["year"].astype(int)

df3 = pd.merge(df,df2, how='inner', on=["country","year"])


#print(df3.where(df3["year"]>1960))


fig = px.scatter(df3.loc[(df3["year"] >= 1960)], x="life expectancy", y="fertility", animation_frame="year", animation_group="country", color="country", range_x=[20,100], range_y=[0,10])

fig.show()