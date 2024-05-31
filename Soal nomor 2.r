fakultas <- c("Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain")
jumlah_mahasiswa <- c(260, 28, 284, 465, 735)
akreditasi <- c("A", "A", "B", "A", "A")

info_mahasiswa <- data.frame(fakultas, jumlah_mahasiswa, akreditasi)
print(info_mahasiswa)

library(ggplot2)
gambar <- ggplot(info_mahasiswa, aes(x=fakultas, y=jumlah_mahasiswa, fill=fakultas)) +
  geom_bar(width=1, stat="identity") +
  labs(title="Jumlah Mahasiswa per Fakultas",
       x="Fakultas",
       y="Jumlah Mahasiswa") +
  theme_minimal()

print(gambar)
