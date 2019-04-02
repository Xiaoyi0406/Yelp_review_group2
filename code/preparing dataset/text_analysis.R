library(data.table)
library(dplyr)
library(stringr)
rm(list=ls())
setwd("E:/UWM/STAT 628/module2/data")
ab.res=fread("ab_res.csv",select = 2:58)
az.res=fread("az_res.csv",select = 2:58)
il.res=fread("il_res.csv",select = 2:58)
nc.res=fread("nc_res.csv",select = 2:58)
nv.res=fread("nv_res.csv",select = 2:58)
oh.res=fread("oh_res.csv",select = 2:58)
on.res=fread("on_res.csv",select = 2:58)
pa.res=fread("pa_res.csv",select = 2:58)
qc.res=fread("qc_res.csv",select = 2:58)
wi.res=fread("wi_res.csv",select = 2:58)
all.res=rbind(ab.res,az.res,il.res,nc.res,nv.res,oh.res,on.res,pa.res,qc.res,wi.res)

##coffee
coffee=all.res %>% filter(grepl("star\\s*bucks",ignore.case = T,name)|
                            grepl("tim\\s*hortons",ignore.case = T,name)|
                            grepl("dunkin\\s*donuts",ignore.case = T,name)|
                            grepl("panera\\s*bread",ignore.case = T,name)|
                            grepl("denny\\s*s",ignore.case = T,name)|
                            grepl("second\\s*cup",ignore.case = T,name)|
                            grepl("denny'\\s*s",ignore.case = T,name)|
                            grepl("dunkin'\\s*s",ignore.case = T,name))
coffee$name %>% table
##burger
burger=all.res %>% filter(grepl("McDonald",ignore.case = T,name)|
                            grepl("burger\\s*king",ignore.case = T,name)|
                            grepl("wendy's",ignore.case = T,name)|
                            grepl("KFC",ignore.case = T,name)|
                            grepl("DQ",ignore.case = F,name)|
                            grepl("Dairy\\s*queen",ignore.case = T,name)|
                            grepl("popeyes\\s*louisiana",ignore.case = T,name)|
                            grepl("arby's",ignore.case = T,name)|
                            grepl("5\\s*guys",ignore.case = T,name)|
                            grepl("five\\s*guys",ignore.case = T,name)|
                            grepl("jack\\s*in\\s*the\\s*box",ignore.case = T,name)|
                            grepl("sonic\\s*drive",ignore.case = T,name))
burger %>% filter(name=="McDonald's") %>% dim
burger$name %>% table
##pizza
pizza=all.res %>% filter(grepl("pizza\\s*hut",ignore.case = T,name)|
                           grepl("domino's\\s*pizza",ignore.case = T,name)|
                           grepl("papa\\s*john",ignore.case = T,name)|
                           grepl("little\\s*caesars",ignore.case = T,name)|
                           grepl("pizza\\s*pizza",ignore.case = T,name)|
                           grepl("domino's",ignore.case = T,name))
pizza$name %>% table
###sandwich
sandwich=all.res %>% filter(grepl("subway",ignore.case = T,name)|
                              grepl("jimmy\\s*john",ignore.case = T,name)|
                              grepl("jersey\\s*mike",ignore.case = T,name))
sandwich$name %>% table
###regional
regional=all.res %>% filter(grepl("taco\\s*bell",ignore.case = T,name)|
                              grepl("chipotle",ignore.case = T,name)|
                              grepl("panda\\s*exp",ignore.case = T,name)|
                              grepl("taco\\s*taco",ignore.case = T,name))
regional$name %>% table
###shop
shop=all.res %>% filter(grepl("walgreens",ignore.case = T,name)|
                          grepl("seven-11",ignore.case = T,name)|
                          grepl("7.eleven",ignore.case = T,name)|
                          grepl("walmart",ignore.case = T,name)|
                          grepl("quik\\s*trip",ignore.case = T,name))
shop$name %>% table
all.res$name %>% table %>% sort(decreasing = T) %>% head(30)
write.csv(coffee,"coffee.csv")
write.csv(burger,"burger.csv")
write.csv(pizza,"pizza.csv")
write.csv(sandwich,"sandwich.csv")
write.csv(regional,"regional.csv")
write.csv(shop,"shop.csv")
