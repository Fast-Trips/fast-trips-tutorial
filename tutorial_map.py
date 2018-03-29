import pandas
import folium
import transitfeed
import vincent

def make_route_df(schedule, route_id):
    routes = []
    for stop_time in schedule.trips[route_id].GetStopTimes():
        d = { "route_id"      : route_id,
         "stop_name"          : stop_time.stop.stop_name,
         "arrival_secs"       : stop_time.arrival_secs,
         "departure_secs"     : stop_time.departure_secs,
         "shape_dist_traveled": stop_time.shape_dist_traveled }
        routes.append(d)
    return pandas.DataFrame(routes)

def route_popup(schedule, route_id):
    route_df = make_route_df(schedule, route_id)
    vega = vincent.Line(vincent.Data.from_pandas(route_df)) 
    popup = Vega(vega.to_json(), width=vega.width+50, height=vega.height+50)

    return popup

def stop_popup():

    html="""
    <h1> This is a big popup</h1><br>
    With a few lines of code...
    <p>
    <code>
        from numpy import *<br>
        exp(-2*pi)
    </code>
    </p>
    """
    
    iframe = folium.element.IFrame(html=html, width=500, height=300)
    popup  = folium.Popup(iframe, max_width=2650)

    return popup

def add_stops(schedule,map):
    for key,val in schedule.stops.iteritems():
        folium.CircleMarker(location=[val.stop_lat, val.stop_lon],
                            radius=50, 
                            color = "yellow",
                            popup=stop_popup()).add_to(map)

def add_routes(schedule,map):
    route_freq    = {}
    html_rt_popup = {}
    
    coords        = {}
    
    for k,v in schedule.trips.iteritems():
        
        # if you've already seen this route
        if v.route_id in route_freq.keys(): 
            route_freq[v.route_id] += 1
            continue
        route_freq[v.route_id] = 1
        coord_list = []
        for stop in v.GetTimeStops():
            lat = stop[2].stop_lat
            lon = stop[2].stop_lon
            coord_list.append(tuple([lat,lon]))
        coords[v.route_id] = coord_list
    
    for k,v in coords.iteritems():
        folium.features.PolyLine(coords[k],
                                  color=k, 
                                  weight=10,
                                  opacity=0.8,
                                  popup=route_popup(schedule, k)).add_to(map) 

def add_transfers(schedule, map):
    for k,v in schedule._transfers.iteritems():
        from_stop_id,to_stop_id = k
        from_stop = schedule.stops[from_stop_id]
        to_stop   = schedule.stops[to_stop_id]

        coord_list = [tuple([from_stop.stop_lat,from_stop.stop_lon]),
                      tuple([to_stop.stop_lat,to_stop.stop_lon])]

        folium.features.PolyLine(coord_list,
                                 color='gray', 
                                 weight=5,
                                 opacity=0.8,
                                 popup="transfer").add_to(map)



def make_map(schedule):
    (min_lat, min_lon, max_lat, max_lon) = schedule.GetStopBoundingBox()
    
    lilmap = folium.Map(location = [min_lat, min_lon], 
                        zoom_start=15,
                        tiles='Stamen Toner')
                        
    #map.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])
    

    add_stops(schedule,lilmap)
    add_routes(schedule,lilmap)
    add_transfers(schedule,lilmap)                    

    folium.LayerControl().add_to(lilmap)
    return lilmap
