from pink_morsel_visualizer import app
from dash import html, dcc


def test_header_present():
    header = app.layout.children[0]
    assert isinstance(header, html.H1)
    assert "Pink Morsel Sales Visualiser" in header.children


def test_region_picker_present():
    region_picker = app.layout.children[2]
    assert isinstance(region_picker, dcc.RadioItems)


def test_visualisation_present():
    graph = app.layout.children[3]
    assert isinstance(graph, dcc.Graph)