set term pdf
set out "highden_compare:den-pre.pdf"
set xlabel "density"
set ylabel "pressure"
set xlabel font "Arial,15"
set ylabel font "Arial,15"
set xrange [14.7:]
#ticsはメモリ文字
set tics font "Arial,10"
#keyは凡例
set key font"Arial,16"
set key left top
plot "highden_compare:den-pre.dat" u 1:2 with lines title "理論値", "highden_compare:den-pre.dat" u 1:3 with lines title "測定値"
