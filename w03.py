# BMI Calculator
# Result = W / {H^2 => H*H}

W = float(input("น้ำหนัก(กก.)"))
H = float(input("ส่วนสูง(ซม.)"))

R = W/(H/100*H/100)
R2 = f"{R:.2f}"
print(f"{R:.2f}")
print(R2)

