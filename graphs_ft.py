import numpy as np

from bokeh.models import ColumnDataSource, DataRange1d, Plot, LinearAxis, Grid,DatetimeAxis, LabelSet
from bokeh.models.glyphs import Segment

mode2color = {'local_bus':"#b3de69",
             'walk_access':'#8dd3c7',
             'walk_egress':'#bebada',
             'transfer':'#fb8072',
             'other':'#80b1d3'}

def assignColorByMode(mode):
    if mode in mode2color.keys():
        return mode2color[mode]
    return mode2color["other"]
    
def yloc(pathnum,linknum):
        return (pathnum*(1))+linknum
        
def createLinkPathAnnotation(mode,sim_cost,route_id,trip_id,probability):
        if mode not in ['local_bus']:
            return str(mode)+" "+str(sim_cost)
        else:
            return str(mode)+" "+str(sim_cost)+" "+str(route_id)+":"+str(trip_id)

def createLinkAnnotation(mode,sim_cost,route_id,trip_id):
    return str(mode)+" "+str(sim_cost)+" "+str(route_id)+":"+str(trip_id)

def plot_choice_links(linkfile_df,cost="sim_cost",paths=False):
    
    linkfile_df["color"]= map(assignColorByMode, linkfile_df["mode"])
    if paths:
        linkfile_df["annotation"]= map(createLinkPathAnnotation, linkfile_df["mode"], linkfile_df[cost], linkfile_df["route_id"], linkfile_df["trip_id"], linkfile_df["probability"])
    else:
        linkfile_df["annotation"]=map(createLinkAnnotation, linkfile_df["mode"], linkfile_df[cost], linkfile_df["route_id"], linkfile_df["trip_id"])
    

    linkfile_df["yloc"]= map(yloc, linkfile_df["pathnum"],linkfile_df["linknum"])

    linksource = ColumnDataSource(linkfile_df)
    #linkfile_df

    xdr2 = DataRange1d()
    ydr2 = DataRange1d()

    choiceplot = Plot(
        title=None, x_range=xdr2, y_range=ydr2, plot_width=800, plot_height=300,
        h_symmetry=False, v_symmetry=False, min_border=0, toolbar_location=None)

    glyph = Segment(y0="yloc", x0="new_A_time", y1="yloc", x1="new_B_time", line_color="color", line_width=cost)
    choiceplot.add_glyph(linksource, glyph)

    choicexaxis = DatetimeAxis()
    choiceplot.add_layout(choicexaxis, 'below')

    xaxis = DatetimeAxis()
    yaxis = LinearAxis()

    choiceplot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
    choiceplot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

    choice_labels = LabelSet(x="new_A_time", y="yloc", text="annotation", y_offset=-5,x_offset=10,
                      text_font_size="8pt", text_color="#555555",
                      source=linksource, text_align='left')
    choiceplot.add_layout(choice_labels)

    return choiceplot
    
def plot_choiceset_links(linkfile_df,cost="sim_cost",paths=False):
    
    linkfile_df["color"]= map(assignColorByMode, linkfile_df["mode"])
    if paths:
        linkfile_df["annotation"]= map(createLinkPathAnnotation, linkfile_df["mode"], linkfile_df[cost], linkfile_df["route_id"], linkfile_df["trip_id"], linkfile_df["probability"])
    else:
        linkfile_df["annotation"]=map(createLinkAnnotation, linkfile_df["mode"], linkfile_df[cost], linkfile_df["route_id"], linkfile_df["trip_id"])
    

    linkfile_df["yloc"]= map(yloc, linkfile_df["pathnum"],linkfile_df["linknum"])
    pathnums = list(set(list(linkfile_df["pathnum"])))
    plots = {}
    for p in pathnums:
        data_df = linkfile_df[linkfile_df["pathnum"]==p]
        linksource = ColumnDataSource(data_df)

        xdr2 = DataRange1d()
        ydr2 = DataRange1d()

        plots[p] = Plot(
            title="Path Number: %d    Probability: %4.2f Percent" % (p,100*data_df["probability"].max()), x_range=xdr2, y_range=ydr2, plot_width=800, plot_height=150,
            h_symmetry=False, v_symmetry=False, min_border=0, toolbar_location=None)

        glyph = Segment(y0="yloc", x0="new_A_time", y1="yloc", x1="new_B_time", line_color="color", line_width=cost)
        plots[p].add_glyph(linksource, glyph)

        choicexaxis = DatetimeAxis()
        plots[p].add_layout(choicexaxis, 'below')

        xaxis = DatetimeAxis()
        yaxis = LinearAxis()

        plots[p].add_layout(Grid(dimension=0, ticker=xaxis.ticker))
        plots[p].add_layout(Grid(dimension=1, ticker=yaxis.ticker))

        choice_labels = LabelSet(x="new_A_time", y="yloc", text="annotation", y_offset=-5,x_offset=10,
                          text_font_size="8pt", text_color="#555555",
                          source=linksource, text_align='left')
        plots[p].add_layout(choice_labels)

    return plots.values()
    

    ##TODO add nodes
