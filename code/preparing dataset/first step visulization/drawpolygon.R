library(data.table)
library(ggplot2)
library(ggmap)
library(retistruct)
register_google("AIzaSyAFOh7jiNE8ICsoirKJnhJ72W8RcE1m_gk")
options("googleAuthR.client_id" = "1000378592526-jumshfl5ggkpkpevqh002bg5ahvrs74s.apps.googleusercontent.com")
options("googleAuthR.client_secret" = "sEWkHBADMqPMejPSFkzx9HdP")

###AZ###
###glendale


poly_az1=data.frame(
  lon=c(-112.27203369140625,-112.25735664367676,-112.25598335266113,-112.26190567016602,-112.27435111999512,-112.27203369140625),
  lat=c(33.53052009502143,33.530305451506415,33.543183119221254,33.55863378791534,33.55276858165188,33.53052009502143)
)
poly_az2=data.frame(
  lon=c(-112.18886375427246,-112.1867823600769,-112.17643976211548,-112.17708349227905,-112.18886375427246),
  lat=c(33.55369845798816,33.54988947798968,33.54967488257032,33.553269285538214,33.55369845798816)
)
poly_az3=data.frame(
  lon=c(-112.18888521194458,-112.19051599502563,-112.18779087066649,-112.18510866165161,-112.18023777008055,-112.1808171272277,-112.18493700027466,-112.18888521194458),
  lat=c(33.58543342625494,33.58175098042201,33.57871195046158,33.58080352962138,33.582090630062915,33.583377711307584,33.58428938224093,33.58543342625494)
)

ggmap(get_map(location = 'glendale, phoenix, AZ', zoom = 12)) +
  geom_point(data=az.res, aes(x=longitude, y=latitude), color="red")+
  geom_polygon(aes(x=lon,y=lat),data=poly_az1,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az2,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az3,color="grey30",alpha=0.3)


################################ Glendale Ends ##################################################
#gilbert
poly_az4=data.frame(
  lon=c(-111.81084394454956,-111.81080102920532,-111.80380582809448,-111.80153131484985,-111.79977178573607,-111.81084394454956),
  lat=c(33.38596252217295,33.375373057362914,33.37589270585725,33.37931514078903,33.385281681672055,33.38596252217295)
)
poly_az5=data.frame(
  lon=c(-111.793595,-111.790340,-111.784731,-111.785206,-111.786354,-111.788188,-111.789690),
  lat=c(33.367084,33.373903,33.373784,33.361599,33.359672,33.354865,33.353225)
)
poly_az6=data.frame(
  lon=c(-111.788462,-111.777735,-111.768142,-111.771281,-111.788772,-111.795336,-111.798468),
  lat=c(33.340216,33.338746,33.337670,33.330966,33.327490,33.327193,33.331389)
)
ggmap(get_map(location = 'Gilbert, phoenix, AZ', zoom = 12)) +
  geom_point(data=az.res, aes(x=longitude, y=latitude), color="red")+
  geom_polygon(aes(x=lon,y=lat),data=poly_az4,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az5,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az6,color="grey30",alpha=0.3)

################################ Gilbert Ends ##################################################
#mesa

poly_az7=data.frame(
  lon=c(-111.876084,
        -111.856714,
        -111.853203,
        -111.857374,
        -111.864421,
        -111.864001),
  lat=c(33.386381,
        33.397238,
        33.378223,
        33.359961,
        33.361131,
        33.369949)
)
poly_az8=data.frame(
  lon=c(-111.817914,
        -111.793650,
        -111.733184,
        -111.734036,
        -111.757402,
        -111.782282,
        -111.783435,
        -111.789489,
        -111.791673,-111.805534,-111.813179),
  lat=c(33.376985,
        33.373899,
        33.376739,
        33.389233,
        33.388453,
        33.387489,
        33.398445,
        33.399601,
        33.388175,
        33.398001,
        33.394694)
)
poly_az9=data.frame(
  lon=c(-111.736935,
        -111.724431,
        -111.724937,
        -111.736537,
        -111.737150),
  lat=c(33.413678,
        33.414618,
        33.416865,
        33.418272,
        33.416542)
)
poly_az10=data.frame(
  lon=c(-111.696668,
        -111.684260,
        -111.680424,
        -111.683006,
        -111.694943),
  lat=c(33.395172,
        33.397124,
        33.391112,
        33.387467,
        33.387650)
)
poly_az11=data.frame(
  lon=c(-111.688241,
        -111.682842,
        -111.687029,
        -111.689365,
        -111.689322),
  lat=c(33.381642,
        33.380835,
        33.374137,
        33.379146,
        33.381216
  )
)

ggmap(get_map(location = 'Mesa, phoenix, AZ', zoom = 11)) +
  geom_point(data=az.res, aes(x=longitude, y=latitude), color="red")+
  geom_polygon(aes(x=lon,y=lat),data=poly_az7,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az8,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az9,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az10,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az11,color="grey30",alpha=0.3)

################################ Mesa Ends ##################################################
#Phoenix

