import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
data = pd.read_csv("C:/Users/13279/Desktop/cs-training.csv")
print(data.info())
print(data.info())


##根据无担保循环利用将用户等级划分
sum1 = 0
for item1 in data["RevolvingUtilizationOfUnsecuredLines"]:
    if item1 <= 1:
        sum1+=item1
aveUnsecuredLines = sum1/(data["RevolvingUtilizationOfUnsecuredLines"].count())
print(aveUnsecuredLines)
for item in range(len(data["RevolvingUtilizationOfUnsecuredLines"])):
    if data["RevolvingUtilizationOfUnsecuredLines"][item]>1:
        data["RevolvingUtilizationOfUnsecuredLines"][item] = 4
    else:
        if data["RevolvingUtilizationOfUnsecuredLines"][item]< aveUnsecuredLines/2:
            data["RevolvingUtilizationOfUnsecuredLines"][item] = 1
        elif item>=aveUnsecuredLines//2 and item<aveUnsecuredLines:
            data["RevolvingUtilizationOfUnsecuredLines"][item] = 2
        elif item>=aveUnsecuredLines and item<aveUnsecuredLines*3/2:
            data["RevolvingUtilizationOfUnsecuredLines"][item] = 3
        else:
            data["RevolvingUtilizationOfUnsecuredLines"][item] = 4

#根据借款年龄，将借款还贷能力区别划分

for age_item in range(len(data["age"])):
    if data["age"][age_item]<20:
        data["age"][age_item] = 1
    elif data["age"][age_item]>=20 and data["age"][age_item]<25:
        data["age"][age_item] = 2
    elif data["age"][age_item]>=25 and data["age"][age_item]<30:
        data["age"][age_item] = 3
    elif data["age"][age_item]>=30 and data["age"][age_item]<40:
        data["age"][age_item] = 4
    elif data["age"][age_item]>=40 and data["age"][age_item]<70:
        data["age"][age_item] = 5
    else:
        data["age"][age_item] = 0

#30-59逾期但不糟糕次数还贷能力区别划分
for DaysPastDueNotWorse_item in range(len(data["NumberOfTime30-59DaysPastDueNotWorse"])):
    if data["NumberOfTime30-59DaysPastDueNotWorse"][DaysPastDueNotWorse_item]<1:
        data["NumberOfTime30-59DaysPastDueNotWorse"][DaysPastDueNotWorse_item] = 0
    elif data["NumberOfTime30-59DaysPastDueNotWorse"][DaysPastDueNotWorse_item]>=2 and data["NumberOfTime30-59DaysPastDueNotWorse"][DaysPastDueNotWorse_item]<4:
        data["NumberOfTime30-59DaysPastDueNotWorse"][DaysPastDueNotWorse_item] = 1
    elif data["NumberOfTime30-59DaysPastDueNotWorse"][DaysPastDueNotWorse_item]>=4 and data["NumberOfTime30-59DaysPastDueNotWorse"][DaysPastDueNotWorse_item]<6:
        data["NumberOfTime30-59DaysPastDueNotWorse"][DaysPastDueNotWorse_item] = 2
    else:
        data["NumberOfTime30-59DaysPastDueNotWorse"][DaysPastDueNotWorse_item] = 3
#负比率还贷能力区别划分
for DebtRatio_item in range(len(data["DebtRatio"])):
    if data["DebtRatio"][DebtRatio_item]<0.3:
        data["DebtRatio"][DebtRatio_item] = 3
    elif data["DebtRatio"][DebtRatio_item]>=0.3 and data["DebtRatio"][DebtRatio_item]<0.6:
        data["DebtRatio"][DebtRatio_item] = 2
    else:
        data["DebtRatio"][DebtRatio_item] = 1
#月收入能力划分
data["MonthlyIncome"] = data["MonthlyIncome"].fillna(data["MonthlyIncome"].mean())
ave_item1 = data["MonthlyIncome"].mean()
for income_item in range(len(data["MonthlyIncome"])):
    if data["MonthlyIncome"][income_item] <ave_item1/2:
        data["MonthlyIncome"][income_item] = 1
    elif data["MonthlyIncome"][income_item]>=ave_item1/2 and data["MonthlyIncome"][income_item]<ave_item1:
        data["MonthlyIncome"][income_item] = 2
    elif data["MonthlyIncome"][income_item]>=ave_item1 and data["MonthlyIncome"][income_item]<ave_item1*3/2:
        data["MonthlyIncome"][income_item] = 3
    else:
        data["MonthlyIncome"][income_item] = 4
print(data.info())

#贷款数量划分等级
ave_credit = data["NumberOfOpenCreditLinesAndLoans"].mean()
for CreditLinesAndLoans_item in range(len(data["NumberOfOpenCreditLinesAndLoans"])):
    if data["NumberOfOpenCreditLinesAndLoans"][CreditLinesAndLoans_item]<ave_credit/2:
        data["NumberOfOpenCreditLinesAndLoans"][CreditLinesAndLoans_item] = 0
    elif data["NumberOfOpenCreditLinesAndLoans"][CreditLinesAndLoans_item]>=ave_credit/2 and data["NumberOfOpenCreditLinesAndLoans"][CreditLinesAndLoans_item]<ave_credit:
        data["NumberOfOpenCreditLinesAndLoans"][CreditLinesAndLoans_item] = 1
    elif data["NumberOfOpenCreditLinesAndLoans"][CreditLinesAndLoans_item]>=ave_credit and data["NumberOfOpenCreditLinesAndLoans"][CreditLinesAndLoans_item]<ave_credit*3/2:
        data["NumberOfOpenCreditLinesAndLoans"][CreditLinesAndLoans_item] = 2
    else:
        data["NumberOfOpenCreditLinesAndLoans"][CreditLinesAndLoans_item] = 3
