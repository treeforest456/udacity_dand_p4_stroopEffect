

data <- read.csv('stroopdata.csv')
library(dplyr)

t.test(x=data$Congruent, \
	y=data$Incongruent, \
	alternative='two.sided', \
	mu=0, \
	paired=TRUE, \
	conf.level=0.95)