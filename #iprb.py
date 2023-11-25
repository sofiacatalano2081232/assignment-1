#iprb
k = 28
m = 20
n = 16	
tot = k + m + n
#calculate all the pairings and prob of getting a dominant phenotype
dominant_k_= 1 #k paired with anything gives a dominant phenotype
dominant_mm =0.75
dominant_mn =0.5
dominant_nn = 0
#now we calculate all the probabilities, so taking k first and then k or m or n
takingk = k / tot
kk = takingk * (k-1)/(tot-1)* dominant_k_
km = takingk * m/(tot-1) * dominant_k_
kn = takingk * n/(tot-1) * dominant_k_

takingm = m / tot
mk = takingm * k/(tot-1) * dominant_k_
mm = takingm * (m-1)/(tot-1) * dominant_mm
mn = takingm * n/(tot-1) * dominant_mn

takingn = n / tot
nk = takingn * k/(tot-1)  * dominant_k_
nm = takingn * m/(tot-1) * dominant_mn
nn = takingn * (n-1)/(tot-1) * dominant_nn
#once we have all the cases we calculate the sum of all probabilities
total_prob = kk + km + kn + mk + mm + mn + nk + nm + nn
print(total_prob)