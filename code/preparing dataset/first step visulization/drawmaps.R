library(ggplot2)
states <- map_data("state")
gg1 <- ggplot() + 
  geom_polygon(data = states, aes(x=long, y = lat, fill=region,group = group), color = "white") + 
  coord_fixed(1.3)+
  guides(fill=FALSE)
gg1

####America and Canada
gg1 + 
  geom_point(data = usca.address, aes(x = longitude, y = latitude), color = "black", size = 1)
#### Only America
gg1+
  geom_point(data=america,aes(x=longitude,y=latitude),color="black",size=1)

east_coast=subset(states,region%in%c("wisconsin","illinois","ohio","pennsylvania","north carolina"))
east_coast %>% head
ggplot(data = east_coast) + 
  geom_polygon(aes(x = long, y = lat, fill=region,group = group), color = "black") +
  coord_fixed(1.3)+
  geom_point(dat=east_business,aes(x=longitude,y=latitude),col="black",size=1)

america$state %>% table
east_business=america[which(america$state!="AZ"&america$state!="NV"),]
which(america$state!="AZ")
east_business %>% head



counties=map_data("county")
wi_df=subset(states,region=="wisconsin")
wi_county=subset(counties,region=="wisconsin")
dane_county=subset(wi_county,subregion=="dane")
wi_base=ggplot(data = wi_df, mapping = aes(x = long, y = lat, group = group)) + 
  coord_fixed(1.3) + 
  geom_polygon(color = "black", fill = "gray")
wi_base+
geom_polygon(data = wi_county, fill = NA, color = "white") +
  geom_polygon(color = "black", fill = NA)


wi_county$subregion %>% table
ggplot(data=dane_county )+
  coord_fixed(1.3)+
  geom_polygon(col="black",aes(x=long,y=lat,group=group),fill=NA)+
  geom_point(data=madison,aes(x=longitude,y=latitude))
ggmap(get_map(location = 'wisconsin', zoom = 7)) +
  geom_point(data=madison, aes(x=lon, y=lat, size=Calls), color="orange")
str(madison)

