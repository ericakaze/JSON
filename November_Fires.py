def main():
    from plotly.graph_objs import Scattergeo, Layout 
    from plotly import offline 
    a,b,c = get_data ("MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2019331.csv") 
   
    data =[dict(type='scattergeo',lon=b,lat=a, mode = 'markers', marker = dict(size = 20,colorscale= 'viridis', reversescale = True,
    color = c, colorbar = dict(title = 'Brightness',titleside = 'top',tickmode = 'array',)))] 

    layout = dict(title = 'Australian Fires - November 2019',geo = dict(showland = True, lataxis = dict(range=[-38.96,-11.01]), 
    lonaxis = dict(range=[113.72,153.80]))) 

    fig = dict(data=data, layout=layout)
    offline.plot(fig, filename='November_Fires.html') 

 
def get_data (x): 
    import csv
    from datetime import datetime 

    open_file= open(x, "r")
    csv_file= csv.reader(open_file, delimiter=",")

    header_row= next (csv_file)


    latitude_index = header_row.index('latitude')
    longitude_index = header_row.index('longitude')
    brightness_index = header_row.index('brightness')
    

    latitudes =[]
    longitudes= []
    brightness= []
    
    for row in csv_file:

            try:
                latitude = float(row[latitude_index])
                longitude = float(row[longitude_index])
                bright = float(row[brightness_index])
            except ValueError:
                print(f"Missing data for brightness")
            else:
                latitudes.append(latitude)
                longitudes.append(longitude)
                brightness.append(bright)
            
    return latitudes, longitudes, brightness





main()