clc

input=[
    0.25 150 40 17 2
    11 900 20 1 10
    6 350 36 2 15
    12 450 25 10 12
    10 600 22 8 11
    5.5 375 40 12 20
    ];

fuzzy quiz_fuzzy
quiz = readfis("quis_fuzzy.fis");

rekom=evalfis(input, quiz);

output = [input, rekom];