import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import base64
import requests

# Load the dataset
file_path = "Updated_DrugReview.csv"  # Replace with your file path
data = pd.read_csv(file_path)

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Drug Review Dashboard", style={"textAlign": "center"}),

    # Sentiment Distribution
    html.Div([
        html.H2("Sentiment Distribution"),
        dcc.Graph(id="sentiment-chart"),
    ]),

    # Topic Insights
    html.Div([
        html.H2("Topic Insights"),
        dcc.Graph(id="topic-chart"),
    ]),

    # Side Effect Trends
    html.Div([
        html.H2("Side Effect Trends"),
        dcc.Graph(id="side-effect-chart"),
    ]),

    # Word Cloud
    html.Div([
        html.H2("Word Cloud"),
        html.Img(id="wordcloud", style={"width": "80%", "margin": "auto"}),
    ]),

    # Chatbot Interface
    html.Div([
        html.H2("Chat with Drug Review Chatbot"),
        dcc.Input(id="user-input", type="text", placeholder="Ask a question...", style={"width": "80%"}),
        html.Button('Submit', id='submit-button', n_clicks=0),
        html.Div(id="chatbot-response", style={"marginTop": "20px", "fontSize": "18px"})
    ]),
])

# Callbacks for dynamic updates
@app.callback(
    Output("sentiment-chart", "figure"),
    Output("topic-chart", "figure"),
    Output("side-effect-chart", "figure"),
    Output("wordcloud", "src"),
    Input("sentiment-chart", "id")  # Dummy input to trigger update
)
def update_charts(_):
    # Sentiment Chart
    sentiment_fig = px.bar(
        data["Sentiment"].value_counts(),
        title="Sentiment Distribution",
        labels={"index": "Sentiment", "value": "Count"},
        color_discrete_sequence=["#636EFA", "#EF553B", "#00CC96"]
    )

    # Topic Chart
    topic_fig = px.bar(
        data["Dominant_Topic"].value_counts().sort_index(),
        title="Topic Distribution",
        labels={"index": "Topic", "value": "Count"},
        color_discrete_sequence=["#AB63FA"]
    )

    # Side Effect Chart
    side_effect_fig = px.pie(
        data["Side_Effect_Label"].value_counts(),
        names=["No Side Effect", "Side Effect"],
        title="Side Effect Trends",
        color_discrete_sequence=["#FFA15A", "#19D3F3"]
    )

    # Word Cloud
    text = " ".join(review for review in data["Cleaned_Reviews"] if isinstance(review, str))
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    wordcloud_path = "wordcloud.png"
    wordcloud.to_file(wordcloud_path)

    # Encode Word Cloud as base64
    with open(wordcloud_path, "rb") as wc_file:
        encoded_image = base64.b64encode(wc_file.read()).decode()

    return sentiment_fig, topic_fig, side_effect_fig, f"data:image/png;base64,{encoded_image}"

# Callback for chatbot response
@app.callback(
    Output("chatbot-response", "children"),
    Input("submit-button", "n_clicks"),
    State("user-input", "value")
)
def update_chatbot_response(n_clicks, user_input):
    if n_clicks > 0 and user_input:
        try:
            # Send a POST request to the chatbot server
            response = requests.post("http://127.0.0.1:5000/chat", json={"query": user_input})
            if response.status_code == 200:
                return response.json().get("response", "Sorry, I couldn't understand that.")
            else:
                return f"Error: Server returned status code {response.status_code}."
        except requests.exceptions.ConnectionError:
            return "Error: Unable to connect to the chatbot server. Please ensure it is running."
    return ""

# Run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)