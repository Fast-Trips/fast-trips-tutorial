import csv
import transitfeed


def routesft_assume_mode(schedule, default_mode):
    routeid_to_mode_dict = dict(zip(schedule.routes.keys(),[default_mode]*len(schedule.routes.keys())))
    return routeid_to_mode_dict


def get_transfer_dist(schedule):
    for k,v in schedule._transfers.iteritems():
        from_stop_id,to_stop_id = k
        
        from_lat = schedule.stops[from_stop_id].stop_lat
        from_lon = schedule.stops[from_stop_id].stop_lon
        to_lat   = schedule.stops[to_stop_id].stop_lat
        to_lon   = schedule.stops[to_stop_id].stop_lon
        
            
