direc1<-"ingrese el directorio donde guardara los archivos ej:' /home/carolinaog/CM20151_HW4_CarolinaOrtiz/Punto1/' "


library(dplyr)
library(tidyr)
library(ggplot2)
library(reshape2)

#Script para generar una tabla en representación limpia del cambio en el tiempo en 5 ciudades de Colombia
#Al ejecutar este código, asegúrese de abrir el link "http://data.giss.nasa.gov/gistemp/station_data/ " y buscar para las ciudades de Bogotá, Cali, Barranquilla, Bucaramanga e Ipiales sus estaciones , y en cada una, abrir "Download monthly data as text" Ya que el archivo es temporal y necesita refrescarse en el navegador.
#NOTA PUNTO 1.b : se generarán los archivos de texto bogota2.txt, cali2.txt, Ipiales2.txt, Bquilla2.txt, Bmanga2.txt, que se guardarán en la carpeta Home del computador. Asegurarse de moverlos a la carpeta en que se está trabajando este punto: "Punto2Final"

#***BOGOTA***
#Descarga la información de temperaturas en un archivo y crea una DataFrame en el ambiente de programación
URLbog <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802220000_14_0/station.txt"
destfilebog <-paste(direc1,"bogota.txt", collapse="/" )
download.file(URLbog, destfilebog, "wget", quiet = FALSE, mode = "r", cacheOK = TRUE, extra = getOption("download.file.extra"))
a=read.table(destfilebog,skip=0,header=T)
#Not avaliable values
a[a == 999.9] <- NA
#Elimina las ultimas 5 columnas innecesarias
a=a[, !(colnames(a) %in% c("D.J.F","M.A.M","J.J.A","S.O.N","metANN"))]

#Ordena de Enero a Diciembre los datos de temperatura
a<- a %>% gather(mes,temp, JAN:DEC)
#ordena por año la matriz
a<-a[do.call(order,a),]

#Creamos para cada ciudad una secuencia con las fechas correspondientes, y la añade al DataFrame:
date <- seq(as.Date("1967-01-01"),as.Date("2015-12-31"), by="month")
date= data.frame(date[])
a<-bind_cols(a, date)
#Creamos una columna con el nombre de la ciudad, y cambiamos los nombres de las columnas
a[["city"]] <- c("Bogota")
colnames(a) <- c("Year","month","temperature","date","City")


#exporta archivo para punto 1.b con las temperaturas y la fecha
a2=a[, !(colnames(a) %in% c("Year","month","City"))]
write.table(a2, "bogota2.txt", sep="\t", row.names=FALSE, col.names=TRUE)

#***CALI*** 
URLcal <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802590000_14_0/station.txt"
destfilecal <-paste(direc1,"cali.txt", collapse="/" )
download.file(URLcal, destfilecal, "wget", quiet = FALSE, mode = "r", cacheOK = TRUE, extra = getOption("download.file.extra"))
b=read.table(destfilecal,skip=0,header=T)
b[b == 999.9] <- NA
b=b[, !(colnames(b) %in% c("D.J.F","M.A.M","J.J.A","S.O.N","metANN"))]
b<- b %>% gather(mes,temp, JAN:DEC)
b<-b[do.call(order,b),]
date <- seq(as.Date("1951-01-01"),as.Date("2014-12-31"), by="month")
date= data.frame(date[])
b<-bind_cols(b, date)
b[["city"]] <- c("Cali")
colnames(b) <- c("Year","month","temperature","date","City")

#exporta archivo para punto 1.b con las temperaturas y la fecha
b2=b[, !(colnames(a) %in% c("Year","month","City"))]
write.table(b2, "cali2.txt", sep="\t", row.names=FALSE, col.names=TRUE)

#***BUCARAMANGA**
URLbmga <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800940000_14_0/station.txt"
destfilebmga <-paste(direc1,"bucaramanga.txt", collapse="/" )
download.file(URLbmga, destfilebmga, "wget", quiet = FALSE, mode = "r", cacheOK = TRUE, extra = getOption("download.file.extra"))
c=read.table(destfilebmga,skip=0,header=T)
c[c == 999.9] <- NA
c=c[, !(colnames(c) %in% c("D.J.F","M.A.M","J.J.A","S.O.N","metANN"))]
c<- c %>% gather(mes,temp, JAN:DEC)
c<-c[do.call(order,c),]
date <- seq(as.Date("1977-01-01"),as.Date("2015-12-31"), by="month")
date= data.frame(date[])
c<-bind_cols(c, date)
c[["city"]] <- c("Bucaramanga")
colnames(c) <- c("Year","month","temperature","date","City")


#exporta archivo para punto 1.b con las temperaturas y la fecha
c2=c[, !(colnames(a) %in% c("Year","month","City"))]
write.table(c2, "Bmanga2.txt", sep="\t", row.names=FALSE, col.names=TRUE)

