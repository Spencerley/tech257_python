# Create a frozen set named frozen_set containing elements "hello", "world".
hi = ['Hello', 'World']
frozen_set = frozenset(hi)

print(frozen_set)

# Try to add "!" to frozen_set. What happens?
# There is no add or remove method on frozenset

# Create a normal set named normal_set containing elements "let's", "learn".
normal_set = {"let's", "learn"}

# Try to add frozen_set to normal_set. Why does it work? Explain.
normal_set.add(frozen_set)
# normal_set is not a frozen set so can be added to but we would not be able to do this in reverse

# Print normal_set.
print(normal_set)

# Run your script half a dozen times.
# What do you notice about where frozen_set is added to normal_set? Hint: Look at the order of the items.
# The order of the items changes within a se as a set is unordered. Except the frozen set items stay together.

# What makes a frozen set different to a normal set? Explain.
# Frozen sets cannot be added to, removed or edited, they print telling you the method
# While parts of a set can be altered at any moment,
# components of a frozen set cannot be modified after they've been created.
# Therefore, frozen sets can be utilized as Dictionary keys or as elements in another set.
