# base data
rm(list = ls())
set.seed(32201303)
cvbase = read.csv("PsyCoronaBaselineExtract.csv")
cvbase <- cvbase[sample(nrow(cvbase), 40000), ]

dim(cvbase) # dimension
str(cvbase) # data types
summary(cvbase) # summary
unique(cvbase$coded_country) # unique country

# replace NA in employee status to 0
cvbase[,21:30] <- replace(cvbase[,21:30], is.na(cvbase[,21:30]), 0) 

# filter out Indonesia
corona_Indonesia <- cvbase[cvbase$coded_country == "Indonesia", c(1:49,51:54)]
# average of each column
means_Indonesia <- colMeans(corona_Indonesia, na.rm = TRUE) 
means_Indonesia <- as.data.frame(means_Indonesia)

# filter out other countries
corona_others <- cvbase[cvbase$coded_country != "Indonesia", c(1:49,51:54)]
# average of each column
means_others <- colMeans(corona_others, na.rm = TRUE)
means_others <- as.data.frame(means_others)

# combine each data frame
means <- bind_cols(means_Indonesia, means_others)

# plotting the means 
library(dplyr)
plot(means, main = "Average of participant responses", xlab = "Indonesia", ylab = "Other country", pch = 16)
abline(0,1)
text(means[,1], means[,2], row.names(means), cex=0.5, pos=4, col="red")

# changing country name to other_countries or Indonesia
other_indonesia <- cvbase
other_indonesia[,50] <- replace(other_indonesia[,50], other_indonesia[,50] != "Indonesia", "other_countries")

# Based on other_country or Indonesia, abstracting the value and attributes 
library(reshape2)
df <- melt(other_indonesia, id.vars = "coded_country")

# creating box plot for each attribute in Indonesia and other countries
library(ggplot2)
p <- ggplot(data=df, aes(x=variable, y=value)) + geom_boxplot(aes(fill=coded_country))
p <- p + facet_wrap( ~ variable, scales="free") # creating a grid in box plot
p <- p + xlab("vriable") + ylab("Distribution") + ggtitle("Indonesia vs other countries") # name of x-axis, y-axis, and title
p <- p + guides(fill=guide_legend(title="Group")) # name the title of legend
p <- p + scale_fill_manual(values=c("orange", "darkgreen"))
p

# linear model and summary for the predictions of Indonesia 
fit_01_Indonesia <- lm(c19ProSo01 ~ . - c19ProSo02 - c19ProSo03 - c19ProSo04, data = corona_Indonesia)
summary(fit_01_Indonesia)
fit_02_Indonesia <- lm(c19ProSo02 ~ . - c19ProSo01 - c19ProSo03 - c19ProSo04, data = corona_Indonesia)
summary(fit_02_Indonesia)
fit_03_Indonesia <- lm(c19ProSo03 ~ . - c19ProSo01 - c19ProSo02 - c19ProSo04, data = corona_Indonesia)
summary(fit_03_Indonesia)
fit_04_Indonesia <- lm(c19ProSo04 ~ . - c19ProSo01 - c19ProSo02 - c19ProSo03, data = corona_Indonesia)
summary(fit_04_Indonesia)

# linear model and summary for the predictions of other countries
fit_01_other <- lm(c19ProSo01 ~ . - c19ProSo02 - c19ProSo03 - c19ProSo04, data = corona_others)
summary(fit_01_other)
fit_02_other <- lm(c19ProSo02 ~ . - c19ProSo01 - c19ProSo03 - c19ProSo04, data = corona_others)
summary(fit_02_other)
fit_03_other <- lm(c19ProSo03 ~ . - c19ProSo01 - c19ProSo02 - c19ProSo04, data = corona_others)
summary(fit_03_other)
fit_04_other <- lm(c19ProSo04 ~ . - c19ProSo01 - c19ProSo02 - c19ProSo03, data = corona_others)
summary(fit_04_other)

# for Life expectancy 
le <- read.csv("data.csv",header = TRUE, skip = 1)
le <- le[le$Year==2019, c(1,3)]

# for GDP per capita 
gdp <- read.csv("gdp.csv", header =TRUE, skip = 4)
gdp <- gdp[,c(1,66)]

# for unemployment rate
un <- read.csv("unemp.csv", header = TRUE, skip = 3)
un <- un[,c(1,66)]

# fro politic stability
po <- read.csv("politic_stability.csv", header = TRUE)
po$Rank <- as.integer(po$Rank)

# abstracting country names from base data
data <- unique(cvbase$coded_country)
data <- as.data.frame(data)

# combine the above data frame into a data frame
data <- inner_join(data, gdp, by = c("data"="Country.Name"))
data <- inner_join(data, le, by = c("data"="Country"))
data <- inner_join(data, un, by = c("data"="Country.Name"))
data <- inner_join(data, po, by = c("data"="Country.Territory"))
names(data) <- c("country", "gdp","life_expectancy", "unemployee_rate", "politic_stability")
# remove NA
data <- na.omit(data)

# Hierarchical Clustering with scaling 
library(ggplot2)
data[,c(2:5)] <- scale(data[,c(2:5)])
datafit <- hclust(dist(data[,2:5]), "ave")
var_names <- data$country
plot(datafit, hang = -1, xlab = "Country", main="Hierarchical Clustering", labels = var_names)

# abstracting similar country 
corona_similar <- cvbase[cvbase$coded_country %in% c("Cambodia", "Philippines", "Guatemala", "Thailand", "Bahrain", "Saudi Arabia")
                        , c(1:49,51:54)]
# linear model and summary for the predictions of similar countries
fit_01_similar <- lm(c19ProSo01 ~ . - c19ProSo02 - c19ProSo03 - c19ProSo04, data = corona_similar)
summary(fit_01_similar)
fit_02_similar <- lm(c19ProSo02 ~ . - c19ProSo01 - c19ProSo03 - c19ProSo04, data = corona_similar)
summary(fit_02_similar)
fit_03_similar <- lm(c19ProSo03 ~ . - c19ProSo01 - c19ProSo02 - c19ProSo04, data = corona_similar)
summary(fit_03_similar)
fit_04_similar <- lm(c19ProSo04 ~ . - c19ProSo01 - c19ProSo02 - c19ProSo03, data = corona_similar)
summary(fit_04_similar)









