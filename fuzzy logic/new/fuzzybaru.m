[System]
Name='quiz_fuzzy'
Type='mamdani'
Version=2.0
NumInputs=5
NumOutputs=1
NumRules=1
AndMethod='min'
OrMethod='max'
ImpMethod='min'
AggMethod='max'
DefuzzMethod='centroid'

[Input1]
Name='biaya_regristrasi'
Range=[0 2000]
NumMFs=6
MF1='very_low':'trimf',[-800 0 280]
MF2='low':'trimf',[200 400 600]
MF3='medium':'trimf',[550 740 780]
MF4='high':'trimf',[760 800 950]
MF5='very_very_high':'trimf',[1100 1250 1400]
MF6='very_high':'trimf',[900 1000 1200]

[Input2]
Name='biaya_kursus'
Range=[0 3000]
NumMFs=6
MF1='very_cheap':'trimf',[-200 0 700]
MF2='cheap':'trimf',[680 760 1000]
MF3='medium':'trimf',[900 1000 1600]
MF4='expensive':'trimf',[1400 1532 2200]
MF5='very_expensive':'trimf',[2000 2498 2600]
MF6='very_very_expensve':'trimf',[2400 2600 2800]

[Input3]
Name='jumlah_siswa'
Range=[0 50]
NumMFs=3
MF1='little':'trimf',[-20 0 18]
MF2='medium':'trimf',[15 25 35]
MF3='a_lot':'trimf',[30 35.5 45]

[Input4]
Name='jarak'
Range=[0 3]
NumMFs=3
MF1='dekat':'trimf',[-1.2 0 0.8]
MF2='medium':'trimf',[0.6 1.5 1.65]
MF3='far':'trimf',[1.4 1.6 2.7]

[Input5]
Name='jumlah_pertemuan'
Range=[0 40]
NumMFs=3
MF1='little':'trimf',[-16 0 19]
MF2='medium':'trimf',[14 20 23]
MF3='over':'trimf',[22 30 39]

[Output1]
Name='output1'
Range=[0 10]
NumMFs=3
MF1='less':'trimf',[-4 0 5]
MF2='decend':'trimf',[3 5 7]
MF3='good':'trimf',[6 8 12]

[Rules]
1 1 1 1 1, 1 (1) : 1
