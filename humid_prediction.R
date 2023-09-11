#Creating my data set
rm(list = ls())
WAUS <- read.csv("HumidPredict2023D.csv")
L <- as.data.frame(c(1:49))
set.seed(32201303) 
L <- L[sample(nrow(L), 10, replace = FALSE),] # sample 10 locations
WAUS <- WAUS[(WAUS$Location %in% L),]
WAUS <- WAUS[sample(nrow(WAUS), 2000, replace = FALSE),] # sample 2000 rows

# more humd than today
more_humid <- sum(WAUS$MHT == 1, na.rm = TRUE)
# less humid than today
less_humid <- sum(WAUS$MHT == 0, na.rm = TRUE)
more_humid
less_humid
summary(WAUS)
library(skimr)
skim(WAUS)

# if WindSpeed9am == 0 and WindDir9am == NA, change WindDir9am to 'no wind'
WAUS$WindDir9am[WAUS$WindSpeed9am == 0 & is.na(WAUS$WindDir9am)] <- "no_wind"
# if WindSpeed3pm == 0 and WindDir3pm == NA, change WindDir3pm to 'no wind'
WAUS$WindDir3pm[WAUS$WindSpeed3pm == 0 & is.na(WAUS$WindDir3pm)] <- "no_wind"
# if Rainfall <= 1, NA of RainToday to No, otherwise Yes
WAUS$RainToday[WAUS$Rainfall <= 1 & is.na(WAUS$RainToday)] <- "No"
WAUS$RainToday[WAUS$Rainfall > 1 & is.na(WAUS$RainToday)] <- "Yes"
# change chr type to factor
WAUS <- as.data.frame(unclass(WAUS), stringsAsFactors = TRUE)
# change MHT value to factor
WAUS$MHT = as.factor(WAUS$MHT)
# remove Evaporation and Sunshine
WAUS <- WAUS[,c(-6,-7)]
# remove the rows if the row has NA
WAUS <- na.omit(WAUS)


set.seed(32201303)
train.row = sample(1:nrow(WAUS), 0.7*nrow(WAUS))
WAUS.train = WAUS[train.row,]
WAUS.test = WAUS[-train.row,]


# Decision Tree
library(tree)
t.fit <- tree(MHT~ ., data=WAUS.train)
summary(t.fit)
plot(t.fit)
text(t.fit, pretty = 0)

# Naïve Bayes
library(e1071)
naive.model <- naiveBayes(MHT~ ., data=WAUS.train)

# Bagging
library(adabag)
library(rpart)
bag.model <- bagging(MHT ~ ., data=WAUS.train)

# Boosting
boost.model <- boosting(MHT ~ ., data=WAUS.train)

# Random Forest
library(randomForest)
rf.model <- randomForest(MHT ~ .,data=WAUS.train)

# Decision Tree
tpredict <- predict(t.fit, WAUS.test, type = "class")
confusion_matrix_dt <- table(actual = WAUS.test$MHT, predicted = tpredict)
rownames(confusion_matrix_dt) <- c("less humid tomorrow", "more humid tomorrow")
colnames(confusion_matrix_dt) <- c("less humid tomorrow", "more humid tomorrow")
confusion_matrix_dt

# Naïve Bayes
nbpredict <- predict(naive.model, WAUS.test)
confusion_matrix_nb <- table(actual = WAUS.test$MHT, predicted = nbpredict)
rownames(confusion_matrix_nb) <- c("less humid tomorrow", "more humid tomorrow")
colnames(confusion_matrix_nb) <- c("less humid tomorrow", "more humid tomorrow")
confusion_matrix_nb

# Bagging
bgpredict <- predict.bagging(bag.model, WAUS.test)
confusion_matrix_bg <- table(actual = WAUS.test$MHT, predicted = bgpredict$class)
rownames(confusion_matrix_bg) <- c("less humid tomorrow", "more humid tomorrow")
colnames(confusion_matrix_bg) <- c("less humid tomorrow", "more humid tomorrow")
confusion_matrix_bg

# Boosting
btpredict <- predict.boosting(boost.model, newdata = WAUS.test)
confusion_matrix_bt <- table(actual = WAUS.test$MHT, predicted = btpredict$class)
rownames(confusion_matrix_bt) <- c("less humid tomorrow", "more humid tomorrow")
colnames(confusion_matrix_bt) <- c("less humid tomorrow", "more humid tomorrow")
confusion_matrix_bt

