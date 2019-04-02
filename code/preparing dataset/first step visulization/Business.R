library(data.table)
library(dplyr)
business=fread("business_train.csv")
business %>% colnames
business$order=1:dim(business)[1]
head(business)
restaurant=business %>% filter(grepl("restaurants",ignore.case = T,categories))
address=restaurant %>% select(state,city,latitude,longitude,order,business_id,categories)
america=address %>% 
  filter(grepl("AL|AK|AZ|AR|AA|AE|AP|CA|CO|CT|DE|DC|FL|GA|HI|ID|IL|IN|IA|KS|KY|
               LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|
               SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY",state))
canada=address %>% 
  filter(grepl("AB|BC|MB|NB|NL|NT|NS|NU|ON|PE|QC|SK|YT",state))
usca.address=rbind(america,canada)
restaurant=restaurant[usca.address$order,]
usca.address=usca.address %>% filter(longitude>=-130&longitude<=-60)
america=usca.address %>% 
  filter(grepl("AL|AK|AZ|AR|AA|AE|AP|CA|CO|CT|DE|DC|FL|GA|HI|ID|IL|IN|IA|KS|KY|
               LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|
               SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY",state))
canada=usca.address %>% 
  filter(grepl("AB|BC|MB|NB|NL|NT|NS|NU|ON|PE|QC|SK|YT",state))
america=america %>% filter(state!="AK"&state!="IN"&state!="NY"&state!="VA")
usca.address=rbind(america,canada)
wrong1=america %>% filter(longitude>=-121&longitude<=-119)
##wrong coordinates
wrong2=america %>% filter(longitude>=-101&longitude<=-97)
##wrong coordinates
wrong3=america %>% filter(longitude>=-75&longitude<=-74)
##wrong coordinates
wrong4=america %>% filter(longitude>=-77.2&longitude<=-76&latitude>=38.6&latitude<=39.6)
wrong=rbind(wrong1,wrong2,wrong3,wrong4)
america=america[-which(america$order%in%wrong$order),]
america %>% head

madison=restaurant %>% select(state,city,longitude,latitude,address) 
madison=madison %>% filter(state=="WI",city=="Madison")
table(madison$city)
