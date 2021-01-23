set term pdf
set out "highden_compare:den-pre.pdf"
set xlabel "{/Arial-Italic ρ}"
set ylabel "{/Arial-Italic P}"
set xlabel font "Arial,15"
set ylabel font "Arial,15"
set xrange [14.7:]
set yrange [0.0:]
#ticsはメモリ文字
set tics font "Arial,10"
#keyは凡例
set key font"Arial,16"
set key left center
plot "highden_compare:den-pre.dat" u 1:2 with lines linewidth 3 title "理論近似値", "highden_compare:den-pre.dat" u 1:3 with lines linewidth 3 title "測定値"
