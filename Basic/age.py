def can_run_for_president(age):
	return age >=35

name = "Leandro"
age = 36
answer = False

if (can_run_for_president(age)):
	 answer = True

print(f"Can {name} run for president?\n{answer}")