poly_az12=data.frame(
  lon=c(-112.040325,
        -112.019460,
        -112.027987,
        -112.039131,
        -112.052542,
        -112.048675),
  lat=c(33.504878,
        33.508667,
        33.514547,
        33.511277,
        33.509551,
        33.504521)
)
poly_az13=data.frame(
  lon=c(-112.133559,
        -112.138466,
        -112.133699,
        -112.129176,
        -112.129254,
        -112.133053),
  lat=c(33.521670,
        33.525497,
        33.528916,
        33.527600,
        33.523369,
        33.522477)
)
poly_az14=data.frame(
  lon=c(-112.077530,
        -112.075321,
        -112.065422,
        -112.061525,
        -112.064359,
        -112.084455,
        -112.084837,
        -112.081605),
  lat=c(33.478269,
        33.473489,
        33.469560,
        33.472845,
        33.481085,
        33.479670,
        33.486703,
        33.491179)
)
poly_az15=data.frame(
  lon=c(-112.072994,
        -112.068776,
        -112.072912,
        -112.075391),
  lat=c(33.508130,
        33.509561,
        33.511853,
        33.509433)
)
poly_az16=data.frame(
  lon=c(-112.064666,
        -112.061305,
        -112.064435,
        -112.068375),
  lat=c(33.520795,
        33.517668,
        33.515621,
        33.518381)
)
ggmap(get_map(location = 'phoenix, AZ', zoom = 11)) +
  geom_point(data=az.res, aes(x=longitude, y=latitude), color="red")+
  geom_polygon(aes(x=lon,y=lat),data=poly_az12,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az13,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az14,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az15,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az16,color="grey30",alpha=0.3)
################# Phoenix Ends ########################
###Scottsdale
poly_az17=data.frame(
  lon=c(-111.932901,
        -111.916800,
        -111.923055,
        -111.928430,
        -111.932776,
        -111.930212,
        -111.924354),
  lat=c(33.621673,
        33.623572,
        33.627656,
        33.626870,
        33.624333,
        33.622689,
        33.622805)
)
poly_az18=data.frame(
  lon=c(-111.936605,
        -111.928739,
        -111.926597,
        -111.920671,
        -111.924664,
        -111.916319,
        -111.917610,
        -111.926756,
        -111.934352,
        -111.931373),
  lat=c(33.502928,
        33.494362,
        33.490817,
        33.491012,
        33.496564,
        33.498939,
        33.503931,
        33.506678,
        33.505331,
        33.494992)
)
poly_az19=data.frame(
  lon=c(-111.918687,
        -111.916807,
        -111.916881,
        -111.924638,
        -111.925624,
        -111.934794,
        -111.934180,
        -111.930479,
        -111.922964),
  lat=c(33.498417,
        33.498772,
        33.502727,
        33.503503,
        33.506450,
        33.506481,
        33.502417,
        33.499594,
        33.498167)
)
ggmap(get_map(location = 'scottsdale, phoenix, AZ', zoom = 11)) +
  geom_point(data=az.res, aes(x=longitude, y=latitude), color="red")+
  geom_polygon(aes(x=lon,y=lat),data=poly_az17,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az18,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az19,color="grey30",alpha=0.3)

################# Scottsdale Ends #################################
### Tempe
poly_az20=data.frame(
  lon=c(-111.902,-111.957,-111.952,-111.916),
  lat=c(33.434,33.426,33.421,33.419)
  
)
poly_az21=data.frame(
  lon=c(-111.939,-111.944,-111.940,-111.936),
  lat=c(33.397,33.393,33.390,33.393)
  
)
poly_az22=data.frame(
  lon=c(-111.926,-111.930,-111.926,-111.905),
  lat=c(33.418,33.407,33.404,33.407)
  
)
poly_az23=data.frame(
  lon=c(-111.909,-111.918,-111.909,-111.905),
  lat=c(33.397,33.393,33.390,33.393)
  
)
poly_az24=data.frame(
  lon=c(-111.911,-111.915,-111.911,-111.907),
  lat=c(33.367,33.364,33.360,33.364)
  
)
poly_az25=data.frame(
  lon=c(-111.939,-111.966,-111.983,-111.920,-111.901),
  lat=c(33.382,33.387,33.378,33.370,33.378)
  
)
poly_az26=data.frame(
  lon=c(-111.969,-111.987,-111.968,-111.900),
  lat=c(33.353,33.349,33.345,33.349)
  
)
poly_az27=data.frame(
  lon=c(-111.928,-111.945,-111.928,-111.921),
  lat=c(33.325,33.320,33.317,33.320)
  
)
ggmap(get_map(location = 'tempe, phoenix, AZ', zoom = 11)) +
  geom_point(data=az.res, aes(x=longitude, y=latitude), color="red")+
  geom_polygon(aes(x=lon,y=lat),data=poly_az20,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az21,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az22,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az23,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az24,color="grey30",alpha=0.3)+  
  geom_polygon(aes(x=lon,y=lat),data=poly_az25,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az26,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_az27,color="grey30",alpha=0.3)

################# AZ Ends #################################
### AZ 27???