#**BARRANQUILLA**
URLbquilla <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800280000_14_0/station.txt"
destfilebquilla <-paste(direc1,"barranquilla.txt", collapse="/" )
download.file(URLbquilla, destfilebquilla, "wget", quiet = FALSE, mode = "r", cacheOK = TRUE, extra = getOption("download.file.extra"))
d=read.table(destfilebquilla,skip=0,header=T)
d[d == 999.9] <- NA
d=d[, !(colnames(d) %in% c("D.J.F","M.A.M","J.J.A","S.O.N","metANN"))]
d<- d %>% gather(mes,temp, JAN:DEC)
d<-d[do.call(order,d),]
date <- seq(as.Date("1966-01-01"),as.Date("2015-12-31"), by="month")
date= data.frame(date[])
d<-bind_cols(d, date)
d[["city"]] <- c("Barranquilla")
colnames(d) <- c("Year","month","temperature","date","City")


#exporta archivo para punto 1.b con las temperaturas y la fecha
d2=d[, !(colnames(a) %in% c("Year","month","City"))]
write.table(d2, "Bquilla2.txt", sep="\t", row.names=FALSE, col.names=TRUE)
            

#**IPIALES**
URLipi <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305803700000_14_0/station.txt"
destfileipi <- paste(direc1,"ipiales.txt", collapse="/" )
download.file(URLipi, destfileipi, "wget", quiet = FALSE, mode = "w", cacheOK = TRUE, extra = getOption("download.file.extra"))
e=read.table(destfileipi,skip=0,header=T)
e[e == 999.9] <- NA
e=e[, !(colnames(e) %in% c("D.J.F","M.A.M","J.J.A","S.O.N","metANN"))]
e<- e %>% gather(mes,temp, JAN:DEC)
e<-e[do.call(order,e),]
date <- seq(as.Date("1973-01-01"),as.Date("2015-12-31"), by="month")
date= data.frame(date[])
e<-bind_cols(e, date)
e[["city"]] <- c("Ipiales")
colnames(e) <- c("Year","month","temperature","date","City")


#exporta archivo para punto 1.b con las temperaturas y la fecha
e2=e[, !(colnames(a) %in% c("Year","month","City"))]
write.table(e2, "Ipiales2.txt", sep="\t", row.names=FALSE, col.names=TRUE)

#CREACIÓN DEL ARCHIVO TEMPERATURAS.CSV a partir de la unión de los DataFrames de las 5 ciudades, se guarda en /Home
f<-bind_rows(a, b, c, d, e)
fdir<-paste(direc1,"temperaturas.csv", collapse="/" )
write.csv(f, file = fdir,row.names=FALSE,)


#PARTE 2 Serie de Tiempo
#serie completa de tiempo organización de una tabla llamada newdate en la que se organiza por fecha, la temperatura de todas las ciudades
#newDate se genera por partes al añadir con el metodo left_join las temperaturas de cada ciudad
newd <- seq(as.Date("1951-01-01"),as.Date("2015-12-31"), by="month")
newdate<- data.frame(newd[])
colnames(newdate) <- c("date")
#Temp bogota
as<-select(a, date, temperature)
newdate<-left_join(newdate, as, by = "date")
colnames(newdate) <- c("date", "TempBog")
#temp Cali
bs<-select(b, date, temperature)
newdate<-left_join(newdate, bs, by = "date")
colnames(newdate) <- c("date", "TempBog","TempCal")
#Temp Bmanga
cs<-select(c, date, temperature)
newdate<-left_join(newdate, cs, by = "date")
colnames(newdate) <- c("date", "TempBog","TempCal","TempBuc")
#Temp Bquilla
ds<-select(d, date, temperature)
newdate<-left_join(newdate, ds, by = "date")
colnames(newdate) <- c("date", "TempBog","TempCal","TempBuc","TempBar")
#Temp Ipiales
es<-select(e, date, temperature)
newdate<-left_join(newdate, es, by = "date")
colnames(newdate) <- c("date", "TempBog","TempCal","TempBuc","TempBar","TempIpi")


#grafica de la serie de tiempo guardada en /Home como "plot.png"
dirpng<-paste(direc1,"plot.png", collapse="/" )
a<-ggplot(newdate, aes(date, y = Temperature, title="Time Series; Temperature behaviour on five cities in Colombia", color = variable)) +
  geom_point(aes(y = TempBog, col = "Bogota")) + 
  geom_point(aes(y = TempCal, col = "Cali")) +
  geom_point(aes(y = TempBuc, col = "Bmanga")) +
  geom_point(aes(y = TempBar, col = "Bquilla")) +
  geom_point(aes(y = TempIpi, col = "Ipiales")) 
print(a)
dev.copy(png,dirpng)

dev.off()
