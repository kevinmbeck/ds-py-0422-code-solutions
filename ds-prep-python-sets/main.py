trail_mix = {"m&ms", "peanuts", "raisins"}
print(trail_mix)
has_cashews = "cashews" in trail_mix
print(has_cashews)
has_peanuts = "peanuts" in trail_mix
print(has_peanuts)
trail_mix.add("pretzels")
others = {"peanuts", "banana chips", "bits of jerkey"}
trail_mix.update(others)
print(trail_mix)
trail_mix.remove("m&ms")
trail_mix.discard("raisins")
trail_mix.discard("rat poison")
print(trail_mix)
nuts = {"peanuts", "cashews", "almonds", "walnuts", "pecans"}
u = trail_mix.union(nuts)
print(u)
i = trail_mix.intersection(nuts)
print(i)
dtm = trail_mix.difference(nuts)
print(dtm)
dn = nuts.difference(trail_mix)
print(dn)
