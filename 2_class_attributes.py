from congress import ElectedOfficial

assert ["D", "R", "I"] == ElectedOfficial.parties


representatives = ElectedOfficial.all()
assert type(representatives) is list
assert 442 == len(representatives)

illinois_delegation = ElectedOfficial.select_all_from_state("IL")
assert type(illinois_delegation) is list
assert 18 == len(illinois_delegation)

