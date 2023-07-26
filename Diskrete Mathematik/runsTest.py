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
s = "\pmatrix{0.8519&0.7548&0.9169&0.5246&0.7394&0.425\cr 0.5185&0.3889&0.6358&0.693&0.9865&0.6992\cr 0.4228&0.6494&0.6234&0.8867&0.7368&0.3604\cr 0.6459&0.8348&0.7253&0.8802&0.5126&0.858\cr 0.9899&0.421&0.945&0.6636&0.803&0.7133\cr 0.8991&0.6006&0.7591&0.5306&0.3606&0.8958\cr 0.5915&0.5847&0.8104&0.7844&0.9631&0.836\cr 0.5341&0.544&0.6833&0.4432&0.5065&0.6554\cr 0.5085&0.5185&0.9277&0.7491&0.5086&0.9534\cr }"
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