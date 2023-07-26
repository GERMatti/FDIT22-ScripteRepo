import math

std_quantil_map = {
    0.9: 1.282,
    0.95: 1.645,
    0.975: 1.960,
    0.99: 2.326,
    0.995: 2.576,
    0.999: 3.090,
    0.1: "−1.282",
    0.05: "−1.645",
    0.025: "−1.960",
    0.01: "−2.326",
    0.005: "−2.576",
    0.001: "−3.090"
}

def str_to_array(string: str):
    # Opal hack, 1337 ;)
    res = []
    string = string.replace("\pmatrix{", "")
    string = string.replace(" }", "")
    string = string.replace("\cr", "")
    for i in string.split("&"):
        if " " in i:
            res.extend(i.split(" "))
            continue
        else:
            res.append(i)
    return [float(x) for x in res]

def run_test(array):
    a = [round(x) for x in array]
    runs = 1
    prev = a[0]
    for i in a:
        if i != prev:
            prev = i
            runs += 1

    return runs
s = "\pmatrix{0.9367&0.5952&0.7083&0.4854&0.6633&0.7864&0.7242\cr 0.5406&0.9988&0.8161&0.8834&0.3929&0.539&0.9364\cr 0.5733&0.3888&0.774&0.7334&0.6634&0.774&0.7098\cr 0.6723&0.5241&0.4892&0.5097&0.8493&0.8054&0.8366\cr 0.7688&0.5939&0.8242&0.578&0.8023&0.8651&0.5963\cr 0.9909&0.782&0.5252&0.9125&0.9296&0.9608&0.4408\cr }"

res = str_to_array(s)
runs = run_test(res)
print(f"Array has {runs} runs")
mu = (len(res) / 2) + 0.5
print(f"Erwartete runs (μ): {mu}")
spread = mu / 2 - 0.5
print(f"Streuung: {spread}")

print(f"Kritischer Wert (c): {std_quantil_map[1 - 0.05/2]}")

u_hat = (runs - mu) / math.sqrt(spread)
print(f"u Dach (û): {u_hat}")

print("Liegt u Dach zwischen -c und c?")