################# IL #################################
poly_il1=data.frame(
  lon=c(-88.245285,-88.247037,-88.242726,-88.218689,-88.218689),
  lat=c(40.111475,40.084277,40.110556,40.100244,40.111371)
)
poly_il2=data.frame(
  lon=c(-88.263925,-88.263170,-88.230203),
  lat=c(40.149441,40.12300,40.141443)
)
poly_il3=data.frame(
  lon=c(-88.28,-88.292,-88.279,-88.260),
  lat=c(40.132,40.113,40.091,40.118)
)
poly_il4=data.frame(
  lon=c(-88.200,-88.213,-88.189),
  lat=c(40.134,40.112,40.091)
)
ggmap(get_map(location = 'champaign IL', zoom = 11)) +
  geom_point(data=il.res, aes(x=longitude, y=latitude), color="red")+
  geom_polygon(aes(x=lon,y=lat),data=poly_il1,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_il2,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_il3,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_il4,color="grey30",alpha=0.3)
#################### IL Ends ##############################################

### IL4???
#################### LV ##########################################
nv.res$city %>% table
poly_nv1=data.frame(
  lon=c(-115.1711298,-115.1977659,-115.1708014,-115.134871),
  lat=c(36.128561,36.1272504,36.0990311,36.122106)
  
)
poly_nv2=data.frame(
  lon=c(-115.131,-115.182,-115.095),
  lat=c(36.188,36.155,36.155)
  
)
poly_nv3=data.frame(
  lon=c(-115.175,-115.180,-115.171,-115.163),
  lat=c(36.079,36.064,36.038,36.064)
  
)
poly_nv4=data.frame(
  lon=c(-115.245,-115.342,-115.243,-115.187),
  lat=c(36.202,36.160,36.140,36.160)
)
ggmap(get_map(location = 'las vegas NV', zoom = 11)) +
  geom_point(data=nv.res, aes(x=longitude, y=latitude), color="red")+
  geom_polygon(aes(x=lon,y=lat),data=poly_nv1,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_nv2,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_nv3,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_nv4,color="grey30",alpha=0.3)

#################### NV ENDS #############################

###NV4???
################# Chen Yixin's Codes #############################
################# QC #############################################
qc.res$city %>% table %>% sort
poly_qc1=data.frame(
  lon=c(-73.740128,
        -73.717893,
        -73.725735,
        -73.750913,
        -73.764751),
  lat=c(45.582003,
        45.557007,
        45.552472,
        45.555646,
        45.568132)
)
poly_qc2=data.frame(
  lon=c(-73.811836,
        -73.828765,
        -73.843398,
        -73.825111
  ),
  lat=c(45.464481,
        45.456746,
        45.468903,
        45.478566
  )
)
poly_qc3=data.frame(
  lon=c(-73.756078,
        -73.751159,
        -73.728698,
        -73.731815,
        -73.745479
  ),
  lat=c(45.449332,
        45.438785,
        45.440709,
        45.450854,
        45.453432
  )
)
poly_qc4=data.frame(
  lon=c(-73.70629,
        -73.691079,
        -73.70282,
        -73.717251,
        -73.719944,
        -73.711425
  ),
  lat=c(45.50216,
        45.494766,
        45.491084,
        45.489437,
        45.498407,
        45.505167
  )
)
poly_qc5=data.frame(
  lon=c(-73.673794,
        -73.66468,
        -73.659024,
        -73.668272
  ),
  lat=c(45.474578,
        45.471126,
        45.479033,
        45.481902
  )
)
poly_qc6=data.frame(
  lon=c(-73.633215,
        -73.626393,
        -73.609825,
        -73.602606,
        -73.604667,
        -73.613115,
        -73.626674,
        -73.620175
  ),
  lat=c(45.433596,
        45.431754,
        45.447687,
        45.446962,
        45.453442,
        45.457437,
        45.449653,
        45.44622
  )
)
poly_qc7=data.frame(
  lon=c(-73.645569,
        -73.666783,
        -73.658809,
        -73.641761,
        -73.643484
  ),
  lat=c(45.525298,
        45.53182,
        45.54861,
        45.542051,
        45.529385
  )
)
poly_qc8=data.frame(
  lon=c(-73.594788,
        -73.586686,
        -73.566883,
        -73.553112,
        -73.549646,
        -73.565374,
        -73.579386
  ),
  lat=c(45.486797,
        45.482994,
        45.496781,
        45.498294,
        45.511983,
        45.514381,
        45.503462
  )
)
poly_qc9=data.frame(
  lon=c(-73.603346,
        -73.583378,
        -73.573965,
        -73.592171
  ),
  lat=c(45.566551,
        45.558525,
        45.57073,
        45.575379
  )
)
poly_qc10=data.frame(
  lon=c(-73.56411,
        -73.550976,
        -73.571452,
        -73.586305
  ),
  lat=c(45.586306,
        45.6027,
        45.609576,
        45.595339
  )
)
poly_qc11=data.frame(
  lon=c(-73.546833,
        -73.525291,
        -73.533141,
        -73.555019
  ),
  lat=c(45.601476,
        45.598575,
        45.582992,
        45.588245
  )
)
ggmap(get_map(location = 'montreal QC', zoom = 10)) +
  geom_point(data=qc.res, aes(x=longitude, y=latitude), color="red")+
  geom_polygon(aes(x=lon,y=lat),data=poly_qc1,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_qc2,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_qc3,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_qc4,color="grey30",alpha=0.3)+  
  geom_polygon(aes(x=lon,y=lat),data=poly_qc5,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_qc6,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_qc7,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_qc8,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_qc9,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_qc10,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_qc11,color="grey30",alpha=0.3)

