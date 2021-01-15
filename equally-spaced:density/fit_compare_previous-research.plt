set term pdf
set out "fit_compare_previous-research.pdf"
set xlabel "{/Arial-Italic ρ}"
set ylabel "{/Arial-Italic P}"
set xlabel font "Arial,15"
set ylabel font "Arial,15"
#ticsはメモリ文字
set tics font "Arial,10"
set xrange [0:3.5]
set yrange [0:10000]
#keyは凡例
set key font"Arial,16"
set key left top
plot "fit_compare_previous-research.dat" u 1:2 with lines linewidth 2 title "剛球流体", "fit_compare_previous-research.dat" u 1:3 with lines linewidth 2 title "調整後の5次近似値"