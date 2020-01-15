library(rstudioapi)
current.path <- getActiveDocumentContext()$path
setwd(dirname(current.path))
getwd()
list.files()

# note:
# may need to run 'grep -v "#" GCA_004171285.1_ASM417128v1_genomic.gff | awk  -F "\t" '{ if ( $8 != 0 ) {print} }' > features.gff'
# to clean up the gff prior to running this script.

gffin = "features.gff"
bedout = "features.bed"

gtf = read.delim(file = gffin, header = F)
bed = as.data.frame(cbind(as.character(gtf$V1), (gtf$V4 - 1), 
                          gtf$V5, gsub( "ID=", "", sapply( strsplit( x = as.character(gtf$V9), split = ";"), "[[", 1) ), 
                          rep(0, length(gtf$V1)), as.character(gtf$V7)), colnames = NULL)

write.table(bed, file = bedout, quote = F, sep = "\t", row.names = F, col.names = F)




