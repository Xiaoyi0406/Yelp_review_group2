#
library(jsonlite)
library(tibble)
library(dplyr)
yelp.bus <- stream_in(file("business_train.json"))
str(yelp.bus)
yelp=yelp.bus
#flat the net structure from json
yelp_flat <- flatten(yelp)
str(yelp_flat)
#tidy as dataframe
yelp_tbl <- as_data_frame(yelp_flat)
yelp_tbl
yelp_tbl=yelp_tbl %>% mutate(categories = as.character(categories)) %>% select(-starts_with("hours"), -starts_with("postal code"),-starts_with("latitude"),-starts_with("longitude"),-starts_with("attributes"))
yelp_tbl
write.csv(yelp_tbl, file = "business_train.csv",row.names=FALSE)
#########
