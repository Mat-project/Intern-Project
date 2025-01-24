from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

# Load the cleaned dataset
df = pd.read_csv("./Data_cleaned/output/cleaned_realtor_data.csv")

# Calculate average price by state
avg_price_by_state = df.groupby("state", as_index=False)["price"].mean()

# Initialize Dash app
app = Dash(__name__)

# Create a Plotly bar chart
fig = px.bar(avg_price_by_state, x="state", y="price", title="Average House Price by State",
             labels={"state": "State", "price": "Average Price"})

# Define layout
app.layout = html.Div([
    html.H1("Real Estate Dashboard", style={"textAlign": "center", "color": "blue"}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True, port=8060)
