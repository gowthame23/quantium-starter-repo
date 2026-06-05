from pink_morsel_visualizer import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert "Pink Morsel Sales Visualiser" in header.text


def test_graph_present(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    radio_items = dash_duo.find_element("#region-filter")
    assert radio_items is not None