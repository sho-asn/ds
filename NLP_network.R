rm(list = ls())
# Q2
library(slam)
library(tm)
library(SnowballC)

# create corpus
cname <- file.path(".", "text")
docs <-  Corpus(DirSource((cname)))
print(summary(docs))

# Q3
# transformations (convert Hyphen into space) 
toSpace <- content_transformer(function(x, pattern) gsub(pattern, " ", x))
docs <- tm_map(docs, toSpace, "-")
# Tokenization
docs <- tm_map(docs, removeNumbers)       # remove numbers
docs <- tm_map(docs, removePunctuation)   # remove punctuation
docs <- tm_map(docs, content_transformer(tolower))        # case normalization
docs <- tm_map(docs, removeWords, stopwords("english"))   # Remove stop words 
docs <- tm_map(docs, stripWhitespace)    # remove extra white space
docs <- tm_map(docs, stemDocument, language = "english")  # Stem

# create document term matrix
dtm <- DocumentTermMatrix(docs)
dtm <- removeSparseTerms(dtm, sparse = 0.70)
dtm <- as.data.frame(as.matrix(dtm))
dtm
write.csv(dtm, "dtm.csv")  # generate csv file for document term matrix

# Q4
library(lsa)
library(proxy)
# Calculate the cosine distance
cd <- proxy::dist(dtm, method = "cosine")
cd
cd <- as.dist(cd)

# plot a hierarchical clustering
fit <- hclust(cd, method = "ward.D")
plot(fit)
plot(fit, hang = -1)

# quantitative measure of the quality of the clustering
# vector of topic labels 
topics <- c("AI","AI","AI", "AI", "AI", "LGBT", "LGBT", "LGBT", "LGBT", "LGBT", "NaturalDisaster", "NaturalDisaster", "NaturalDisaster", "NaturalDisaster", "NaturalDisaster")

# separate them into 3 groups
groups = cutree(fit, k = 3)

# create a table for quanttive anlysis
labels <- c("AI", "LGBT", "NaturalDisaster")
table <- table(Actual = topics, Predicted = groups)
colnames(table) <- c("AI", "LGBT", "NaturalDisaster")
table


# Q5
library(igraph)
dtmd <- as.matrix(dtmd)
dtmsx <- as.matrix((dtmd > 0) + 0)  #  binary matrix of dtm
ByDocMatrix <- dtmd %*% t(dtmd)     # binary matrix * its transpose
diag(ByDocMatrix) <- 0              # set leading diagonal as zero
# create graph with documents
graph <- graph_from_adjacency_matrix(ByDocMatrix, mode = "undirected", weighted = TRUE)
plot(graph)

# check for central 
# degree centrality
degree <- as.data.frame(degree(graph))
# betweenness centrality
betweenness <- as.data.frame(betweenness(graph))
# closeness centrality
closeness <- as.data.frame(closeness(graph))
# eigenvector centrality
eigenvector <- as.data.frame(eigen_centrality(graph)$vector)
# combine all centralities
central <- cbind(degree, betweenness, closeness, eigenvector)
central

# improved graph with fast greedy
cfg <- cluster_fast_greedy(as.undirected(graph))   # identify communities
plot(cfg, as.undirected(graph), vertex.label = V(graph)$role, main = "Fast Greedy")

# Q6
dtmt <- as.matrix(dtm)
dtmsx <- as.matrix((dtmt > 0) + 0)     # create binary matrix of dtm
ByTokenMatrix <- t(dtmt) %*% dtmt      # binary matrix * its transpose
diag(ByTokenMatrix) <- 0               # set leading diagonal as zero
# create graph with token
graph <- graph_from_adjacency_matrix(ByTokenMatrix, mode = "undirected", weighted = TRUE)
plot(graph)

# check for central 
# degree centrality
degree <- as.data.frame(degree(graph))
# betweenness centrality
betweenness <- as.data.frame(betweenness(graph))
# closeness centrality
closeness <- as.data.frame(closeness(graph))
# eigenvector centrality
eigenvector <- as.data.frame(eigen_centrality(graph)$vector)
# combine all centralities
central <- cbind(degree, betweenness, closeness, eigenvector)
central

# improved graph with fast greedy
cfg <- cluster_fast_greedy(as.undirected(graph))   # identify communities
plot(cfg, as.undirected(graph), vertex.label = V(graph)$role, main = "Fast Greedy")


# Q7
dtmb <- as.data.frame(dtm)
dtmb$ABS <- rownames(dtmb)        # add row names
dtm_bipar <- data.frame()
for (i in 1:nrow(dtmb)){
  for (j in 1:(ncol(dtmb)-1)){
    comb <- cbind(dtmb[i,j], dtmb[i,ncol(dtmb)], colnames(dtmb[j]))
    dtm_bipar <- rbind(dtm_bipar, comb)}}
colnames(dtm_bipar) <- c("weight", "abs", "token")
dtms_comp <- dtm_bipar[dtm_bipar$weight != 0, ]   # delete weights that is 0
dtms_comp <- dtms_comp[,c(2,3,1)]         # reorder the column names (abs, token, weight)
dtms_comp

# create bipartite graph
bip_graph <- graph.data.frame(dtmsc, directed = FALSE)
bipartite.mapping(bip_graph)
V(bip_graph)$type <- bipartite_mapping(bip_graph)$type        
V(bip_graph)$color <- ifelse(V(bip_graph)$type, "lightblue", "salmon")
V(bip_graph)$shape <- ifelse(V(bip_graph)$type, "circle", "square")  
E(bip_graph)$color <- "lightgray"
plot(bip_graph)

# improve bipartite graph
cfg <- cluster_fast_greedy(as.undirected(bip_graph))   # identify communities
plot(cfg, as.undirected(bip_graph), vertex.label = V(bip_graph)$role, main = "Fast Greedy")



