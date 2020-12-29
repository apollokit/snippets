# see https://theunixtips.com/bash-brace-expansion-automatic-substitution/
echo 111-{aa,bb,cc}+{xx,yy,zz}-222
# output: 111-aa+xx-222 111-aa+yy-222 111-aa+zz-222 111-bb+xx-222 111-bb+yy-222 111-bb+zz-222 111-cc+xx-222 111-cc+yy-222 111-cc+zz-222


mv process.log{,.old} #This will move process.log to process.log.old
mv process.log.{old,oldest} #This will move process.log.old to process.log.oldest
