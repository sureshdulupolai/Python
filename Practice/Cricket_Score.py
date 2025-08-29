# 6 over = 4.5 Run Rate
# 153 Target, Abhi Uska Run Rate Kitne Hoga

import math

TotalRun = 153
OverDone = 6
RunGet = (4.5 * OverDone)

RunLeft = float(TotalRun) - float(RunGet)
TotalBallLeft = 20 - OverDone

CurrentRunRate = round(RunLeft / TotalBallLeft, 2)

print('Current Run Rate : {}'.format(CurrentRunRate))

prBallRun = math.ceil(round((CurrentRunRate / 6), 2))
print('Pr Ball Run Rate : {}'.format(prBallRun))