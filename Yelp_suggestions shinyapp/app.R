rm(list = ls())
#install.packages("shinythemes")
#library(shinythemes)
library(shiny)
#install.packages("plotGoogleMaps")
#library(plotGoogleMaps)
library(ggplot2)
library(data.table)
library(dplyr)
library(stringr)



small = read.csv("small.csv",row.names = 1)
small$name = as.character(small$name)
small$state = as.character(small$state)
sdist = read.csv("sdist.csv",row.names = 1)
burstar = read.csv("burger_star.csv",row.names = 1)
pizstar = read.csv("pizza_star.csv",row.names = 1)
cofstar = read.csv("coffee_star.csv",row.names = 1)
sandstar = read.csv("sandwich_star.csv",row.names = 1)
regstar = read.csv("regional_star.csv",row.names = 1)
shopstar = read.csv("shop_star.csv",row.names = 1)
allstar = read.csv("allstar.csv",row.names = 1)
result = read.csv("result.csv")
result$name = as.character(result$name)
result$option1 = as.character(result$option1)
result$option2 = as.character(result$option2)
result$significance = as.character(result$significance)
result$class = as.character(result$class)
all_avgscore = read.csv("all_avgscore.csv")



ui <- fluidPage(
  #shinythemes::themeSelector(),
  headerPanel('Yelp Suggestions System'),
 
  sidebarPanel(
    numericInput("id", label = p("Business ID:"), value = 0, min = 0),
    hr(),
    strong(htmlOutput("txtoutname"),style = "font-size: 20px;"),
    strong(htmlOutput("txtoutavgstar"),style = "font-size: 20px;"),
    hr(),
    selectInput("name", "Please select a restaurant:",choices = c("Arby's","Burger King","Dairy Queen","Five Guys","Jack In the Box","KFC", "Pizza Hut",                     
                                                                  "McDonald's","Popeyes Louisiana Kitchen","Sonic Drive","Wendy's","Denny's",
                                                                  "Dunkin' Donuts","Panera Bread","Second Cup","Starbucks","Tim Hortons",
                                                                  "Domino's Pizza","Little Caesars Pizza","Papa John's","Chipotle","Panda Express",
                                                                  "Taco Bell","Jersey Mike's Sub","Jimmy John's","Subway","Pizza Pizza")),
    hr(),
    radioButtons("choix1", "Please choose one aspect:",
                 c("Review" = "review","Food" = "food","Service" = "service"),inline = T),
    hr(),
    helpText(p("If you have further question about this app,please contact: "),
             p("lzeng32@wisc.edu",style = "font-size: 12px;"),
             p("kzhao46@wisc.edu",style = "font-size: 12px;"),
             p("chen777@wisc.edu",style = "font-size: 12px;"),
             p("cliu523@wisc.edu",style = "font-size: 12px;"))
  ),
  
  
  # Main panel for displaying outputs ----
  mainPanel(
    tabsetPanel(type = "tabs",
                tabPanel("Star distribution", plotOutput("stardist1"),plotOutput("stardist2")),
                tabPanel("General Suggestions", verbatimTextOutput("gsuggestion1"),plotOutput("gsuggestion2"),plotOutput("gsuggestion3")),
                tabPanel("Specific Suggestions", verbatimTextOutput("ssuggestion1"),verbatimTextOutput("ssuggestion2"),verbatimTextOutput("ssuggestion3")))
  )
)