##################### QC ENDS ############################
### QC11???
####PA
pa.res$city %>% table %>% sort
poly_pa1=data.frame(
  lon=c(-80.062235,
        -80.052831,
        -80.045606,
        -80.049146,
        -80.058612
  ),
  lat=c(40.427348,
        40.434267,
        40.430313,
        40.425833,
        40.424686
  )
)
poly_pa2=data.frame(
  lon=c(-80.008285,
        -80.002033,
        -80.006518,
        -80.010324,
        -80.009761
  ),
  lat=c(40.436582,
        40.43358,
        40.427536,
        40.428703,
        40.433802
  )
)
poly_pa3=data.frame(
  lon=c(-80.015777,
        -79.991276,
        -79.988226,
        -79.995079
  ),
  lat=c(40.442136,
        40.451154,
        40.442285,
        40.433188
  )
)
poly_pa4=data.frame(
  lon=c(-79.991414,
        -79.971407,
        -79.964622,
        -79.959826,
        -79.969813,
        -79.992602
  ),
  lat=c(40.427232,
        40.427231,
        40.423772,
        40.426904,
        40.432329,
        40.432681
  )
)
poly_pa5=data.frame(
  lon=c(-79.950493,
        -79.950515,
        -79.947398,
        -79.946726
  ),
  lat=c(40.444134,
        40.447189,
        40.447376,
        40.444237
  )
)
poly_pa6=data.frame(
  lon=c(-79.938241,
        -79.936134,
        -79.923322,
        -79.916084,
        -79.909592,
        -79.921045
  ),
  lat=c(40.459524,
        40.453758,
        40.457093,
        40.453239,
        40.459109,
        40.463842
  )
)
poly_pa7=data.frame(
  lon=c(-79.925838,
        -79.919262,
        -79.90647,
        -79.895817,
        -79.895887,
        -79.911423
  ),
  lat=c(40.402718,
        40.398907,
        40.407263,
        40.408023,
        40.414371,
        40.415701
  )
)
poly_pa8=data.frame(
  lon=c(-79.910403,
        -79.867208,
        -79.8717,
        -79.883908,
        -79.904895
  ),
  lat=c(40.488774,
        40.484364,
        40.49423,
        40.491914,
        40.4962
  )
)
ggmap(get_map(location = 'pittsburgh PA', zoom = 11)) +
  geom_point(data=pa.res, aes(x=longitude, y=latitude), color="red")+
  geom_polygon(aes(x=lon,y=lat),data=poly_pa1,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_pa2,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_pa3,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_pa4,color="grey30",alpha=0.3)+  
  geom_polygon(aes(x=lon,y=lat),data=poly_pa5,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_pa6,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_pa7,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_pa8,color="grey30",alpha=0.3)