# Random Forest
rfpredict <- predict(rf.model, WAUS.test)
confusion_matrix_rf <- table(actual = WAUS.test$MHT, predicted = rfpredict)
rownames(confusion_matrix_rf) <- c("less humid tomorrow", "more humid tomorrow")
colnames(confusion_matrix_rf) <- c("less humid tomorrow", "more humid tomorrow")
confusion_matrix_rf


library(ROCR)
# Decision Tree
tpredict <- predict(t.fit, WAUS.test, type = "vector")
dtRocpred <- prediction(tpredict[,2], WAUS.test$MHT)
dt_roc <- performance(dtRocpred, "tpr", "fpr")
plot(dt_roc, col = "orange", main = "ROC curve for humidity")
abline(0,1)
cauc = performance(dtRocpred, "auc")
print(as.numeric(cauc@y.values))

# Naïve Bayes
nbpredict <- predict(naive.model, WAUS.test, type = 'raw')
nbRocpred<- prediction(nbpredict[,2], WAUS.test$MHT)
nb_roc <- performance(nbRocpred, "tpr", "fpr")
plot(nb_roc, add=TRUE, col = "blueviolet")
cauc = performance(nbRocpred, "auc")
print(as.numeric(cauc@y.values))

# Bagging
bgRocpred <- prediction(bgpredict$prob[,2], WAUS.test$MHT)
bg_roc <- performance(bgRocpred, "tpr", "fpr")
plot(bg_roc, add=TRUE, col = "red")
cauc = performance(bgRocpred, "auc")
print(as.numeric(cauc@y.values))

# Boosting
btRocpred <- prediction(btpredict$prob[,2], WAUS.test$MHT)
bt_roc <- performance(btRocpred, "tpr", "fpr")
plot(bt_roc, add=TRUE, col = "green")
cauc = performance(btRocpred, "auc")
print(as.numeric(cauc@y.values))

# Random Forest
rfpredict <- predict(rf.model, WAUS.test, type = "prob")
rfRocpred <- prediction(rfpredict[,2], WAUS.test$MHT)
rf_roc <- performance(rfRocpred, "tpr", "fpr")
plot(rf_roc, add=TRUE, col = "blue")
cauc = performance(rfRocpred, "auc")
print(as.numeric(cauc@y.values))
legend(0.0, 1.0, legend=c("Decision Tree", "Naïve Bayes", "Bagging", "Boosting", "Random Forest"),
       col=c("orange", "blueviolet", "red", "green", "blue"), lty = 1:1, cex = 0.8,)

# importance for bagging model
bag.model$importance
# importance for boosting
boost.model$importance
# importance for random forest
rf.model$importance
# importance for decision tree
summary(t.fit)

# decision tree with WindGustDir, WindDir9am and WindDir3pm
t_fit_simple <- tree(MHT~ WindGustDir + WindDir9am + WindDir3pm, data=WAUS.train)
t_fit_simple
summary(t_fit_simple )
plot(t_fit_simple)
text(t_fit_simple, pretty=0)

# prediction with test data
tpredict <- predict(t_fit_simple, WAUS.test, type = "class")

# confusion matrix
confusion_matrix_dt <- table(actual = WAUS.test$MHT, predicted = tpredict)
rownames(confusion_matrix_dt) <- c("less humid tomorrow", "more humid tomorrow")
colnames(confusion_matrix_dt) <- c("less humid tomorrow", "more humid tomorrow")
confusion_matrix_dt

# ROC curve
tpredict <- predict(t_fit_simple, WAUS.test, type = "vector")
dtRocpred <- prediction(tpredict[,2], WAUS.test$MHT)
dt_roc <- performance(dtRocpred, "tpr", "fpr")
plot(dt_roc, col = "red", main = "ROC curve for humidity")
abline(0,1)

# AUC
cauc = performance(dtRocpred, "auc")
print(as.numeric(cauc@y.values))

#  best random forest 
repeat_cv <- trainControl(method = 'repeatedcv', number = 10, repeats = 4)
best_rf <- train(MHT ~ ., data = WAUS.train, method = 'rf', trControl = repeat_cv, metric = 'Accuracy')

# confusion matrix
predictionRF <- predict(best_rf, newdata = WAUS.test)
confusion_matrix<- table(actual = WAUS.test$MHT, predicted = predictionRF)
rownames(confusion_matrix) <- c("less humid tomorrow", "more humid tomorrow")
colnames(confusion_matrix) <- c("less humid tomorrow", "more humid tomorrow")
confusion_matrix

# AUC
rfredict <- predict(best_rf, WAUS.test, type = "prob")
dtRocpred <- prediction(rfredict[,2], WAUS.test$MHT)
cauc = performance(dtRocpred, "auc")
print(as.numeric(cauc@y.values))


