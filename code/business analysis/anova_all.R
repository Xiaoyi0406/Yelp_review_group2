rm(list=ls())
library(data.table)
library(dplyr)
library(stringr)
library(ggplot2)

type=list(burger=c("mcdonald","burger\\\\s*king","wendy","KFC","Dairy\\\\s*queen","popeyes\\\\s*louisiana",
                   "arby","five\\\\s*guys","jack\\\\s*in\\\\s*the\\\\s*box","sonic\\\\s*drive"),
          pizza=c("pizza\\\\s*hut","domino","papa\\\\s*john","little\\\\s*caesars",
                  "pizza\\\\s*pizza"),
          coffee=c("star\\\\s*bucks","tim\\\\s*hortons","dunkin","panera\\\\s*bread",
                   "denny","second\\\\s*cup"),
          sandwich=c("subway","jimmy\\\\s*john","jersey\\\\s*mike"),
          regional=c("taco\\\\s*bell","chipotle","panda\\\\s*exp"))
typename=list(burger=c("mcdonalds","burgerking","wendys","kfc","DQ","popeyes","arbys","fiveguys",
                       "jackinthebox","sonicdrive"),
              pizza=c("pizzahut","dominos","papajohn","littlecaesars","pizzapizza"),
              coffee=c("starbucks","timhortons","dunkin","panerabread","dennys","secondcup"),
              sandwich=c("subway","jimmyjohn","jerseymike"),
              regional=c("tacobell","chipotle","pandaexp"))
k=1;l=1;m=1

for(i in 1:5){
  eval(parse(text=paste(paste(names(typename)[i]),'=fread(\'',
                        paste(names(typename)[i],'.csv',sep = ""),
                        '\',select=c(\'business_id\',\'state\',\'name\',\'circle\',\'stars\',\'score_food\',\'score_service\'))',
                        sep="")))
  for(j in (1:length(type[[i]]))){
    
    
    
    eval(parse(text=paste(typename[[i]][j],'=filter(',names(type)[i],
                          ',grepl(\'',type[[i]][j],'\',ignore.case=T,name)) ',sep="")))
    eval(parse(text=paste(paste(typename[[i]][j],'mean',sep=""),'=summarize(group_by(',
                          typename[[i]][j],',business_id),mean(stars))',sep="")))
    eval(parse(text=paste(typename[[i]][j],'=left_join(',typename[[i]][j],',',
                          paste(typename[[i]][j],'mean',sep=""),',by=\'business_id\')'  ,sep="")))
    ###### Avg_star
    eval(parse(text=paste(paste(typename[[i]][j],'_avg',sep=""),'=select(',typename[[i]][j],
                          ',business_id,state,circle,\`mean(stars)\`)',sep="")))
    eval(parse(text=paste(paste(typename[[i]][j],'_avg',sep=""),'=unique(',
                          paste(typename[[i]][j],'_avg',sep=""),')',sep="")))
    eval(parse(text=paste(paste('anova.',typename[[i]][j],sep=""),
                          '=anova(lm(\`mean(stars)\`~state*circle,data=',
                          paste(typename[[i]][j],'_avg',sep=""),'))',sep="")))
    eval(parse(text=paste(paste('state.',typename[[i]][j],sep=""),
                          '=summarize(group_by(',paste(typename[[i]][j],'_avg',sep=""),
                          ',state),star=mean(\`mean(stars)\`)) ',sep="")))
    eval(parse(text=paste(paste('circle.',typename[[i]][j],sep=""),
                          '=summarize(group_by(',paste(typename[[i]][j],'_avg',sep=""),
                          ',circle),star=mean(\`mean(stars)\`)) ',sep="")))
    ###### food_score
    eval(parse(text=paste(paste(typename[[i]][j],'_food',sep=""),'=mutate(',typename[[i]][j],
                          ',foodscore=gsub(pattern=\'\\\\[(.+)\\\\]\',replacement=\'\\\\1\',x=score_food))',sep="")))
    eval(parse(text=paste(paste(typename[[i]][j],'_food',sep=""),'=filter(',
                          paste(typename[[i]][j],'_food',sep=""),',foodscore!=\'None\')',sep="")))
    eval(parse(text=paste(paste(typename[[i]][j],'_food',sep=""),'=mutate(',paste(typename[[i]][j],'_food',sep=""),
                          ',foodscore=str_extract_all(gsub(pattern=\'\\\\[(.+)\\\\]\',replacement=\'\\\\1\',x=score_food),\'[0-9]\'))',
                          sep="")))
    eval(parse(text=paste(paste(typename[[i]][j],'_food',sep=""),'=mutate(',paste(typename[[i]][j],'_food',sep=""),
                          ',foodscore=unlist(lapply(lapply(foodscore,as.numeric),mean)))',sep="")))
    eval(parse(text=paste(paste(typename[[i]][j],'_food',sep=""),'=filter(',
                          paste(typename[[i]][j],'_food',sep=""),',!is.na(foodscore))',sep="")))
    eval(parse(text=paste(paste('anovafood.',typename[[i]][j],sep=""),
                          '=anova(lm(foodscore~state*circle,data=',
                          paste(typename[[i]][j],'_food',sep=""),'))',sep="")))
    eval(parse(text=paste(paste('statefood.',typename[[i]][j],sep=""),
                          '=summarize(group_by(',paste(typename[[i]][j],'_food',sep=""),
                          ',state),score=mean(foodscore)) ',sep="")))
    eval(parse(text=paste(paste('circlefood.',typename[[i]][j],sep=""),
                          '=summarize(group_by(',paste(typename[[i]][j],'_food',sep=""),
                          ',circle),score=mean(foodscore)) ',sep="")))
    ##### Service score
    eval(parse(text=paste(paste(typename[[i]][j],'_service',sep=""),'=mutate(',typename[[i]][j],
                          ',servscore=gsub(pattern=\'\\\\[(.+)\\\\]\',replacement=\'\\\\1\',x=score_service))',sep="")))
    eval(parse(text=paste(paste(typename[[i]][j],'_service',sep=""),'=filter(',
                          paste(typename[[i]][j],'_service',sep=""),',servscore!=\'None\')',sep="")))
    eval(parse(text=paste(paste(typename[[i]][j],'_service',sep=""),'=mutate(',paste(typename[[i]][j],'_service',sep=""),
                          ',servscore=str_extract_all(gsub(pattern=\'\\\\[(.+)\\\\]\',replacement=\'\\\\1\',x=score_service),\'[0-9]\'))',
                          sep="")))
    eval(parse(text=paste(paste(typename[[i]][j],'_service',sep=""),'=mutate(',paste(typename[[i]][j],'_service',sep=""),
                          ',servscore=unlist(lapply(lapply(servscore,as.numeric),mean)))',sep="")))
    eval(parse(text=paste(paste(typename[[i]][j],'_service',sep=""),'=filter(',
                          paste(typename[[i]][j],'_service',sep=""),',!is.na(servscore))',sep="")))
    eval(parse(text=paste(paste('anovaserv.',typename[[i]][j],sep=""),
                          '=anova(lm(servscore~state*circle,data=',
                          paste(typename[[i]][j],'_service',sep=""),'))',sep="")))
    eval(parse(text=paste(paste('stateserv.',typename[[i]][j],sep=""),
                          '=summarize(group_by(',paste(typename[[i]][j],'_service',sep=""),
                          ',state),score=mean(servscore)) ',sep="")))
    eval(parse(text=paste(paste('circleserv.',typename[[i]][j],sep=""),
                          '=summarize(group_by(',paste(typename[[i]][j],'_service',sep=""),
                          ',circle),score=mean(servscore)) ',sep="")))
    
    
    print(paste(i,j))
  }
}