####################### PA ENDS ############################################
PA8???
######################### OH ###############################################
oh.res$city %>% table %>% sort
poly_oh1=data.frame(
  lon=c(-81.70892,
        -81.695635,
        -81.675298,
        -81.685288
  ),
  lat=c(41.501941,
        41.494371,
        41.498787,
        41.508914
  )
)
poly_oh2=data.frame(
  lon=c(-81.684984,
        -81.697704,
        -81.693002,
        -81.679927
  ),
  lat=c(41.454199,
        41.457252,
        41.468672,
        41.466371
  )
)
poly_oh3=data.frame(
  lon=c(-81.853373,
        -81.844187,
        -81.844327,
        -81.839195,
        -81.84066,
        -81.859282
  ),
  lat=c(41.456594,
        41.457938,
        41.462597,
        41.464135,
        41.467184,
        41.461553
  )
)
poly_oh4=data.frame(
  lon=c(-81.939575,
        -81.931814,
        -81.900253,
        -81.885504,
        -81.887249,
        -81.878333,
        -81.882289,
        -81.91052
  ),
  lat=c(41.417074,
        41.407909,
        41.411896,
        41.421038,
        41.426629,
        41.433986,
        41.43594,
        41.426651
  )
)
poly_oh5=data.frame(
  lon=c(-81.752377,
        -81.752625,
        -81.73095,
        -81.730491
  ),
  lat=c(41.387073,
        41.376012,
        41.375326,
        41.38673
  )
)
poly_oh6=data.frame(
  lon=c(-81.701219,
        -81.701618,
        -81.68565,
        -81.686547
  ),
  lat=c(41.408566,
        41.401642,
        41.401529,
        41.408304
  )
)
poly_oh7=data.frame(
  lon=c(-81.664639,
        -81.667304,
        -81.659862,
        -81.657525
  ),
  lat=c(41.402465,
        41.399174,
        41.396867,
        41.401373
  )
)
poly_oh8=data.frame(
  lon=c(-81.646788,
        -81.655114,
        -81.63918,
        -81.635118
  ),
  lat=c(41.400726,
        41.394122,
        41.390666,
        41.398115
  )
)
poly_oh9=data.frame(
  lon=c(-81.512954,
        -81.513492,
        -81.501175,
        -81.502521,
        -81.477891,
        -81.477285,
        -81.454924,
        -81.455486,
        -81.489416
  ),
  lat=c(41.468355,
        41.462504,
        41.46079,
        41.44374,
        41.448761,
        41.457853,
        41.45964,
        41.467489,
        41.470097
  )
)
poly_oh10=data.frame(
  lon=c(-81.510824,
        -81.506908,
        -81.495014,
        -81.489618,
        -81.4951
  ),
  lat=c(41.506171,
        41.498437,
        41.495459,
        41.498262,
        41.506345
  )
)
poly_oh11=data.frame(
  lon=c(-81.504764,
        -81.505686,
        -81.483486,
        -81.483816
  ),
  lat=c(41.548634,
        41.534274,
        41.535839,
        41.55045
  )
)
ggmap(get_map(location = 'cleveland, OH', zoom = 1)) +
  geom_point(data=oh.res, aes(x=longitude, y=latitude), color="red")+
  geom_polygon(aes(x=lon,y=lat),data=poly_oh1,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_oh2,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_oh3,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_oh4,color="grey30",alpha=0.3)+  
  geom_polygon(aes(x=lon,y=lat),data=poly_oh5,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_oh6,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_oh7,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_oh8,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_oh9,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_oh10,color="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_oh11,color="grey30",alpha=0.3)
################# OH ENDS ###############################################

###OH11???
################# WI ####################################################
poly_wi1=data.frame(
  lon=c(-89.525,-89.495,-89.493,-89.503,-89.51),
  lat=c(43.062,43.063,43.054,43.045,43.056)
)
poly_wi2=data.frame(
  lon=c(-89.398,-89.389,-89.384,-89.379,-89.384,-89.389,-89.398),
  lat=c(43.076,43.076,43.078,43.0745,43.072,43.074,43.074)
)
poly_wi3=data.frame(
  lon=c(-89.33,-89.298,-89.297,-89.305,-89.325),
  lat=c(43.1148,43.139,43.133,43.12,43.114)
)

ggmap(get_map(location = 'madison WI', zoom = 12)) +
  geom_point(data=wi.res, aes(x=longitude, y=latitude), color="red",size=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_wi1,col="grey30",alpha=0.4)+
  geom_polygon(aes(x=lon,y=lat),data=poly_wi2,col="grey30",alpha=0.4)+
  geom_polygon(aes(x=lon,y=lat),data=poly_wi3,col="grey30",alpha=0.4)
################### WI ENDS #############################################

###WI 3???
################### AB ##############################################
restaurant$state %>% table
ab.res$city %>% table %>% sort
ggmap(get_map(location = 'calgary ab', zoom = 11)) +
  geom_point(data=ab.res, aes(x=longitude, y=latitude), color="red")
poly_ab1=data.frame(
  lon=c(-114.0937,-114.0483,-114.0587,-114.0683),
  lat=c(51.0462,51.0438,51.0509,51.0545)
)
poly_ab2=data.frame(
  lon=c(-114.0709,-114.0705,-114.0554,-114.0613),
  lat=c(50.959,50.950,50.9474,50.9542)
)
poly_ab3=data.frame(
  lon=c(-114.0024,-113.9869,-113.969,-113.9726),
  lat=c(51.0863,51.0509,51.0521,51.0810)
)
poly_ab4=data.frame(
  lon=c(-114.2045,-114.2105,-114.1999,-114.1949),
  lat=c(51.13141,51.1254,51.1220,51.1277)
)
poly_ab5=data.frame(
  lon=c(-114.0776,-114.0717,-114.0717,-114.0776),
  lat=c(51.0023,51.0023,50.9945,50.9945)
)
ggmap(get_map(location = 'calgary ab', zoom = 11)) +
  geom_point(data=ab.res, aes(x=longitude, y=latitude), color="red")+
  geom_polygon(aes(x=lon,y=lat),data=poly_ab1,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_ab2,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_ab3,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_ab4,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_ab5,col="grey30",alpha=0.3)

########################## AB ENDS ########################################
###AB 5???
########################## NC ##########################################

nc.res$city %>% table %>% sort

poly_nc1=data.frame(
  lon=c(-80.8414,-80.8511,-80.8453,-80.8324),
  lat=c(35.2319,35.2253,35.2189,35.2265)
)
poly_nc2=data.frame(
  lon=c(-80/8323,-80.8378,-80.8218,-80.8247),
  lat=c(35.1557,35.1467,35.1429,35.1520)
)
poly_nc3=data.frame(
  lon=c(-80.8861,-80.8853,-80.8795,-80.8791,-80.8911,-80.8857,-80.8721,-80.8744),
  lat=c(35.1834,35.1763,35.1751,35.1666,35.1630,35.1585,35.1631,35.1795)
)
poly_nc4=data.frame(
  lon=c(-80.8559,-80.8651,-80.8397,-80.8390),
  lat=c(35.3567,35.3451,35.3429,35.3550)
)
poly_nc5=data.frame(
  lon=c(-80.7543,-80.7608,-80.7534,-80.7418),
  lat=c(35.3173,35.2932,35.2907,35.3059)
)
poly_nc6=data.frame(
  lon=c(-80.7307,-80.7372,-80.7142,-80.7054),
  lat=c(35.3798,35.3705,35.3601,35.3692)
)
ggmap(get_map(location = 'charlotte nc', zoom = 11)) +
  geom_point(data=nc.res, aes(x=longitude, y=latitude), color="red")+
  geom_polygon(aes(x=lon,y=lat),data=poly_nc1,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_nc2,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_nc3,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_nc4,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_nc5,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_nc6,col="grey30",alpha=0.3)

########################## NC ENDS ####################################

##NC6???
########################## ON ######################################## 
on.res$city %>% table %>% sort

poly_on1=data.frame(
  lon=c(-79.3994,-79.3916,-79.4322,-79.4251,-79.3485,-79.3702,-79.3807),
  lat=c(43.6748,43.6591,43.6527,43.6311,43.6487,43.6582,43.6749)
)
poly_on2=data.frame(
  lon=c(-79.4028,-79.3916,-79.3858,-79.3981),
  lat=c(43.7167,43.6752,43.6763,43.718)
)
poly_on3=data.frame(
  lon=c(-79.3494,-79.3461,-79.3398,-79.3407),
  lat=c(43.7361,43.7258,43.7232,43.7367)
)
poly_on4=data.frame(
  lon=c(-79.4584,-79.4636,-79.4566,-79.444,-79.4471),
  lat=c(43.7298,43.7180,43.7159,43.7278,43.7322)
)
poly_on5=data.frame(
  lon=c(-79.5601,-79.5596,-79.5303,-79.5339),
  lat=c(43.8294,43.8236,43.8256,43.8322)
)
poly_on6=data.frame(
  lon=c(-79.5815,-79.5803,-79.5157,-79.5218),
  lat=c(43.7886,43.7763,43.7855,43.7998)
)
poly_on7=data.frame(
  lon=c(-79.6437,-79.6522,-79.6369,-79.6286),
  lat=c(43.5979,43.5893,43.5790,43.5897)
)
ggmap(get_map(location = 'toronto canada', zoom = 10)) +
  geom_point(data=on.res, aes(x=longitude, y=latitude), color="red")+
  geom_polygon(aes(x=lon,y=lat),data=poly_on1,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_on2,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_on3,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_on4,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_on5,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_on6,col="grey30",alpha=0.3)+
  geom_polygon(aes(x=lon,y=lat),data=poly_on7,col="grey30",alpha=0.3)

############################ ON ENDS #####################################
###ON7???

restaurant$state %>% table
business_count=c(5,27,4,6,4,11,7,8,11,3)
names(business_count)=c("AB","AZ","IL","NC","NV","OH","ON","PA","QC","WI")
business_count
### WI ###
wi.coor=data.frame(
  lon=wi.res$longitude,
  lat=wi.res$latitude
)
wi.res$circle=rep(0,dim(wi.res)[1])
for(i in 1:dim(wi.res)[1]){
  a=in_or_out(poly_wi1,as.numeric(wi.coor[i,1:2]))
  b=in_or_out(poly_wi2,as.numeric(wi.coor[i,1:2]))
  c=in_or_out(poly_wi3,as.numeric(wi.coor[i,1:2]))
  d=a|b|c
  wi.res$circle[i]=d
}
wi.res$circle %>% table
### WI END ###

### IL ###

il.coor=data.frame(
  lon=il.res$longitude,
  lat=il.res$latitude
)
il.res$circle=rep(0,dim(il.res)[1])
for(i in 1:dim(il.res)[1]){
  a=in_or_out(poly_il1,as.numeric(il.coor[i,1:2]))
  b=in_or_out(poly_il2,as.numeric(il.coor[i,1:2]))
  c=in_or_out(poly_il3,as.numeric(il.coor[i,1:2]))
  d=in_or_out(poly_il4,as.numeric(il.coor[i,1:2]))
  logic=a|b|c|d
  il.res$circle[i]=logic
}
il.res$circle %>% table

##############  IL ENDS ################################
### NV ##############################

nv.coor=data.frame(
  lon=nv.res$longitude,
  lat=nv.res$latitude
)
nv.res$circle=rep(0,dim(nv.res)[1])
for(i in 1:dim(nv.res)[1]){
  a=in_or_out(poly_nv1,as.numeric(nv.coor[i,1:2]))
  b=in_or_out(poly_nv2,as.numeric(nv.coor[i,1:2]))
  c=in_or_out(poly_nv3,as.numeric(nv.coor[i,1:2]))
  d=in_or_out(poly_nv4,as.numeric(nv.coor[i,1:2]))
  logic=a|b|c|d
  nv.res$circle[i]=logic
}
nv.res$circle %>% table

### NV ENDS ###########################
### AB ################################
ab.coor=data.frame(
  lon=ab.res$longitude,
  lat=ab.res$latitude
)
ab.res$circle=rep(0,dim(ab.res)[1])
for(i in 1:dim(ab.res)[1]){
  a=in_or_out(poly_ab1,as.numeric(ab.coor[i,1:2]))
  b=in_or_out(poly_ab2,as.numeric(ab.coor[i,1:2]))
  c=in_or_out(poly_ab3,as.numeric(ab.coor[i,1:2]))
  d=in_or_out(poly_ab4,as.numeric(ab.coor[i,1:2]))
  e=in_or_out(poly_ab5,as.numeric(ab.coor[i,1:2]))
  logic=a|b|c|d|e
  ab.res$circle[i]=logic
}
ab.res$circle %>% table
### AB ENDS ##############################
### NC ###################################
nc.coor=data.frame(
  lon=nc.res$longitude,
  lat=nc.res$latitude
)
nc.res$circle=rep(0,dim(nc.res)[1])
for(i in 1:dim(nc.res)[1]){
  a=in_or_out(poly_nc1,as.numeric(nc.coor[i,1:2]))
  b=in_or_out(poly_nc2,as.numeric(nc.coor[i,1:2]))
  c=in_or_out(poly_nc3,as.numeric(nc.coor[i,1:2]))
  d=in_or_out(poly_nc4,as.numeric(nc.coor[i,1:2]))
  e=in_or_out(poly_nc5,as.numeric(nc.coor[i,1:2]))
  f=in_or_out(poly_nc6,as.numeric(nc.coor[i,1:2]))
  logic=a|b|c|d|e|f
  nc.res$circle[i]=logic
}
nc.res$circle %>% table
### NC ENDS ##############################
### ON ###################################
on.coor=data.frame(
  lon=on.res$longitude,
  lat=on.res$latitude
)
on.res$circle=rep(0,dim(on.res)[1])
for(i in 1:dim(on.res)[1]){
  a=in_or_out(poly_on1,as.numeric(on.coor[i,1:2]))
  b=in_or_out(poly_on2,as.numeric(on.coor[i,1:2]))
  c=in_or_out(poly_on3,as.numeric(on.coor[i,1:2]))
  d=in_or_out(poly_on4,as.numeric(on.coor[i,1:2]))
  e=in_or_out(poly_on5,as.numeric(on.coor[i,1:2]))
  f=in_or_out(poly_on6,as.numeric(on.coor[i,1:2]))
  g=in_or_out(poly_on7,as.numeric(on.coor[i,1:2]))
  logic=a|b|c|d|e|f|g
  on.res$circle[i]=logic
}
on.res$circle %>% table
##### ON ENDS ############################
### PA ###################################
pa.coor=data.frame(
  lpa=pa.res$longitude,
  lat=pa.res$latitude
)
pa.res$circle=rep(0,dim(pa.res)[1])
for(i in 1:dim(pa.res)[1]){
  a=in_or_out(poly_pa1,as.numeric(pa.coor[i,1:2]))
  b=in_or_out(poly_pa2,as.numeric(pa.coor[i,1:2]))
  c=in_or_out(poly_pa3,as.numeric(pa.coor[i,1:2]))
  d=in_or_out(poly_pa4,as.numeric(pa.coor[i,1:2]))
  e=in_or_out(poly_pa5,as.numeric(pa.coor[i,1:2]))
  f=in_or_out(poly_pa6,as.numeric(pa.coor[i,1:2]))
  g=in_or_out(poly_pa7,as.numeric(pa.coor[i,1:2]))
  h=in_or_out(poly_pa8,as.numeric(pa.coor[i,1:2]))
  logic=a|b|c|d|e|f|g|h
  pa.res$circle[i]=logic
}
pa.res$circle %>% table
#### PA ENDS ##############################
### QC 11####################################
qc.coor=data.frame(
  lqc=qc.res$longitude,
  lat=qc.res$latitude
)
qc.res$circle=rep(0,dim(qc.res)[1])
for(i in 1:dim(qc.res)[1]){
  a=in_or_out(poly_qc1,as.numeric(qc.coor[i,1:2]))
  b=in_or_out(poly_qc2,as.numeric(qc.coor[i,1:2]))
  c=in_or_out(poly_qc3,as.numeric(qc.coor[i,1:2]))
  d=in_or_out(poly_qc4,as.numeric(qc.coor[i,1:2]))
  e=in_or_out(poly_qc5,as.numeric(qc.coor[i,1:2]))
  f=in_or_out(poly_qc6,as.numeric(qc.coor[i,1:2]))
  g=in_or_out(poly_qc7,as.numeric(qc.coor[i,1:2]))
  h=in_or_out(poly_qc8,as.numeric(qc.coor[i,1:2]))
  j=in_or_out(poly_qc9,as.numeric(qc.coor[i,1:2]))
  k=in_or_out(poly_qc10,as.numeric(qc.coor[i,1:2]))
  l=in_or_out(poly_qc11,as.numeric(qc.coor[i,1:2]))
  logic=a|b|c|d|e|f|g|h|j|k|l
  qc.res$circle[i]=logic
}
qc.res$circle %>% table
#### QC ENDS #######################################
#### OH 11 ############################################
oh.coor=data.frame(
  loh=oh.res$longitude,
  lat=oh.res$latitude
)
oh.res$circle=rep(0,dim(oh.res)[1])
for(i in 1:dim(oh.res)[1]){
  a=in_or_out(poly_oh1,as.numeric(oh.coor[i,1:2]))
  b=in_or_out(poly_oh2,as.numeric(oh.coor[i,1:2]))
  c=in_or_out(poly_oh3,as.numeric(oh.coor[i,1:2]))
  d=in_or_out(poly_oh4,as.numeric(oh.coor[i,1:2]))
  e=in_or_out(poly_oh5,as.numeric(oh.coor[i,1:2]))
  f=in_or_out(poly_oh6,as.numeric(oh.coor[i,1:2]))
  g=in_or_out(poly_oh7,as.numeric(oh.coor[i,1:2]))
  h=in_or_out(poly_oh8,as.numeric(oh.coor[i,1:2]))
  j=in_or_out(poly_oh9,as.numeric(oh.coor[i,1:2]))
  k=in_or_out(poly_oh10,as.numeric(oh.coor[i,1:2]))
  l=in_or_out(poly_oh11,as.numeric(oh.coor[i,1:2]))
  logic=a|b|c|d|e|f|g|h|j|k|l
  oh.res$circle[i]=logic
}
oh.res$circle %>% table
### OH ENDS ####################################
### AZ 27 ######################################
az.coor=data.frame(
  laz=az.res$longitude,
  lat=az.res$latitude
)
az.res$circle=rep(0,dim(az.res)[1])
for(i in 1:dim(az.res)[1]){
  a=in_or_out(poly_az1,as.numeric(az.coor[i,1:2]))
  b=in_or_out(poly_az2,as.numeric(az.coor[i,1:2]))
  c=in_or_out(poly_az3,as.numeric(az.coor[i,1:2]))
  d=in_or_out(poly_az4,as.numeric(az.coor[i,1:2]))
  e=in_or_out(poly_az5,as.numeric(az.coor[i,1:2]))
  f=in_or_out(poly_az6,as.numeric(az.coor[i,1:2]))
  g=in_or_out(poly_az7,as.numeric(az.coor[i,1:2]))
  h=in_or_out(poly_az8,as.numeric(az.coor[i,1:2]))
  j=in_or_out(poly_az9,as.numeric(az.coor[i,1:2]))
  k=in_or_out(poly_az10,as.numeric(az.coor[i,1:2]))
  l=in_or_out(poly_az11,as.numeric(az.coor[i,1:2]))
  m=in_or_out(poly_az12,as.numeric(az.coor[i,1:2]))
  n=in_or_out(poly_az13,as.numeric(az.coor[i,1:2]))
  o=in_or_out(poly_az14,as.numeric(az.coor[i,1:2]))
  p=in_or_out(poly_az15,as.numeric(az.coor[i,1:2]))
  q=in_or_out(poly_az16,as.numeric(az.coor[i,1:2]))
  r=in_or_out(poly_az17,as.numeric(az.coor[i,1:2]))
  s=in_or_out(poly_az18,as.numeric(az.coor[i,1:2]))
  t=in_or_out(poly_az19,as.numeric(az.coor[i,1:2]))
  u=in_or_out(poly_az20,as.numeric(az.coor[i,1:2]))
  v=in_or_out(poly_az21,as.numeric(az.coor[i,1:2]))
  w=in_or_out(poly_az22,as.numeric(az.coor[i,1:2]))
  x=in_or_out(poly_az23,as.numeric(az.coor[i,1:2]))
  y=in_or_out(poly_az24,as.numeric(az.coor[i,1:2]))
  z=in_or_out(poly_az25,as.numeric(az.coor[i,1:2]))
  aa=in_or_out(poly_az26,as.numeric(az.coor[i,1:2]))
  bb=in_or_out(poly_az27,as.numeric(az.coor[i,1:2]))
  logic=a|b|c|d|e|f|g|h|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|aa|bb
  az.res$circle[i]=logic
}
az.res$circle %>% table
### AZ ENDS ###############################################

### ALL FINISHED, WRITE .CSV ########################
restaurant_circle=rbind()
restaurant$state %>% table
az.res$circle %>% table
write.csv(az.res,"az_res.csv")
write.csv(ab.res,"ab_res.csv")
write.csv(il.res,"il_res.csv")
write.csv(nc.res,"nc_res.csv")
write.csv(nv.res,"nv_res.csv")
write.csv(oh.res,"oh_res.csv")
write.csv(on.res,"on_res.csv")
write.csv(pa.res,"pa_res.csv")
write.csv(qc.res,"qc_res.csv")
write.csv(wi.res,"wi_res.csv")


