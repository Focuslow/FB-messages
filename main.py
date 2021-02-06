from get_json import get_json
from plotter import plotppl
from words_used import words_used
from grapher import graph
import dash
import dash_core_components as dcc
import dash_html_components as html
import msgs_overtime as ms
from message_script import message_script

app = dash.Dash(__name__)

main_path, name_fix = message_script()
data = get_json(main_path)
save = data.copy()
times = ms.get_msgs_time(data)
fig1, fig2, fig3 = plotppl(data)
fig5 = ms.plot_overtime(times, 1)
msg_info = ""
people = list(data.keys())

msgs_start = times[0][0].year
msgs_end = times[0][-1].year+1


app.layout = html.Div(children=[
    html.Div([
        html.Div([
            dcc.Graph(id='g2', figure=fig2)
        ], className="six columns"),

        html.Div([
            dcc.RangeSlider(
                id="slider1",
                min=msgs_start,
                max=msgs_end,
                value=[msgs_start, msgs_end],
                marks={msgs_start + i: '{}'.format(msgs_start + i) for i in range(msgs_end - msgs_start + 1)},
                pushable=1,
                step=1/12
            )], style={'width': '94%', 'padding-left': '3%', 'padding-right': '3%'}),

        html.Div([
            dcc.Graph(id='g5', figure=fig5)
        ], className="six columns"),

        html.Div([
            dcc.Graph(id='g1', figure=fig1)
        ], className="six columns"),

        html.Div([
            dcc.Graph(id='g3', figure=fig3)
        ], className="six columns"),

        html.Div([
            dcc.Dropdown(
                id='name',
                options=[{'label': i.replace("_", " "), 'value': i.replace("_", " ")} for i in people],
                value='{}'.format(people[0].replace("_", " ")),
            ),
        ], style={'width': '100%', 'display': 'inline-block'})
        ,

        html.Div([
            html.H4(id="msg_info_first_me", children=["init"]),
            html.H4(id="msg_info_first_you", children=["init"])
        ]),

        html.Div([
            html.H4(id="msg_info_last_me", children=["init"]),
            html.H4(id="msg_info_last_you", children=["init"])
        ]),

        html.Div([
            dcc.Graph(id='g4')
        ], className="six columns"),

        html.Div([
            dcc.Graph(id='g6')
        ], className="six columns"),

    ], className="row")
])


@app.callback(
    dash.dependencies.Output('g2', 'figure'),
    dash.dependencies.Input('slider1', 'value'))

def main_time_limit(value):

    timestamps = ms.time_limiter(value,msgs_end)

    fig2 = plotppl(data,sums_update=True,timestamps=timestamps)

    return fig2


@app.callback(
    [dash.dependencies.Output('g4', 'figure'),
     dash.dependencies.Output('g6', 'figure'),
     dash.dependencies.Output('msg_info_last_me', 'children'),
     dash.dependencies.Output('msg_info_last_you', 'children'),
     dash.dependencies.Output('msg_info_first_me', 'children'),
     dash.dependencies.Output('msg_info_first_you', 'children'), ],
    [dash.dependencies.Input('name', 'value')]
)
def update_graph(name):
    person = name
    words_me, words_you = words_used(data[person.replace(" ", "_")], name_fix)
    times_info, msgs_info_first_me, msgs_info_last_me, msgs_info_last_you, msgs_info_first_you = ms.get_msgs_time(
        save[person.replace(" ", "_")])
    fig4 = graph(words_me, words_you, person)
    fig6 = ms.plot_overtime(times_info, 2)

    return fig4, fig6, msgs_info_last_me, msgs_info_last_you, msgs_info_first_me, msgs_info_first_you


if __name__ == '__main__':
    app.run_server(debug=True)