###result
###### review average star
typename
aaa="panerabread"
eval(parse(text=paste('print(anova.',aaa,')',sep='')))
eval(parse(text=paste('print(anovafood.',aaa,')',sep='')))
eval(parse(text=paste('print(anovaserv.',aaa,')',sep='')))

eval(parse(text=paste('print(anova.',aaa,')',sep='')))
eval(parse(text=paste('print(state.',aaa,')',sep='')))
eval(parse(text=paste('ggplot(state.',aaa,
                      ',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
eval(parse(text=paste('print(circle.',aaa,')',sep='')))
eval(parse(text=paste('ggplot(circle.',aaa,
                      ',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
###### food score
eval(parse(text=paste('print(anovafood.',aaa,')',sep='')))
eval(parse(text=paste('print(statefood.',aaa,')',sep='')))
eval(parse(text=paste('ggplot(statefood.',aaa,
                      ',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
eval(parse(text=paste('print(circlefood.',aaa,')',sep='')))
eval(parse(text=paste('ggplot(circlefood.',aaa,
                      ',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
###### service score
eval(parse(text=paste('print(anovaserv.',aaa,')',sep='')))
eval(parse(text=paste('print(stateserv.',aaa,')',sep='')))
eval(parse(text=paste('ggplot(stateserv.',aaa,
                      ',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
eval(parse(text=paste('print(circleserv.',aaa,')',sep='')))
eval(parse(text=paste('ggplot(circleserv.',aaa,
                      ',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))



mcdonalds_food %>% head
panerabread_service %>% head
bbb=fread("coffee.csv") 
bbb %>% colnames
bbb %>% select(name,state,circle,service_NN,service_JJ,service_RB,score_service) %>% 
  filter(grepl("panera",ignore.case = T,name),circle==1) %>% head



