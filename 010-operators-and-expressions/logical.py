age: int = 20
has_id: bool = True

can_enter: bool = age >= 18 and has_id
is_minor: bool = age < 18 or not has_id

print(can_enter)
print(is_minor)