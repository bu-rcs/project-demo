
# print current time
curr.time <- Sys.time()
print(paste("Current Time", curr.time))

#epoch time
#new line
print( as.integer( as.POSIXct( curr.time ) ) )

if ( is.na(curr.time) ) stop("Missing time")
