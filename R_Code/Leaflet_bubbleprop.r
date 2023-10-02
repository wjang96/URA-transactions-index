library(leaflet)
library(htmltools)

#read three bedder condo csv
project_transactions_df = read.csv('transactions_three_bedder_23q3.csv')

# Define color palette
pal <- colorFactor(c('#4AC6B7','#C61951','#FF7070',"lightgreen"), domain = c("Low", "Average", "High", "Extreme"))

# Create html for new lines in label
labs <- lapply(seq(nrow(project_transactions_df)), function(i) {
     paste0( '<b>Project Name: </b>', project_transactions_df[i, "project"], '</br>',
             '<b>Average Rent ($): </b>',project_transactions_df[i, "rent"],'</br>',
            '<b>No of Bedroom: </b>',project_transactions_df[i, "noOfBedRoom"],'</br>',
             '<b>District : </b>',project_transactions_df[i, "district"],'</br>')
 })

m <- leaflet(project_transactions_df) %>%
    setView(lng = 103.8198, lat = 1.3521, zoom = 12) %>%
    setMaxBounds( lng1 = 103.600250,
                   lat1 = 1.202674,
                   lng2 = 104.027344,
                   lat2 = 1.484121 )%>%
    addTiles(options=tileOptions(opacity=0.6)) %>%  
    addCircles(lng=~long, lat=~lat,
                radius=~sqrt(rent/10),
                color=~pal(rentCategory),
                weight=2,
                label=lapply(labs, HTML),
                stroke=TRUE,opacity=0.8,fillOpacity=0.5,
                #clusterOptions=markerClusterOptions(),
                layerId = ~project) %>%
    addLegend("topright", pal = pal,
               values = ~rentCategory,
               title = "Rent Category",
               opacity = 1)
m