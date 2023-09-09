district_name = ["BĐ", "BTL", "CG", "ĐĐ", "HBT"]
district_population = [247100, 333300, 266800, 420900, 318000]
print(
    f"Most populated distric: {district_name[district_population.index(max(district_population))]}"
)
print(
    f"Least populated distric: {district_name[district_population.index(min(district_population))]}"
)
