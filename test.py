from datetime import date
d = "2020-05-10"
ds = [int(i) for i in d.split("-")]
print(
   date(ds[0], ds[1], ds[2])

)
