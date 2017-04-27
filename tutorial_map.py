import folium
import transitfeed

def make_map(schedule):

    lilmap = folium.Map(location = [35.779584, -78.661572], 
                        zoom_start=15,
                        tiles='Stamen Toner'
                       )
    # add stops
    for key,val in schedule.stops.iteritems():
        folium.CircleMarker(location=[val.stop_lat, val.stop_lon],
                         radius=50, color = "yellow",popup=key).add_to(lilmap)

    # add routes                         
    route_freq = {}
    for k,v in schedule.trips.iteritems():
    
        if v.route_id in route_freq.keys(): 
            route_freq[v.route_id] += 1
            continue
        route_freq[v.route_id] = 1
        coord_list = []
        for stop in v.GetTimeStops():
            lat = stop[2].stop_lat
            lon = stop[2].stop_lon

            coord_list.append(tuple([lat,lon]))
        folium.features.PolyLine(coord_list,
                                      color=v.route_id, 
                                      weight=10,
                                      opacity=0.8,popup=v.route_id).add_to(lilmap)

    # add transfers
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
                                 popup="transfer").add_to(lilmap)

    folium.LayerControl().add_to(lilmap)
    return lilmap