#90天逾期贷款次数

for DaysLate_item in range(len(data["NumberOfTimes90DaysLate"])):
    if data["NumberOfTimes90DaysLate"][DaysLate_item]<1:
        data["NumberOfTimes90DaysLate"][DaysLate_item] = 4
    elif data["NumberOfTimes90DaysLate"][DaysLate_item]>1 and data["NumberOfTimes90DaysLate"][DaysLate_item]<3:
        data["NumberOfOpenCreditLinesAndLoans"][CreditLinesAndLoans_item] = 3
    elif data["NumberOfTimes90DaysLate"][DaysLate_item]>=3 and data["NumberOfTimes90DaysLate"][DaysLate_item]<7:
        data["NumberOfTimes90DaysLate"][DaysLate_item] = 2
    else:
        data["NumberOfTimes90DaysLate"][DaysLate_item] = 3

#不动产贷款和额度数量等级
ave1 = data["NumberRealEstateLoansOrLines"].mean()
for RealEstateLoansOrLines_item in range(len(data["NumberRealEstateLoansOrLines"])):
    if data["NumberRealEstateLoansOrLines"][RealEstateLoansOrLines_item]<ave1/2:
        data["NumberRealEstateLoansOrLines"][RealEstateLoansOrLines_item] = 1
    elif data["NumberRealEstateLoansOrLines"][RealEstateLoansOrLines_item]>ave1/2 and data["NumberRealEstateLoansOrLines"][RealEstateLoansOrLines_item]<ave1:
        data["NumberRealEstateLoansOrLines"][RealEstateLoansOrLines_item] = 2
    elif data["NumberRealEstateLoansOrLines"][RealEstateLoansOrLines_item]>=ave1 and data["NumberRealEstateLoansOrLines"][RealEstateLoansOrLines_item]<ave1*3/2:
        data["NumberRealEstateLoansOrLines"][RealEstateLoansOrLines_item] = 3
    else:
        data["NumberRealEstateLoansOrLines"][RealEstateLoansOrLines_item] = 4

#60-89逾期但不糟糕等级划分
ave2 = data["NumberOfTime60-89DaysPastDueNotWorse"].mean()
for PastDueNotWorse_item in range(len(data["NumberOfTime60-89DaysPastDueNotWorse"])):
    if data["NumberOfTime60-89DaysPastDueNotWorse"][PastDueNotWorse_item]<ave2/2:
        data["NumberOfTime60-89DaysPastDueNotWorse"][PastDueNotWorse_item] = 1
    elif data["NumberOfTime60-89DaysPastDueNotWorse"][PastDueNotWorse_item]>ave2/2 and data["NumberOfTime60-89DaysPastDueNotWorse"][PastDueNotWorse_item]<ave2:
        data["NumberOfTime60-89DaysPastDueNotWorse"][PastDueNotWorse_item] = 2
    elif data["NumberOfTime60-89DaysPastDueNotWorse"][PastDueNotWorse_item]>=ave2 and data["NumberOfTime60-89DaysPastDueNotWorse"][PastDueNotWorse_item]<ave2*3/2:
        data["NumberOfTime60-89DaysPastDueNotWorse"][PastDueNotWorse_item] = 3
    else:
        data["NumberRealEstateLoansOrLines"][PastDueNotWorse_item] = 4

#根据家庭人口预测还贷能力
data["NumberOfDependents"]= data["NumberOfDependents"].fillna(data["NumberOfDependents"].mean())
for NumberOfDependents_item in range(len(data["NumberOfDependents"])):
    if data["NumberOfDependents"][NumberOfDependents_item]<1:
        data["NumberOfDependents"][NumberOfDependents_item] = 1
    elif data["NumberOfDependents"][NumberOfDependents_item]>=1 and data["NumberOfDependents"][NumberOfDependents_item]<3:
        data["NumberOfDependents"][NumberOfDependents_item] = 2
    elif data["NumberOfDependents"][NumberOfDependents_item]>=3and data["NumberOfDependents"][NumberOfDependents_item]<5:
        data["NumberOfDependents"][NumberOfDependents_item] = 3
    else:
        data["NumberOfDependents"][NumberOfDependents_item] = 4
judge_value = []
for item3 in range(len(data["NumberOfDependents"])):
    judge_value .append(data.iloc[item3].sum())

for item4 in range(len(judge_value)):
    if judge_value[item4]<=10:
        judge_value = '低质量客户'
    elif judge_value[item4]>10 and judge_value[item4]<20:
        judge_value[item4] = '中质量客户'
    elif judge_value[item4]>=20 and judge_value[item4]<30:
        judge_value[item4] = '中上质量客户'
    else:
        judge_value[item4] = '优质客户'
print(data.info())

with open ("C:/Users/13279/Desktop/5.txt","wb+") as f:
    for i in range(len(judge_value)):
        f.write(bytes(str(i),encoding = "utf8"))
        f.write(bytes(judge_value[i],encoding = "utf8"))
        f.write(bytes("\n",encoding = "utf8"))
f.close()






