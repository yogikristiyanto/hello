from scipy.stats import binom

# Parameter distribusi binomial
n = 5  # jumlah tahun
p = 0.3  # probabilitas kerugian dalam satu tahun

# Menghitung probabilitas untuk setiap k dari 0 hingga 5
probabilities = [binom.pmf(k, n, p) for k in range(n+1)]

# Menampilkan hasil
for k in range(n+1):
    print(f"Probabilitas mengalami kerugian dalam {k} dari 5 tahun: {probabilities[k]:.4f}")
