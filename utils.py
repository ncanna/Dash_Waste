import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [html.H5("UVA Sustainability Waste Dashboard")],
                        className="main-title",
                    ),
                ],
                className="full column",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header

#High Level Pages
#Home

#Team A Pages (Trends)
#Seasonality
#Predictions (Normalized for pop. and Not)
#Location/Heatmap

#Team B Pages (Waste Reduction)
#Waste Streams

def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Home",
                href="/home",
                className="tab first",
            ),
            dcc.Link(
                "Seasonality",
                href="/seasonality",
                className="tab",
            ),
            dcc.Link(
                "Predictions",
                href="/predict",
                className="tab",
            ),
            dcc.Link(
                "Location Analysis",
                href="/loc",
                className="tab",
            ),
            dcc.Link(
                "Waste Streams",
                href="/streams",
                className="tab",
            )
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
