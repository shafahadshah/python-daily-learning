admin_permissions: set[str] = {
    "read",
    "write",
    "delete",
}

user_permissions: set[str] = {
    "read",
    "write",
}

print("Common:", admin_permissions & user_permissions)
print("All:", admin_permissions | user_permissions)
print("Admin only:", admin_permissions - user_permissions)