server <- function(input, output) {
  # Avg score food
  output$ssuggestion1 <- renderText({
    paste("Food score:",round(all_avgscore[which(all_avgscore$business_id == input$id),]$food_mean,1),
          "    Service score:  ",round(all_avgscore[which(all_avgscore$business_id == input$id),]$sev_mean,1))
  })

  # Score Suggestion
  output$ssuggestion2 <- renderText({
    if (input$id == 0){
      paste("Please input id.")
    }else{
      if (all_avgscore[which(all_avgscore$business_id == input$id),]$food_mean<=2){
        paste("The customers seem to be very unsatisfied with your food. Your restaurant still need many efforts in food.")
      }else if(all_avgscore[which(all_avgscore$business_id == input$id),]$food_mean>2 & all_avgscore[which(all_avgscore$business_id == input$id),]$food_mean<=4){
        paste("The customers seem to be ok with your food. Your restaurant still need some efforts in food.")
      }else if(all_avgscore[which(all_avgscore$business_id == input$id),]$food_mean>4 & all_avgscore[which(all_avgscore$business_id == input$id),]$food_mean<=5){
        paste("The customers love your food! Please maintain the level!")
      }
    }
  })
  
  output$ssuggestion3 <- renderText({
    if (input$id == 0){
      paste("Please input id.")
    }else{
      if (all_avgscore[which(all_avgscore$business_id == input$id),]$sev_mean<=2){
        paste("The customers seem to be unpleased with your service. Your restaurant still need many efforts in service.")
      }else if(all_avgscore[which(all_avgscore$business_id == input$id),]$sev_mean>2 & all_avgscore[which(all_avgscore$business_id == input$id),]$sev_mean<=4){
        paste("The customers seem to be ok with your service. Your restaurant still need some efforts in service")
      }else if(all_avgscore[which(all_avgscore$business_id == input$id),]$sev_mean>4 & all_avgscore[which(all_avgscore$business_id == input$id),]$sev_mean<=5){
        paste("The customers love your service! Please maintain the level!")
      }
    }
  })
  
  
  
  # General sugg significance
  output$gsuggestion1 <- renderText({
    a = (result$name == input$name & result$option1 == input$choix1 )
    b = (result$name == input$name & result$option1 == input$choix1)
    c = (result$name == input$name & result$option1 == input$choix1)
    d = (result[which(a & result$option2 == "state"),]$significance == "has influence")
    e = (result[which(a & result$option2 == "state"),]$significance == "no influence")
    f = (result[which(a & result$option2 == "circle"),]$significance == "has influence")
    g = (result[which(a & result$option2 == "circle"),]$significance == "no influence")
    if (input$choix1 == "review"){
      if(d & f){ #T,T
        paste("Influence?",'\n',"State: ", result[which(a & result$option2 == "state"),]$significance,
              "    Circle:  ",result[which(a & result$option2 == "circle"),]$significance, '\n','\n',
              "The potential business owners should run their newbusiness in the states rank by the front, because people in those states are more likely to enjoy this restaurant.",'\n',
              "For circle, it means whether open in business district may influence the review stars they receive. Potential owners have to weigh the beneficial and cost of business district.")
      }else if (d & g){ #T,F
        paste("Influence?",'\n',"State: ", result[which(a & result$option2 == "state"),]$significance,
              "    Circle:  ",result[which(a & result$option2 == "circle"),]$significance, '\n','\n',
              "The potential business owners should run their newbusiness in the states rank by the front, because people in those states are more likely to enjoy this restaurant.",'\n','\n',
              "There is no significant difference between in or out a business circle.")
      }else if(e & f){ #F,T
        paste("Influence?",'\n',"State: ", result[which(a & result$option2 == "state"),]$significance,
              "    Circle:  ",result[which(a & result$option2 == "circle"),]$significance, '\n','\n',
              "There is no significant difference between in a specific state or another one.",'\n','\n',
              "For circle, it means whether open in business district may influence the review stars they receive. Potential owners have to weigh the beneficial and cost of business district.")
      }else if(e & g){ #F,F
        paste("Influence?",'\n',"State: ", result[which(a & result$option2 == "state"),]$significance,
              "    Circle:  ",result[which(a & result$option2 == "circle"),]$significance, '\n','\n',
              "There is no significant difference between in a specific state or another one.",'\n','\n',
              "There is no significant difference between in or out a business circle.")
      }
    }else if (input$choix1 == "food"){
      if(d & f){ #T,T
        paste("Influence?",'\n',"State: ", result[which(a & result$option2 == "state"),]$significance,
              "    Circle:  ",result[which(a & result$option2 == "circle"),]$significance, '\n','\n',
              "For state,it indicates the flavor may differ among states, and also people's taste may differ. Potential owners should choose states rank by the front.",'\n','\n',
              "For circle, it means the flavor inside/outside business circle differs. Owners in lower score group should 
              introspect what's wrong with their flavor.")
      }else if (d & g){ #T,F
        paste("Influence?",'\n',"State: ", result[which(a & result$option2 == "state"),]$significance,
              "    Circle:  ",result[which(a & result$option2 == "circle"),]$significance, '\n','\n',
              "For state, it indicates the flavor may differ among states, and also people's taste may differ. Potential owners should choose states rank by the front.",'\n','\n',
              "There is no significant difference between in or out a business circle.")
      }else if(e & f){ #F,T
        paste("Influence?",'\n',"State: ", result[which(a & result$option2 == "state"),]$significance,
              "    Circle:  ",result[which(a & result$option2 == "circle"),]$significance, '\n','\n',
              "There is no significant difference between in a specific state or another one.",'\n','\n',
              "For circle,it means the flavor inside/outside business circle differs. Owners in lower score group should introspect what's wrong with their flavor.")
      }else if(e & g){ #F,F
        paste("Influence?",'\n',"State: ", result[which(a & result$option2 == "state"),]$significance,
              "    Circle:  ",result[which(a & result$option2 == "circle"),]$significance, '\n','\n',
              "There is no significant difference between in a specific state or another one.",'\n','\n',
              "There is no significant difference between in or out a business circle.")
      }
    }else if(input$choix1 == "service"){
      if(d & f){ #T,T
        paste("Influence?",'\n',"State: ", result[which(a & result$option2 == "state"),]$significance,
              "    Circle:  ",result[which(a & result$option2 == "circle"),]$significance, '\n','\n',
              "For state, it indicates the service may differ among states, and also people's tolerance may differ. Potential owners should choose states rank by  the front.",'\n','\n',
              "For circle, it means the service inside/outside business circle differs. Owners in lower score group should introspect what's wrong with their service.")
      }else if (d & g){ #T,F
        paste("Influence?",'\n',"State: ", result[which(a & result$option2 == "state"),]$significance,
              "    Circle:  ",result[which(a & result$option2 == "circle"),]$significance, '\n','\n',
              "For state, it indicates the service may differ among states, and also people's tolerance may differ. Potential owners should choose states rank by the front.",'\n','\n',
              "There is no significant difference between in or out a business circle.")
      }else if(e & f){ #F,T
        paste("Influence?",'\n',"State: ", result[which(a & result$option2 == "state"),]$significance,
              "    Circle:  ",result[which(a & result$option2 == "circle"),]$significance, '\n','\n',
              "There is no significant difference between in a specific state or another one.",'\n','\n',
              "For circle, it means the service inside/outside business circle differs. Owners in lower score group should introspect what's wrong with their service.")
      }else if(e & g){ #F,F
        paste("Influence?",'\n',"State: ", result[which(a & result$option2 == "state"),]$significance,
              "    Circle:  ",result[which(a & result$option2 == "circle"),]$significance, '\n','\n',
              "There is no significant difference between in a specific state or another one.",'\n','\n',
              "There is no significant difference between in or out a business circle.")
      }
    }
    
  })
  
  
  #General sugg plot
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
    }
  }
  
  
  
  
  
  
  
  
  output$gsuggestion2 <- renderPlot({
    
    if (input$name == "McDonald's"){
      aaa="mcdonalds"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Burger King"){
      aaa="burgerking"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Wendy's"){
      aaa="wendys"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "KFC"){
      aaa="kfc"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Dairy Queen"){
      aaa="DQ"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Popeyes Louisiana Kitchen"){
      aaa="popeyes"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Arby's"){
      aaa="arbys"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Five Guys"){
      aaa="fiveguys"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Jack In the Box"){
      aaa="jackinthebox"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Sonic Drive"){
      aaa="sonicdrive"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Pizza Hut"){
      aaa="pizzahut"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Domino's Pizza"){
      aaa="dominos"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Papa John's"){
      aaa="papajohn"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Pizza Pizza"){
      aaa="pizzapizza"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Starbucks"){
      aaa="starbucks"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Tim Hortons"){
      aaa="timhortons"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Dunkin' Donuts"){
      aaa="dunkin"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Panera Bread"){
      aaa="panerabread"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Denny's"){
      aaa="dennys"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Second Cup"){
      aaa="secondcup"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Subway"){
      aaa="subway"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Jimmy John's"){
      aaa="jimmyjohn"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Jersey Mike's Sub"){
      aaa="jerseymike"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Taco Bell"){
      aaa="tacobell"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Chipotle"){
      aaa="chipotle"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }else if(input$name == "Panda Express"){
      aaa="pandaexp"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(state.',aaa,',aes(x=reorder(state,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(statefood.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(stateserv.',aaa,',aes(x=reorder(state,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
        
      }
    }
    
  })
  
  
  
  output$gsuggestion3 <-  renderPlot({
   
    if (input$name == "McDonald's"){
      aaa="mcdonalds"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      } 
    }else if(input$name == "Burger King"){
      aaa="burgerking"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Wendy's"){
      aaa="wendys"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "KFC"){
      aaa="kfc"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Dairy Queen"){
      aaa="DQ"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Popeyes Louisiana Kitchen"){
      aaa="popeyes"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Arby's"){
      aaa="arbys"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Five Guys"){
      aaa="fiveguys"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Jack In the Box"){
      aaa="jackinthebox"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Sonic Drive"){
      aaa="sonicdrive"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Pizza Hut"){
      aaa="pizzahut"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Domino's Pizza"){
      aaa="dominos"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Papa John's"){
      aaa="papajohn"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Pizza Pizza"){
      aaa="pizzapizza"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Starbucks"){
      aaa="starbucks"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Tim Hortons"){
      aaa="timhortons"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Dunkin' Donuts"){
      aaa="dunkin"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Panera Bread"){
      aaa="panerabread"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Denny's"){
      aaa="dennys"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Second Cup"){
      aaa="secondcup"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Subway"){
      aaa="subway"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Jimmy John's"){
      aaa="jimmyjohn"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Jersey Mike's Sub"){
      aaa="jerseymike"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Taco Bell"){
      aaa="tacobell"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Chipotle"){
      aaa="chipotle"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }else if(input$name == "Panda Express"){
      aaa="pandaexp"
      if (input$choix1 == "review"){
        eval(parse(text=paste('ggplot(circle.',aaa,',aes(x=reorder(circle,-star),y=star))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "food"){
        eval(parse(text=paste('ggplot(circlefood.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }else if (input$choix1 == "service"){
        eval(parse(text=paste('ggplot(circleserv.',aaa,',aes(x=reorder(circle,-score),y=score))+geom_bar(stat=\'identity\')',sep="")))
      }
    }
    
  })
  
  
  
  # Name and avgstar
  output$txtoutname <- renderText({paste("Name:",small[which(small$business_id == input$id),][2][1,1])})
  output$txtoutavgstar <- renderText({paste("Average star:",round(small[which(small$business_id == input$id),][4][1,1],1))})
  
  # Star dist
  output$stardist1 <- renderPlot({
    if (input$id == 0){
      paste("please input id.")
    }else{
      ggplot(data=sdist[which(sdist$business_id == input$id),], aes(stars)) + 
        geom_histogram(col = "white",binwidth = 1,fill="#56B4E9",alpha = 0.8) + 
        ggtitle("Star distribution of this restaurant")+
        labs(x="Stars", y="Count") + theme(axis.title.x  = element_text(size = 20)) +
        theme(axis.title.y  = element_text(size = 20)) +
        theme(axis.text.x = element_text(size = 15)) +
        theme(axis.text.y = element_text(size = 15)) +
        theme(plot.title = element_text(size = 20, hjust = 0.5))
    }
    
    
    
  })
  
  output$stardist2 <- renderPlot({
    if (input$id == 0){
      paste("please input id.")
    }else{
      if (allstar[which(allstar$business_id == input$id),][,2] == 1){
        ggplot(data=burstar, aes(stars)) + 
          geom_histogram(col = "white",binwidth = 1,fill="#E69F00",alpha = 0.8) + 
          ggtitle("Star distribution")+
          labs(x="Stars", y="Count") + theme(axis.title.x  = element_text(size = 20)) +
          theme(axis.title.y  = element_text(size = 20)) +
          theme(axis.text.x = element_text(size = 15)) +
          theme(axis.text.y = element_text(size = 15)) +
          theme(plot.title = element_text(size = 20, hjust = 0.5)) 
      }else if (allstar[which(allstar$business_id == input$id),][,2] == 2){
        ggplot(data=pizstar, aes(stars)) + 
          geom_histogram(col = "white",binwidth = 1,fill="#E69F00", alpha = 0.8) + 
          ggtitle("Star distribution")+
          labs(x="Stars", y="Count") + theme(axis.title.x  = element_text(size = 20)) +
          theme(axis.title.y  = element_text(size = 20)) +
          theme(axis.text.x = element_text(size = 15)) +
          theme(axis.text.y = element_text(size = 15)) +
          theme(plot.title = element_text(size = 20, hjust = 0.5)) 
      }else if (allstar[which(allstar$business_id == input$id),][,2] == 3){
        ggplot(data=cofstar, aes(stars)) + 
          geom_histogram(col = "white", binwidth = 1,fill="#E69F00", alpha = 0.8) + 
          ggtitle("Star distribution")+
          labs(x="Stars", y="Count") + theme(axis.title.x  = element_text(size = 20)) +
          theme(axis.title.y  = element_text(size = 20)) +
          theme(axis.text.x = element_text(size = 15)) +
          theme(axis.text.y = element_text(size = 15)) +
          theme(plot.title = element_text(size = 20, hjust = 0.5)) 
      }else if (allstar[which(allstar$business_id == input$id),][,2] == 4){
        ggplot(data=sandstar, aes(stars)) + 
          geom_histogram(col = "white",binwidth = 1, fill="#E69F00", alpha = 0.8) + 
          ggtitle("Star distribution")+
          labs(x="Stars", y="Count") + theme(axis.title.x  = element_text(size = 20)) +
          theme(axis.title.y  = element_text(size = 20)) +
          theme(axis.text.x = element_text(size = 15)) +
          theme(axis.text.y = element_text(size = 15)) +
          theme(plot.title = element_text(size = 20, hjust = 0.5)) 
      }else if (allstar[which(allstar$business_id == input$id),][,2] == 5){
        ggplot(data=regstar, aes(stars)) + 
          geom_histogram(col = "white",binwidth = 1,fill="#E69F00", alpha = 0.8) + 
          ggtitle("Star distribution")+
          labs(x="Stars", y="Count") + theme(axis.title.x  = element_text(size = 20)) +
          theme(axis.title.y  = element_text(size = 20)) +
          theme(axis.text.x = element_text(size = 15)) +
          theme(axis.text.y = element_text(size = 15)) +
          theme(plot.title = element_text(size = 20, hjust = 0.5)) 
      }else if (allstar[which(allstar$business_id == input$id),][,2] == 6){
        ggplot(data=shopstar, aes(stars)) + 
          geom_histogram(col = "white",binwidth = 1,fill="#E69F00", alpha = 0.8) + 
          ggtitle("Star distribution")+
          labs(x="Stars", y="Count") + theme(axis.title.x  = element_text(size = 20)) +
          theme(axis.title.y  = element_text(size = 20)) +
          theme(axis.text.x = element_text(size = 15)) +
          theme(axis.text.y = element_text(size = 15)) +
          theme(plot.title = element_text(size = 20, hjust = 0.5)) 
      }
    }
    
    
    
})

}


shinyApp(ui = ui, server = server)
#"<font color=\"#FF0000\"><b>"
#161856
#14859
#24984



#result[which(result$name == "KFC" && result$option1 == "review" && result$option2 == "circle"),]