# pre-processing
library(neuralnet)
set.seed(32201303)

# encode chr type
ann_train = model.matrix(~ WindGustDir + WindDir9am + WindDir3pm + RainToday, data = WAUS.train)
ann_test = model.matrix(~ WindGustDir + WindDir9am + WindDir3pm + RainToday, data = WAUS.test)
wtrain = cbind(WAUS.train, ann_train)
wtest = cbind(WAUS.test, ann_test)

# remove unnecessary column
wtrain = wtrain[,c(-6,-8,-9,-18,-21,-59)]
wtest = wtest[,c(-6,-8,-9,-18,-21,-59)]

# ANN
waus.nn = neuralnet(MHT ~ WindGustDirENE + WindGustDirESE + 
                      WindGustDirN + WindGustDirNE + WindGustDirNNE + WindGustDirNNW +
                      WindGustDirNW + WindGustDirS + WindGustDirSE + WindGustDirSSE + WindGustDirSSW +
                      WindGustDirSW + WindGustDirW + WindGustDirWNW + WindGustDirWSW + WindDir9amENE +
                      WindDir9amESE + WindDir9amN + WindDir9amNE + WindDir9amNNE + WindDir9amNNW + 
                      WindDir9amno_wind + WindDir9amNW + WindDir9amS + WindDir9amSE + WindDir9amSSE + 
                      WindDir9amSSW + WindDir9amSW + WindDir9amWNW + WindDir9amWSW + WindDir9amENE + 
                      WindDir3pmESE + WindDir3pmN + WindDir3pmNE + WindDir3pmNNE + WindDir3pmNNW + 
                      + WindDir3pmNW + WindDir3pmS +
                      WindDir3pmSE + WindDir3pmSSE + WindDir3pmSSW + WindDir3pmSW + WindDir3pmW +
                      WindDir3pmWNW + WindDir3pmWSW, wtrain, hidden = 2)

plot(waus.nn, rep = "best")
waus.nn$result.matrix

# prediction with test data 
waus.pred = compute(waus.nn, wtest[c(17:62)])
pred <- ifelse(waus.pred$net.result > 0.5, 1, 0)
pred <- as.data.frame(pred)

# confusion matrix
confusion_matrix <- table(actual = wtest$MHT, predicted = pred$V2)
rownames(confusion_matrix) <- c("less humid tomorrow", "more humid tomorrow")
colnames(confusion_matrix) <- c("less humid tomorrow", "more humid tomorrow")
confusion_matrix

# AUC
library(pROC)
dtRocpred <- roc(wtest$MHT, waus.pred$net.result[,2])
dtRocpred$auc

# pre-processing 
library(xgboost)
# encode chr type
xg_train = model.matrix(~ WindGustDir + WindDir9am + WindDir3pm + RainToday, data = WAUS.train)
xg_test = model.matrix(~ WindGustDir + WindDir9am + WindDir3pm + RainToday, data = WAUS.test)
# combine data set
wtrain = cbind(WAUS.train, xg_train)
wtest = cbind(WAUS.test, xg_test)

# remove unnecessary column
wtrain = wtrain[,c(-6,-8,-9,-18,-21)]
wtest = wtest[,c(-6,-8,-9,-18,-21)]

# convert factor to int type
wtrain$MHT = as.integer(wtrain$MHT) - 1
wtest$MHT = as.integer(wtest$MHT) - 1
train_labels = wtrain$MHT
test_labels = wtest$MHT

# remove MHT 
train_data <- wtrain[,-16]
test_data<- wtest[,-16]

# Xgboost
dtrain <- xgb.DMatrix(data = as.matrix(train_data), label= train_labels)
dtest <- xgb.DMatrix(data = as.matrix(test_data), label= test_labels)
xg_model <- xgboost(data = dtrain, nround = 2, objective = "binary:logistic") 
xg_pred <- predict(xg_model, dtest)

# confusion matrix
xg_pred <- predict(xg_model, as.matrix(test_data), reshape = TRUE)
xg_predDf <- as.data.frame(xg_pred)
xg_predDf <- round(xg_predDf)
confusion_matrix <- table(actual = wtest$MHT, predicted = xg_predDf$xg_pred)
rownames(confusion_matrix) <- c("less humid tomorrow", "more humid tomorrow")
colnames(confusion_matrix) <- c("less humid tomorrow", "more humid tomorrow")
confusion_matrix

# AUC
library(pROC)
xgRocpred <- roc(wtest$MHT, xg_predDf$xg_pred)
xgRocpred$auc
