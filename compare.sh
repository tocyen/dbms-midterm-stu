#!/bin/bash
sum_score=0

function compare_function(){

# $1 is first file
# $2 is second file
# $3 is score of single question
# $4 is the question index
if cmp -s "$1" "$2" ; then
       echo "第" $4 "題: Success";
       sum_score=$(($sum_score+$3))
   else
       echo "第" $4 "題: Failed";
fi

}

#                    學生結果            正確結果      分數  題目編號
compare_function result/Q1.result testcase/Q1.testcase 15    1
compare_function result/Q2.result testcase/Q2.testcase 15    2
compare_function result/Q3.result testcase/Q3.testcase 15    3
compare_function result/Q4.result testcase/Q4.testcase 15    4
compare_function result/Q5.result testcase/Q5.testcase 15    5
compare_function result/Q6.result testcase/Q6.testcase 5    6
compare_function result/Q7.result testcase/Q7.testcase 5    7
compare_function result/Q8.result testcase/Q8.testcase 15    8

echo "總分 : " $sum_score
