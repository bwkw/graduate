set term pdf
set out "dis-poen.pdf"
set xrange [0:]
set yrange [-1:4]
set xlabel "{/Arial-Italic r}"
set ylabel "{/Arial-Italic E}"
set xlabel font "Arial,15"
set ylabel font "Arial,15"
#ticsはメモリ文字
set tics font "Arial,10"
#keyは凡例
set key font"Arial,16"
plot "dis-poen.dat" u 1:2 with lines linewidth 5 title "WCA", "dis-poen.dat" u 1:3 with lines linewidth 5 title "LJ"
